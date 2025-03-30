from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigateway
from constructs import Construct

class LambdaStack8935920(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.lambda_function = _lambda.Function(
            self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index_8935920.handler",
            code=_lambda.Code.from_asset("lambda")
        )

        self.api_gateway = apigateway.LambdaRestApi(
            self, "MyApiGateway",
            handler=self.lambda_function
        )
