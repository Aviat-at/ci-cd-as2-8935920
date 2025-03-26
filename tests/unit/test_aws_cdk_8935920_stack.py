import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_8935920.aws_cdk_8935920_stack import AwsCdk8935920Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_8935920/aws_cdk_8935920_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdk8935920Stack(app, "aws-cdk-8935920")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
