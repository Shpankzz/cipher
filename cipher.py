import random
import string
import math

alpha = (
    "".join(
        eval("string.{}".format(x)) for x in ["ascii_letters", "digits", "punctuation"]
    )
    + " "
) * 2

# generates and saves a key for the cipher
def generate_key():
    length = random.randint(40, 60)
    key = []
    for x in range(length):
        choose_value = random.randint(0, len(alpha) - 1)
        if choose_value > 9:
            key.append(alpha[choose_value])
        else:
            key.append(str(alpha.find(alpha[choose_value])))
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
    "I want to suck Troys big peen :)",
)
test2 = cipher(key, test.encrypt())
print(f"key: {key}")
print(f"encrypted: {test.encrypt()}")
print(f"decrypted: {test2.decrypt()}")

# print(generate_key())
