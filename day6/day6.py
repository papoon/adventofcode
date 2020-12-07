with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip('\n') for x in data]

list_diferent_answers = []
list_tmp = []
list_group_answers = []
for x in data:
    if x != '':
        list_tmp.append(x)
    else:
        if len(list_tmp) > 0:
            list_group_answers.append(set(list_tmp))
            diferent_answers = len(set(''.join(list_tmp)))
            list_diferent_answers.append(diferent_answers)
            list_tmp = []

list_diferent_answers.append(diferent_answers)
list_group_answers.append(set(list_tmp))

print(sum(list_diferent_answers))


number_answers_all_yes = 0
for x in list_group_answers:
    group_answers = sorted(x, reverse=False) 
    group_answers = sorted(group_answers,  key=len , reverse=True)
    if len(group_answers) == 1:
        number_answers_all_yes += len(group_answers[0])
    else:
        if len(group_answers[0]) > 1:
            for t in group_answers[0]:
                number_answers_all_yes += ''.join(group_answers[1:]).count(t) == len(group_answers[1:])
     
print(number_answers_all_yes)

