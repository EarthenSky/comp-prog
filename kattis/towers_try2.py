import math
import fileinput
import decimal

# Tried this approach, but it is too dependent on precision, going to 
# try the same approach but 'lazily evaluate' top components

decimal.getcontext().prec = 500

# NOTE: all numbers are limited between 1 and 100

# normalize top to the range [0.5, sqrt(base)]
def normalize(top, height, base):
    while top > (base**0.5):
        # also, if it gets too big (top > 2), expand it into 10^log(top) & add a layer
        top = math.log(top, base)
        height += 1

    while top < 0.5:
        # if new_tower[0] is too small (top < 0.5), multiply it with it's child & move down a layer.
        top = base ** top
        height -= 1

    # NOTE: if top ~~= sqrt(10), then it may trigger both while loops above, but will be effectively 
    # really close to sqrt(10)

    return top, height

def normalize_10(top, height):
    while top > (10**0.5):
        # also, if it gets too big (top > 2), expand it into 10^log(top) & add a layer
        top = top.log10()
        height += 1

    while top < 0.5:
        # if new_tower[0] is too small (top < 0.5), multiply it with it's child & move down a layer.
        top = 10 ** top
        height -= 1

    # NOTE: if top ~~= sqrt(10), then it may trigger both while loops above, but will be effectively 
    # really close to sqrt(10)

    return top, height

# converts a tower to base 10 representation
def to_base_10_tower(tower):
    # remove all values above the top most 1
    for i, ai in enumerate(tower):
        if ai == 1:
            tower = tower[:i]
            break

    top = decimal.Decimal(0)
    height = 1
    tower.reverse()
    for i, ai in enumerate(tower):
        ai = decimal.Decimal(ai)
        #print(ai)
        if i == 0:
            top = ai # eq (0)
        elif i == 1:
            top *= ai.log10() # eq (0)
            height += 1
        elif ai == 10:
            height += 1
        else:
            carry = ai.log10().log10() # eq (2)
            for j in range(i - 2):
                # eq (3, 4)
                if carry > 0:
                    compute_offset = lambda a, b: ((10 ** a + b) / ((10 ** a) * b)).log10()
                    carry = carry.log10() + compute_offset(500, carry)
                elif carry < 0:
                    compute_offset = lambda a, b: ((10 ** a + b) / ((10 ** a) * -b)).log10()
                    carry = (-carry).log10() + compute_offset(500, carry)
            top += carry
            height += 1
            top, height = normalize_10(top, height)

    return normalize_10(top, height)

# converts a tower to base 10 representation
def to_base_n_tower(tower, base=10):
    # remove all values above the top most 1
    for i, ai in enumerate(tower):
        if ai == 1:
            tower = tower[:i]
            break

    top = 0 #decimal.Decimal(0)
    height = 1
    tower.reverse()
    for i, ai in enumerate(tower):
        if i == 0:
            top = ai # eq (0)
        elif i == 1:
            top *= math.log(ai, base) # eq (0)
            height += 1
        elif ai == base:
            height += 1
        else:
            carry = math.log(math.log(ai, base), base) # eq (2)
            for j in range(i - 2):
                # eq (3, 4)
                if carry > 0:
                    compute_offset = lambda a, b: math.log((base ** a + b) / ((base ** a) * b), base)
                    carry = math.log(carry, base) + compute_offset(30, carry)
                elif carry < 0:
                    compute_offset = lambda a, b: math.log((base ** a + b) / ((base ** a) * -b), base)
                    carry = math.log(-carry, base) + compute_offset(30, carry)
            top += carry
            height += 1
            top, height = normalize(top, height, base)
            #print("{} {}".format(top, height))

    return normalize(top, height, base)

# compares two towers, for sorting. Both towers must be base 10 representation
def compare_towers(t1, t2, i1, i2, eps=0.000_000_01):
    top1, height1 = t1
    top2, height2 = t2

    if height1 > height2:
        return 1
    elif height1 < height2:
        return -1
    else:
        #if abs(top1 - top2) < eps:
        #    return 0
        if top1 > top2:
            return 1
        elif top1 < top2:
            return -1
        else:
            return 0

stdin = iter(fileinput.input())
next(stdin) # ignore number
 
to_list = lambda s, i: (list(map(int, s.split("^"))), s.strip(), i)
tower_list = [to_list(line, i) for i, line in enumerate(stdin)]
#print(tower_list)
tower_list = [(to_base_n_tower(list, 100), s, i) for list, s, i in tower_list] 
#print(tower_list)

from functools import cmp_to_key
tower_list.sort(key=cmp_to_key(lambda a, b: compare_towers(a[0], b[0], a[2], b[2])))

print("Case 1:")
for list, s, _ in tower_list:
    #print(str(s))
    print(str(s) + " : " + str(list))