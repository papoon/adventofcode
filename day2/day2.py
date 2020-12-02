
validPasswords1 = validPasswords2 = 0
with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]

for x in data:
    listTmp = x.split(' ')
    minum,maximun = listTmp[0].split('-')
    letter = listTmp[1].strip(':')
    password = listTmp[2]
    minum,maximun = int(minum),int(maximun)
    if(password.count(letter) >= minum and password.count(letter) <= maximun):
        validPasswords1 += 1
    if password[minum -1] == letter and password[maximun-1] != letter or password[minum -1] != letter and password[maximun -1] == letter:
        validPasswords2 += 1

print(validPasswords1)
print(validPasswords2)
