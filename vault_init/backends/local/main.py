import json
import os


def write_keys(secrets):
    with open('keys.txt', 'w', encoding='utf-8') as file:
        for k in secrets["keys"]:
            file.write(k + "\n")
    file.close()
    with open("base_64_keys.txt", 'w', encoding='utf-8') as file:
        for key in secrets["keys_base64"]:
            file.write(key + "\n")
    file.close()
    with open('root_token.txt', 'w', encoding='utf-8') as file:
        file.write(secrets["root_token"])
    file.close()

