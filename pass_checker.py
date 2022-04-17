pass_user = input()

flag_upp = False
flag_low = False
flag_dig = False
flag_char = False

length_user = len(pass_user)
length_right = len(pass_user) >= 14
count = 0

for sym in pass_user:
    if ord(sym) in range(65, 91):
        flag_upp = True
        count += 1
    if ord(sym) in range(97, 123):
        flag_low = True
        count += 1
    if ord(sym) in range(48, 58):
        flag_dig = True
        count += 1
    if ord(sym) in range(33, 48) or ord(sym) in range(58, 65) or ord(sym) in range(91, 97) or ord(sym) in range(123,
                                                                                                                127):
        flag_char = True
        count += 1

if flag_upp and flag_low and flag_dig and flag_char and length_right and count == length_user:
    print("Strong password")
else:
    print("Weak password:")

if not flag_upp or not flag_low:
    print("Password must contain both lowercase and uppercase characters")
if not flag_dig:
    print("Password must contain digits")
if not flag_char:
    print("Password must contain at least one punctuation character")
if length_user < 14:
    print("Password must be at least 14 characters long")
