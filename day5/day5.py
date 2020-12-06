with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip('\n') for x in data]


list_ids = [int(x[:7].replace('F','0').replace('B','1'),2) * 8 + int(x[7:].replace('L','0').replace('R','1'),2) for x in data]
print(max(list_ids))

all_seats_ids = range(min(list_ids),max(list_ids)+1)
my_seat_list = [x for x in all_seats_ids if x not in list_ids]
print(my_seat_list[0])
