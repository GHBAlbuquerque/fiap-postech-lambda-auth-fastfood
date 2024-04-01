data "archive_file" "zip" {
  type        = "zip"
  source_file = "../lambda/hello.js"
  output_path = "../lambda/hello.zip"
}

resource "aws_lambda_function" "postech-lambda-auth-fastfood" {
  filename         = data.archive_file.zip.output_path
  source_code_hash = filebase64sha256(data.archive_file.zip.output_path)

  function_name = var.project_name
  # role          = aws_iam_role.lambda_role.arn
  role          = var.lab_role_arn
  handler       = "hello.handler"
  runtime       = "nodejs18.x"
  timeout       = 10
  # publish       = true
}

resource "aws_cloudwatch_log_group" "convert_log_group" {
  name = "/aws/lambda/${aws_lambda_function.postech-lambda-auth-fastfood.function_name}"
}