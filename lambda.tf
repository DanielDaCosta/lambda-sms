data "aws_caller_identity" "current" {}

data "archive_file" "lambda_with_dependencies" {
  source_dir  = "${path.module}/lambda/"
  output_path = "${path.module}/${local.name_dash}-${var.lambda_name}.zip"
  type        = "zip"
}

resource "aws_lambda_function" "lambda_sms" {
  description      = "Send SMS to user"
  function_name    = "${local.name_dash}-${var.lambda_name}"

  filename         = data.archive_file.lambda_with_dependencies.output_path
  source_code_hash = data.archive_file.lambda_with_dependencies.output_base64sha256

  handler          = "handler.lambda_handler"
  runtime          = "python3.7"

  timeout          = 300
  memory_size      = 128

  role             = data.aws_iam_role.lambda_exec_role.arn

  environment {
    variables = {
      ENV = local.name_dash
    }
  }

  reserved_concurrent_executions = 30

  depends_on = [
    aws_cloudwatch_log_group.log_lambda
  ]

  tags = {
    Product = local.name_dash
  }
}
