
with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]


def tree_path(n_right,n_down):
    number_trees = 0
    tree = '#'
    deep_lines = len(data)
    deep_lines =  deep_lines / n_down + (deep_lines % n_down > 0)
    initial_fields = len(data[0])
    for i in range(deep_lines):
        pos = (i * n_right) % initial_fields
        if data[i*n_down][pos] == tree:
            number_trees += 1
    
    return number_trees


print(tree_path(3,1))

list_trees_encounter = [tree_path(x[0],x[1]) for x in [(1,1),(3,1),(5,1),(7,1),(1,2)]]
prod_trees_encounter = 1
for x in list_trees_encounter:
    prod_trees_encounter *= x

print(prod_trees_encounter)
