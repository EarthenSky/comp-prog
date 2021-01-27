# unsolved

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
# import sys
# sys.setrecursionlimit(4 * 10**6 + 1000)
# YEP! -> Error had to do with recursion limit

# NOTE: This algorithm is a bit inefficient, although it runs in time O(m * n) ~ O(n^3), with a better avg case
# Uses pseudo DFS -> by walkable, I mean any position can get to any other position
def is_digraph_strongly_connected(digraph):
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

# TODO: this one
# A non-recursive version that it logically different.
def is_digraph_strongly_connected_fast(digraph):
    walkable = set({0})

    frontier = []
    frontier.append(0)

    while len(frontier) != 0:
        head = frontier.pop() # take one from frontier
        current_path = [head]
        current_path_set = set({head}) # NOTE: replace this with current_path to speed up performance on smaller graphs

        child_stack = []

        # find a single loop
        hit_walkable = False
        while not hit_walkable:
            children = []

            print("current_path -> ", current_path)

            # look through all children
            for item in digraph[head]:
                if item in walkable: # item in current_path_set or 
                    hit_walkable = True
                elif not item in current_path_set: # don't walk back onto self, unless self is walkable
                    children.append(item)
            
            # if no children are walkable, then the path must take one step
            if not hit_walkable:
                # case: there is nowhere left for the current path to go -> the graph is not strongly connected
                if len(children) == 0: 
                    children = current_path.pop()
                    # EDIT: TODO: recurse backwards
                else:
                    head = children.pop()
                    current_path += [head]
                    current_path_set.add(head)
            
            child_stack.append(children)
        
        # case: at least one child is walkable, so the current path is all walkable
        for item in current_path:
            walkable.add(item)

        # add children from child_stack to the frontier:

    return len(walkable) == len(digraph) # returns true if all nodes are walkable

# A non-recursive version that it logically different.
# NOTE: this does not work because it needs one more list which determines which local_frontier spaces can be re-checked.
# TODO: just do the walk in backwards order and use a stack to hold the items. If a space is ignored, then it will simply 
# not be retraversed & will show up as not an element in the walkable set.
def is_digraph_strongly_connected_fast_complicated(digraph):
    walkable = set({0})

    frontier = []
    frontier.append(0)

    while len(frontier) != 0:
        head = frontier.pop() # take one from frontier
        current_path_set = set({head}) # NOTE: remove this with current_path to speed up performance on smaller graphs

        local_frontier = []

        # find a single loop
        hit_walkable = False
        while not hit_walkable:
            children = []

            #print("current_path -> ", current_path_set)
            
            hit_path = False

            # look through all children
            for item in digraph[head]:
                if item in walkable:
                    hit_walkable = True
                elif not item in current_path_set: # don't walk back onto self
                    children.append(item)
                elif item in current_path_set:
                    hit_path = True
            
            # if no children are walkable, then the path must take one step
            if not hit_walkable:
                # case: there is nowhere left for the current path to go -> the graph is not strongly connected
                if len(children) == 0 and not hit_path: 
                    return False
                elif len(children) == 0 and hit_path:
                    # case: we hit a dead end and the local frontier is empty so we truly have nowhere else to go.
                    # TODO: track the depth of the local_frontier -> can only take an item from local frontier if it is accessible from the current node.
                    #       will need to make a depth tracking chart for figuring out which connections can go where.
                    # OR -> just do it more traditionally recursively
                    if len(local_frontier) == 0: 
                        return False

                    # no children left, but we hit our own path, so we can keep going with any local frontier item
                    head = local_frontier.pop()
                    current_path_set.add(head)
                else:
                    # start with any item in children
                    head = children.pop()
                    current_path_set.add(head)
            
            local_frontier += children
        
        # case: at least one child is walkable, so the current path is all walkable
        for item in current_path_set:
            walkable.add(item)

        # copy local frontier to main frontier
        frontier += local_frontier

    return len(walkable) == len(digraph) # returns true if all nodes are walkable

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

        print("1" if is_digraph_strongly_connected_fast(digraph) else "0")

main()