with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip('\n.') for x in data]


s = [x.split('contain') for x in data]

bags_dict = {}
for x in s:
    bags_dict[x[0].replace('bags','').replace('bag','').strip()] = [r.split(',') for r in x[1:]][0]


def search_bags(bags_dict, bag, bags_in):
    for c in bags_dict:
        for bags in bags_dict[c]:
            if bag in bags:
                bags_in[c.rstrip()] = bags_dict[c]
                search_bags(bags_dict, c.rstrip().replace('bags','').replace('bag',''), bags_in)
    return bags_in

def number_bags_in(bag, bags):
    number = 0
    for bag in bags[bag]:
        bag = bag.strip()
        if bag[0].isdigit():
            number += int(bag[0]) + int(bag[0]) * number_bags_in(bag[2:].replace('bags','').replace('bag','').strip(), bags)
    return number

print(len(search_bags(bags_dict, 'shiny gold', {})))
print(number_bags_in('shiny gold', bags_dict))

