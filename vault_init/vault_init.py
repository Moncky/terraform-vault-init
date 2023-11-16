import json
import backends.local.main as local
import backends.aws.parameter_store as ps
import backends.aws.s3 as s3
import requests
import os

addr = os.environ.get("VAULT_ADDR", "http://127.0.0.1")
shares = int(os.environ.get("VAULT_SHARES", 2))
threshold = int(os.environ.get("VAULT_THRESHOLD", 2))
store = os.environ.get("VAULT_STORE", "local")
backend = os.environ.get("VAULT_BACKEND", "local")
aws_region = os.environ.get("AWS_REGION", "eu-west-1")
debug = os.environ.get("DEBUG", "False")

def main():
    match vault_status(addr):
        case 200:
            print("Vault is initialized and unsealed and active")
        case 429:
            print("Vault is initialized and sealed")
        case 501:
            print("Vault is not initialized")
            if debug == "True":
                print("Initializing with the following settings: ")
                print("VAULT_ADDR: " + addr)
                print("VAULT_SHARES: " + shares)
                print("VAULT_THRESHOLD: " + threshold)
                print("VAULT_STORE: " + store)
                print("VAULT_BACKEND: " + backend)
                print("AWS_REGION: " + aws_region)
                print("DEBUG: " + debug)
                
            secrets = vault_init(addr, shares, threshold)
            store_secrets(secrets, backend, aws_region, store)
            if debug == "True":
                print("vault_status: ")
                print(secrets)
        case _:
            print("Error: Unable to connect to Vault")


def vault_status(vault_addr):
    response = requests.get(vault_addr + "/v1/sys/health")
    return response.status_code


def vault_init(vault_addr, shares, threshold):
    payload = json.dumps({
        "secret_shares": shares,
        "secret_threshold": threshold
    })
    try:
        print("Attempting to initialize Vault")
        req = requests.put(vault_addr + "/v1/sys/init", data=payload)
        print("Vault initialized successfully")
        if debug == "True":
            print("vault_init: ")
            print(req.json())
        return req.json()
    except:
        print("Error: Unable to initialize Vault")


def store_secrets(secrets, backend, region, store):
    if backend == "aws_parameter_store":
        ps.parameter_store(store, secrets)
    elif backend == "aws_s3":
        s3.s3_store(store, region, secrets)
    elif backend == "local":
        local.write_keys(secrets)
    else:
        print("Error: Unsupported backend")


if __name__ == "__main__":
    main()
