from aws_cdk import App
from lib.iam_stack_8935920 import IAMStack8935920
from lib.core_stack_8935920 import CoreStack8935920
from lib.lambda_stack_8935920 import LambdaStack8935920
from lib.pipeline_stack_8935920 import PipelineStack8935920

app = App()
IAMStack8935920(app, "IAMStack8935920")
CoreStack8935920(app, "CoreStack8935920")
LambdaStack8935920(app, "LambdaStack8935920")
PipelineStack8935920(app, "PipelineStack8935920")
app.synth()
