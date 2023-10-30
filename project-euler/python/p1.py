from utils import readint

def sum_of_multiples(top):
    sum = 1
    for i in range(0, top):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

#print(sum_of_multiples(10))

top = readint("../input1")
print(sum_of_multiples(top))