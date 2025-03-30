from aws_cdk import Stack
from aws_cdk import aws_iam as iam
from constructs import Construct

class IAMStack8935920(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # 🔹 Lambda Role
        self.lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # 🔹 CodePipeline Role
        self.pipeline_role = iam.Role(
            self, "CodePipelineRole8935920",
            assumed_by=iam.ServicePrincipal("codepipeline.amazonaws.com"),
            description="Allows CodePipeline to deploy CDK stacks and access Secrets Manager"
        )

        # 🔹 CodeBuild Role
        self.codebuild_role = iam.Role(
            self, "CodeBuildRole8935920",
            assumed_by=iam.ServicePrincipal("codebuild.amazonaws.com"),
            description="Allows CodeBuild to synth and deploy CDK app"
        )

        # ✅ SSM + S3 Asset Bucket permissions for CodeBuild
        self.codebuild_role.add_to_policy(iam.PolicyStatement(
            actions=[
                "ssm:GetParameter",
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket",
                "s3:DeleteObject"
            ],
            resources=[
                f"arn:aws:ssm:{self.region}:{self.account}:parameter/cdk-bootstrap/hnb659fds/version",
                f"arn:aws:s3:::cdk-hnb659fds-assets-{self.account}-{self.region}",
                f"arn:aws:s3:::cdk-hnb659fds-assets-{self.account}-{self.region}/*"
            ]
        ))

        # ✅ GitHub Secret read access for CodePipeline
        self.pipeline_role.add_to_policy(iam.PolicyStatement(
            actions=["secretsmanager:GetSecretValue"],
            resources=[
                f"arn:aws:secretsmanager:{self.region}:{self.account}:secret:github-token*"
            ]
        ))

        # ✅ Base permissions for pipeline & build to manage stack resources
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
