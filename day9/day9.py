import itertools

with open('input.txt') as f:
    data = f.readlines()
    data = [int(x.strip('\n.')) for x in data]

preamble_length = 25

def find_number_without_sum_of_two_numbers_in_preamble(list_numbers,preamble_length):
    start_preamble_at_index = preamble_length +1
    start_at_index = 0
    def get_preamble(list_numbers,start_at_index,preamble_length):
        return list_numbers[start_at_index:start_at_index+preamble_length]

    def get_next_check_number(index):
        return list_numbers[index]
    
    def number_is_equal_sum_two_numbers_in_list(number_to_check,list_numbers):
        permutations = [p for p in itertools.product(list_numbers, repeat=2)]
        for permutation in permutations:
            permutation_list = list(permutation)
            if(sum(permutation_list) == number_to_check):
                return True
        return False

    while start_preamble_at_index <= len(list_numbers):
        preamble = get_preamble(list_numbers,start_at_index,preamble_length)
        number_to_check = get_next_check_number(start_preamble_at_index-1)
        is_valid = number_is_equal_sum_two_numbers_in_list(number_to_check,preamble)
        start_at_index += 1
        start_preamble_at_index+=1
        if not is_valid:
            return False,number_to_check
    
    return True

result = find_number_without_sum_of_two_numbers_in_preamble(data,preamble_length)
print(result)


def get_list_sum_items_equal_number(list_numbers,number_to_check):
    start_at_index = 0
    end_index = 2
    sum_list = 0

    def get_list_to_check(list_numbers,start_index,end_index):
        return list_numbers[start_index:end_index]
    
    while sum_list < number_to_check or end_index <= len(list_numbers)-1:
        temp_list = get_list_to_check(list_numbers,start_at_index,end_index)
        sum_list = sum(temp_list)
        if sum_list > number_to_check:
            start_at_index += 1
        elif sum_list < number_to_check:
            end_index+=1
        else:
            return temp_list

list_numbers = get_list_sum_items_equal_number(data,result[1])
min_list = min(list_numbers)
max_list = max(list_numbers)

print(min_list+max_list)