#
# lambda assume role policy
#

# trust relationships
#data "aws_iam_policy_document" "lambda_assume_role_policy" {
#  statement {
#    actions = ["sts:AssumeRole"]
#    principals {
#      type        = "Service"
#      identifiers = ["lambda.amazonaws.com"]
#    }
#  }
#}
#
#resource "aws_iam_role" "lambda_role" {
#  name               = "${var.project_name}-lambda-role"
#  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role_policy.json
#}


resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = jsonencode({
    Version: "2012-10-17",
    Statement: [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  })
}