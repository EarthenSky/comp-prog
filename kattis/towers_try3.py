import math
import fileinput
import decimal

# Tried this approach, but it is too dependent on precision, going to 
# try the same approach but 'lazily evaluate' top components

# TODO: maybe just comparing the top & bottoms of a number, then converting it to a base_10 tower after 
# the top & bottom have been removed first would help improve precision? I know it's a trivial case, but 
# maybe there are only trivial numbers that are close like this...

# TODO: see tower9, it has an error where 2^4, 4^2 and 16 are all treated differently

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

    # NOTE: if top ~~= sqrt(base), then it may trigger both while loops above, but will be effectively 
    # really close to sqrt(base)

    return top, height

# converts a tower to base representation
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
                    carry = math.log(carry, base) + compute_offset(15, carry)
                elif carry < 0:
                    compute_offset = lambda a, b: math.log((base ** a + b) / ((base ** a) * -b), base)
                    carry = math.log(-carry, base) + compute_offset(15, carry)
            top += carry
            height += 1
            top, height = normalize(top, height, base)
            #print("{} {}".format(top, height))

    tower.reverse()
    return normalize(top, height, base)

def fix_top(t):
    while len(t) > 1:
        top = t[len(t)-1]
        under = t[len(t)-2]
        # if the top could reduce, then reduce it
        if top < 7 and under < 11 and (under ** top) <= 100:
            t.pop()
            t[len(t)-1] = under ** top
        else:
            break # could not reduce
    return t

# compares two towers, for sorting. Both towers must be base 10 representation
def compare_towers(t1, t2, i1, i2, eps=0.000_000_01):
    top1, height1 = t1
    top2, height2 = t2

    if height1 > height2:
        return 1
    elif height1 < height2:
        return -1
    else:
        # TODO: remove top elements in the tower that are shared & recompute
        #if abs(top1 - top2) < eps:
        #    return 0
        if top1 > top2:
            return 1
        elif top1 < top2:
            return -1
        else:
            return 0
        
def compare_tower_slow(ta, tb, eps=0.000_000_01):
    t1 = ta.copy()
    t2 = tb.copy()
    #print("cmp 1: {} {}".format(len(t1), len(t2)))
    if len(t1) > len(t2):
        return 1
    elif len(t1) < len(t2):
        return -1
    else: #len(t1) == len(t2):
        # NOTE: helps, but doesn't solve!
        # remove top equalities (unsure if this is allowed)
        for i in reversed(range(len(t1))):
            if t1[i] == t2[i]:
                t1.pop()
                t2.pop()
            else:
                break
        
        #print("cmp 2: {} {}".format(t1, t2))

        # deal with empty-list case
        if len(t1) == 0 and len(t2) == 0:
            return 0
        elif len(t2) == 0:
            return 1
        elif len(t1) == 0:
            return -1        

        pair1 = to_base_n_tower(t1)
        pair2 = to_base_n_tower(t2)

        #print("cmp 3: {} {}".format(pair1, pair2))
        
        return compare_towers(pair1, pair2, 0, 0)

stdin = iter(fileinput.input())
next(stdin) # ignore number
 
to_list = lambda s, i: (list(map(int, s.split("^"))), s.strip(), i)
tower_list = [to_list(line, i) for i, line in enumerate(stdin)]
#print(tower_list)
tower_list = [(to_base_n_tower(fix_top(list)), fix_top(list), s, i) for list, s, i in tower_list] 
#print(tower_list)

from functools import cmp_to_key
#tower_list.sort(key=cmp_to_key(lambda a, b: compare_towers(a[0], b[0], a[3], b[3])))
tower_list.sort(key=cmp_to_key(lambda a, b: compare_tower_slow(a[1], b[1])))

print("Case 1:")
for pair, list, s, _ in tower_list:
    print(str(s))
    #print(str(s) + " : " + str(pair))