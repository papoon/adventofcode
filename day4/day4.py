import sys
import re

with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip('\n') for x in data]

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
optional_fields = ['cid']
list_passport_dict = []
passport_dict = {}
for x in data:
    if x == '' :
        list_passport_dict.append(passport_dict)
        passport_dict = {}
        continue
    itens = x.split(' ')
    for item in itens:
        key,value = item.split(':')
        passport_dict[key] = value
list_passport_dict.append(passport_dict)


number_valid_passwords = 0
valid_passports = []
for passport in list_passport_dict:
    passport_fields = sorted(passport.keys())
    if passport_fields == sorted(required_fields) or passport_fields == sorted(required_fields + optional_fields): 
        valid_passports.append(passport)

print(len(valid_passports))

number_valid_passports =0
for x in valid_passports:
    number_valid_passports += int(x['byr']) >= 1920 and int(x['byr']) <= 2002 \
    and int(x['iyr']) >= 2010 and int(x['iyr']) <= 2020 \
    and int(x['eyr']) >= 2020 and int(x['eyr']) <= 2030 \
    and x['ecl'] in ['amb' ,'blu' ,'brn', 'gry', 'grn', 'hzl' ,'oth'] \
    and x['pid'].isdigit() and len(x['pid']) == 9 \
    and len(x['hcl'][1:]) == 6 and len(re.findall("[^0-9a-f]", x['hcl'][1:])) == 0 \
    and x['hgt'][:-2].isdigit() and (x['hgt'][:-2] in map(str,range(150,194)) and x['hgt'][-2:] == 'cm' or x['hgt'][:-2] in map(str,range(59,77)) and x['hgt'][-2:] == 'in')


print(number_valid_passports)