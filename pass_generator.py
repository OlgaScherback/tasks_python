import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
char = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

weak = lower + upper + digit + char
length = 14
password = "".join(random.sample(weak, length))
password_right = password + chr(random.randint(48, 58)) + chr(random.randint(65, 91)) + chr(random.randint(97, 123)) +\
                 chr(random.randint(33, 48))
print(password_right)
