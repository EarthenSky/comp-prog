# undetermined

# solving: 
# from: https://vjudge.net/contest/418454#problem/E

# NOTE: I should have seen this problem and thought 
# 
# "I can't do this better than m time, since I have to parse all of the input values, so how can I do this in n time?
# Oh yeah, DFS / any graph search runs in m time because it remembers all the nodes it touched and never double counts."
#
# I did think of DFS really quickly, but then I tried to solve the problem in time better than n which was a mistake.
#
# EDIT: I actually had to use a modified dfs which does some back & forth tracking in order to make sure that it grabs 
# cycles that come back and hit the "walkable" areas

# This is for recursion
import sys
sys.setrecursionlimit(4 * 10**6 + 1000)
# YEP! -> Error had to do with recursion limit 

# NOTE: This algorithm is a bit inefficient, although it runs in time O(m * n) ~ O(n^3), with a better avg case
# Uses pseudo DFS -> by walkable, I mean any position can get to any other position
def is_digraph_walkable(digraph):
    walked = set({0}) # inital item must be in set
    
    #print(digraph); print(walked)

    return rec_walk_search(0, digraph, walked) and (len(walked) == len(digraph))

# NOTE: if a node returns false, then the entire algorithm exits. this reduces a lot of double counting.
# Returns true if a node is walked
def rec_walk_search(at, digraph, walked):
    if len(digraph[at]) == 0:
        return False
        
    successful_exit = False

    # check adjacent nodes for if expansion should end
    for item in digraph[at]:
        if (item in walked) == True:
            walked.add(at)
            successful_exit = True
            break

    # do an expansion walk
    for item in digraph[at]:
        if (item in walked) == False:
            if rec_walk_search(item, digraph, walked):
                walked.add(at)
                successful_exit = True
            else:
                # This is probably an indicator that we are ded.
                # TODO: make sure this is correct
                return False

    return successful_exit

# TODO: write a non-recursive version of this that it logically different.
def is_digraph_walkable_fast(digraph):
    walked = set({0})

    stack = []
    stack.append(0)

    successful_exit = False

    while len(stack) != 0:
        at = stack.pop()
        successful_exit = False

        for item in digraph[at]:
            if (item in walked) == True:
                walked.add(at)
                successful_exit = True
                break

        # do an expansion walk
        for item in digraph[at]:
            if (item in walked) == False:
                if rec_walk_search(item, digraph, walked): # Oops, accidentally recursive....
                    walked.add(at)
                    successful_exit = True
                else:
                    # This is probably an indicator that we are ded.
                    # TODO: make sure this is correct
                    successful_exit = False
                    break

        if successful_exit == False:
            return False

    return len(walked) == len(digraph)


def main():
    while True:
        invalues = input().strip().split(" ")
        n, m = int(invalues[0]), int(invalues[1])
        if n == 0 and m == 0: break

        digraph = [set({}) for _ in range(0, n)]

        for i in range(0, m):
            invalues = input().strip().split(" ")
            v, w, p = int(invalues[0])-1, int(invalues[1])-1, int(invalues[2])

            if p == 1:
                digraph[v].add(w)
            elif p == 2: 
                digraph[v].add(w)
                digraph[w].add(v)

        print("1" if is_digraph_walkable_fast(digraph) else "0")

main()