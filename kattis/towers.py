import math
import fileinput

from functools import cmp_to_key

# all numbers are limited between 1 and 100

# converts a tower to base 10 representation
def old_to_base_n_tower(tower, base=10):
    #print("start, " + str(tower))

    new_tower = []
    for ai in tower:
        if ai <= base:
            if len(new_tower) == 0:
                new_tower += [ai]
            else:
                # A
                top = new_tower.pop()
                top = top ** ai
                
                #print("\t" + str(top) + " : " + str(math.log(10, base)))

                # current element is larger than 10, so can be broken down
                while math.log(top, base) > 1: 
                    top = math.log(top, base)
                    new_tower += [base]

                new_tower += [top]
        else:
            # break down ai, because it's currently too big
            tmp_tower = []
            while ai > base:
                ai = math.log(ai, base) 
                tmp_tower += [base]

            tmp_tower += [ai]

            print(tmp_tower)

            for tmp_ai in tmp_tower:
                print(new_tower)
                if len(new_tower) == 0:
                    new_tower += [tmp_ai]
                else:
                    # A
                    top = new_tower.pop()
                    top = top ** tmp_ai
                    
                    # current element is larger than 10, so can be broken down
                    while math.log(top, base) > 1: 
                        top = math.log(top, base)
                        new_tower += [base]

                    new_tower += [top]
    
    #print(new_tower)
    return new_tower, (len(new_tower), new_tower[-1])

# a new recursive version, that is actually correct
def to_base_n_tower(tower, base=10):
    # for each element:
    # - break el into two
    pass

# NOTE: there might be problems with double precision, however if we do a sufficiently small epsilon, we'll probably be fine
# compares two towers, for sorting. Both towers must be base 10 representation
# -1 means <
# 1 means >
# 0 means =
def compare_towers(ta, ai, tb, bi, eps=0.000_000_000_000_1):
    #print(ta)

    if ta[0] < tb[0]:
        return -1
    elif ta[0] > tb[0]:
        return 1
    elif ta[0] == tb[0]:
        if math.fabs(ta[1] - tb[1]) < eps:
            if ai < bi:
                return -1
            else:
                return 1
        elif ta[1] < tb[1]:
            return -1
        elif ta[1] > tb[1]:
            return 1
        
    # assert: control should never reach here, unless eps is too small & ta[1]==tb[1]
    return -99

stdin = iter(fileinput.input())
next(stdin)

# (list, string)
tower_list = [(list(map(int, line[:-1].split("^"))), line[:-1], i) for i, line in enumerate(stdin)]
#print(tower_list)

tower_list = [(to_base_n_tower(list), str, i) for list, str, i in tower_list] 
#print(tower_list)

tower_list.sort(key=cmp_to_key(lambda a, b: compare_towers(a[0][1], a[2], b[0][1], b[2])))

print("Case 1:")
for list, s, i in tower_list:
    #print(s)
    print(str(s) + " : " + str(list))
