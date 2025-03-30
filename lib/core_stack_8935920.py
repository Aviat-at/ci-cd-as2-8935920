from aws_cdk import Stack, RemovalPolicy
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_dynamodb as dynamodb
from constructs import Construct

class CoreStack8935920(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.bucket = s3.Bucket(self, "MyS3Bucket", versioned=True)

        self.table = dynamodb.Table(
            self, "MyDynamoDBTable",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            table_name="MyTable",
            removal_policy=RemovalPolicy.DESTROY
        )
