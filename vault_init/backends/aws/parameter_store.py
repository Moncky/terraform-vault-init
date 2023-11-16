import boto3


def client(store, region):
    ssm = boto3.client(store, region_name=region)
    return ssm


def parameter_store(param_path, secrets):
    ssm = client("ssm", "us-east-1")
    for s in secrets:
        ssm.put_parameter(
            Name=param_path,
            Description='This is a test parameter',
            Value=s,
            Type='SecureString',
            KeyID='string',
        )
