# AWS CDK CI/CD Deployment Project – Full Documentation

## Overview

This project sets up a full CI/CD pipeline using **AWS CDK (Python)** to deploy a serverless application. It includes:

- Lambda + API Gateway deployment
- CI/CD via CodePipeline & CodeBuild
- Role-based IAM access control
- S3 assets and bootstrap management

---

## Project Structure

- `IAMStack` – IAM roles for CodeBuild, CodePipeline, and Lambda
- `CoreStack` – Core resources (e.g., buckets)
- `LambdaStack` – Deploys Lambda + API Gateway
- `PipelineStack` – CI/CD pipeline with GitHub trigger
- `buildspec.yml` – Build instructions for CodeBuild
- `.github/workflows` – GitHub Actions config (optional)
- `cdk.json`, `app.py` – CDK entry point and config

---

## Prerequisites

1. AWS CLI configured (`aws configure`)
2. CDK installed globally: `npm install -g aws-cdk`
3. Python v3.9+ installed with `virtualenv`
4. Bootstrapped AWS environment for CDK:
   ```bash
   cdk bootstrap      --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess      --trust arn:aws:iam::<account-id>:role/<build-role>      aws://<account-id>/<region>
   ```

---

## Deployment Steps

### Step 1: Setup virtualenv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Deploy IAM Stack

```bash
cdk deploy IAMStack8935920
```

### Step 3: Deploy All Stacks

```bash
cdk deploy --all
```

---

## CodeBuild Execution Flow

1. Install Python & CDK
2. Install Python dependencies
3. Run `cdk synth`
4. Run `cdk deploy --all`

**Success Output Example**:
- IAMStack8935920 (no changes)
- LambdaStack8935920 (created)
- PipelineStack8935920 (GitHub integrated)

---

## Common Errors and Fixes

###  S3 Bucket Access Denied

**Message**: Bucket exists, but access denied

**Fix**:
- Ensure `cdk-hnb659fds-assets-<account>-<region>` exists
- Add S3 permissions in `codebuild_role` for:
  - `s3:GetObject`, `s3:PutObject`, `s3:ListBucket`

---

### Invalid Principal in Policy

**Message**: `Invalid principal in policy: "AWS":"arn:aws:iam::<account>:role/<role-name>"`

**Fix**:
- The role doesn’t exist yet.
- Deploy `IAMStack` first.
- Use correct role ARN in bootstrap.

---

### CDK Bootstrap Failed

**Message**: CDKToolkit failed to deploy

**Fix**:
- Make sure role used in `--trust` exists
- Replace placeholders in `cdk bootstrap` with actual role ARNs

```bash
cdk bootstrap   --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess   --trust arn:aws:iam::<account>:role/<CodeBuildRole>   aws://<account>/<region>
```

---

## Permissions Summary

### CodeBuild Role

- `s3:*` (for asset access)
- `ssm:GetParameter` (for CDK bootstrapping)
- `cloudformation:*`, `iam:*`, `logs:*`

### CodePipeline Role

- `secretsmanager:GetSecretValue` (for GitHub token)
- `codebuild:*`, `cloudformation:*`, `iam:*`

---

## Final Notes

- Always deploy `IAMStack` first to avoid bootstrap/role errors.
- Confirm GitHub token is securely stored in Secrets Manager.
- Run `cdk bootstrap` with correct `--trust` role before first deploy.

---

## Author

- Built by **Akash** using AWS CDK + Python


---

## License

MIT License – Free to use, modify, and share.