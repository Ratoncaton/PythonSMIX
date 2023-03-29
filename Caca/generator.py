import random
import string

for n in range(16):
    print((random.choice(string.ascii_letters + (string.digits * 3))), end="")
