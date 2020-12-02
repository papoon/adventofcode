

goal = 2020;
with open('input.txt') as f:
    data = f.readlines()
    data = [int(x.strip()) for x in data]


def product2(data):
    for i in data:
        for x in data:
            if i + x == 2020:
                print('result is: ' + str(i*x))
                return

def product3(data):
    for i in data:
        for x in data:
            for v in data:
                if i + x + v == 2020:
                    print('result is: ' + str(i*x*v))
                    return


product2(data)
product3(data)

            
    