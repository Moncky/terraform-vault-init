import io

import boto3


# Write out the secrets to objects in the priovided S3 bucket

def client(store, region):
    s3 = boto3.client(store, region_name=region)
    return s3


def s3_store(bucket_name, region, secrets):
    s3 = client("s3", region)

    keys = "\n".join(secrets["keys"])
    s3.put_object(
        Bucket=bucket_name,
        Body=io.BytesIO("\n".join(secrets["keys"]).encode("utf-8")),
        Key="keys.txt"
    )

    s3.put_object(
        Bucket=bucket_name,
        Body=io.BytesIO("\n".join(secrets["keys_base64"]).encode("utf-8")),
        Key="keys_base64.txt"
    )

    s3.put_object(
        Bucket=bucket_name,
        Body=io.BytesIO(secrets["root_token"].encode("utf-8")),
        Key="root_token.txt"
    )
