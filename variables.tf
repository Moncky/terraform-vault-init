variable "vault_host" {
  type = string
  default = "127.0.0.1"
}

variable "vault_secret_shares" {
  type = number
  default = 5
}

variable "vault_secret_threshold" {
  type = number
  default = 3
}

variable "vault_unseal_key" {
  type = string
  default = "my-unseal-key"
}
