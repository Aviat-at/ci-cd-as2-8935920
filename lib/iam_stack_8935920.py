from aws_cdk import Stack
from aws_cdk import aws_iam as iam
from constructs import Construct

class IAMStack8935920(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        self.pipeline_role = iam.Role(
            self, "CodePipelineRole8935920",
            assumed_by=iam.ServicePrincipal("codepipeline.amazonaws.com"),
            description="Allows CodePipeline to deploy CDK stacks and access Secrets Manager"
        )

        self.codebuild_role = iam.Role(
            self, "CodeBuildRole8935920",
            assumed_by=iam.ServicePrincipal("codebuild.amazonaws.com"),
            description="Allows CodeBuild to synth and deploy CDK app"
        )

        self.pipeline_role.add_to_policy(iam.PolicyStatement(
            actions=["secretsmanager:GetSecretValue"],
            resources=["arn:aws:secretsmanager:us-east-1:123456789012:secret:github-token*"]
        ))

        for role in [self.pipeline_role, self.codebuild_role]:
            role.add_to_policy(iam.PolicyStatement(
                actions=[
                    "cloudformation:*",
                    "s3:*",
                    "logs:*",
                    "codebuild:*",
                    "codepipeline:*",
                    "iam:PassRole",
                    "iam:GetRole",
                    "iam:CreateRole",
                    "iam:AttachRolePolicy"
                ],
                resources=["*"]
            ))
