from aws_cdk import Stack, SecretValue
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as codepipeline_actions
from aws_cdk import aws_codebuild as codebuild
from constructs import Construct

class PipelineStack8935920(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        pipeline = codepipeline.Pipeline(self, "MyPipeline")

        source_action = codepipeline_actions.GitHubSourceAction(
            action_name="GitHub_Source",
            owner="Aviat-at",
            repo="ci-cd-as2-8935920",
            branch="main",
            oauth_token=SecretValue.secrets_manager("github-token"),
            output=source_output
        )

        pipeline.add_stage(stage_name="Source", actions=[source_action])

        build_project = codebuild.PipelineProject(self, "BuildProject")
        build_action = codepipeline_actions.CodeBuildAction(
            action_name="Build",
            project=build_project,
            input=source_output,
            outputs=[build_output]
        )

        pipeline.add_stage(stage_name="Build", actions=[build_action])
