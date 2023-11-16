variable "vault_host" {
  type    = string
  default = "127.0.0.1"
}

variable "python_path" {
  type        = string
  default     = "/usr/bin/python3"
  description = "Path to python executable"
}

variable "use_tls" {
  type        = bool
  default     = true
  description = "Use TLS connection when connecting to Vault"
}

variable "vault_init_backend" {
  type        = string
  default     = "local"
  description = "Vault init backend type"
  validation {
    condition     = contains(["local", "aws"], var.vault_init_backend)
    error_message = "Vault init backend must be one of: local, aws"
  }
}

variable "vault_init_store" {
  type        = string
  default     = "local"
  description = "Vault init store type"
  validation {
    condition     = contains(["local", "aws_s3", "parameter_store"], var.vault_init_store)
    error_message = "Vault init store must be one of: local, aws_s3, parameter_store"
  }
}

variable "vault_init_debug" {
  type        = string
  default     = "False"
  description = "Enable debug mode for init script"
}

variable "vault_secret_shares" {
  type    = number
  default = 5
}

variable "vault_secret_threshold" {
  type    = number
  default = 3
}

variable "vault_unseal_key" {
  type    = string
  default = "my-unseal-key"
}
