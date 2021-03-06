import re

def password_ok(l,h,c,p):
    count = 0
    for char in p:
        if c == char:
            count += 1
    if count > h:
        return False
    if count < l:
        return False
    return True

def password_ok2(idx1, idx2, char, password):
    first = password[idx1-1] == char
    second = password[idx2-1] == char
    return first ^ second


file = open('day2.txt', 'r')
lines = file.readlines()
file.close()

correct_passwords = 0

for line in lines:
    parts = re.split("-|: | ", line)
    low = int(parts[0])
    high = int(parts[1])
    char = parts[2]
    password = parts[3]

    if password_ok2(low, high, char, password):
        correct_passwords += 1
    
print(correct_passwords)

