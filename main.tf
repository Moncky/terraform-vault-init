terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.23.1"
    }
    http = {
      source  = "hashicorp/http"
      version = "3.4.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "2.4.0"
    }
  }
}

locals {
  vault_host = var.use_tls ? "https://${var.vault_host}" : "http://${var.vault_host}"
}

resource "null_resource" "init" {
  provisioner "local-exec" {
    command = "${var.python_path} vault_init/vault_init.py > vault_init.out"
    //interpreter = ["${path.module}/vault_init/bin/python3.12"]
    environment = {
      VAULT_ADDR      = local.vault_host
      VAULT_SHARES    = var.vault_secret_shares
      VAULT_THRESHOLD = var.vault_secret_threshold
      VAULT_BACKEND   = var.vault_init_backend
      VAULT_STORE     = var.vault_init_backend
      DEBUG           = var.vault_init_debug
    }
  }
}

data "local_file" "vault_init_log" {
  filename   = "${path.module}/vault_init.out"
  depends_on = [null_resource.init]
}

output "vault_init_log" {
  value = data.local_file.vault_init_log.content
}

