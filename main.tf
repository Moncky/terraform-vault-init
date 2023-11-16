terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.23.1"
    }
    http = {
      source = "hashicorp/http"
      version = "3.4.0"
    }
    local = {
      source = "hashicorp/local"
      version = "2.4.0"
    }
  }
}

data "http" "init_status" {
  url = "http://${var.vault_host}/v1/sys/init"
  method = "GET"
}

resource "null_resource" "init" {
  provisioner "local-exec" {
    command = "${path.module}/vault_init/bin/python3.12 vault_init/vault_init.py > vault_init.out"
    //interpreter = ["${path.module}/vault_init/bin/python3.12"]
    environment = {
      VAULT_ADDR = "http://127.0.0.1"
      VAULT_SHARES = 1
      VAULT_THRESHOLD = 1
      VAULT_BACKEND = "local"
      VAULT_STORE = "local"
      DEBUG = "False"
    }
  }
}

data "local_file" "vault_init_log" {
  filename = "${path.module}/vault_init.out"
  depends_on = [null_resource.init]
}

output "vault_init_log" {
  value = data.local_file.vault_init_log.content
}

