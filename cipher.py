import random
import string
import math

alpha = (string.ascii_letters + string.digits + string.punctuation + " ") * 2

# generates and saves a key for the cipher
def generate_key():
    key = []
    for x in range(random.randint(40, 60)):
        choose_value = random.randint(0, len(alpha) - 1)
        key.append(alpha[choose_value])
    return "".join(key)


class cipher:
    def __init__(self, key, value):
        self.value = value
        self.key = key * ((math.floor(len(value) / len(key))) + 1)

    def encrypt(self):
        save = []
        for x in range(len(self.value)):
            save.append(alpha[alpha.find(self.value[x]) - alpha.find(self.key[x])])
        return "".join(save)

    def decrypt(self):
        save = []
        for x in range(len(self.value)):
            save.append(alpha[alpha.find(self.value[x]) + alpha.find(self.key[x])])
        return "".join(save)


key = generate_key()
test = cipher(
    key,
    "1898w90du9efu()Eu90`88dfn9adf8n=`nfas'df",
)
test2 = cipher(key, test.encrypt())
print(f"key: {key}")
print(f"encrypted: {test.encrypt()}")
print(f"decrypted: {test2.decrypt()}")
