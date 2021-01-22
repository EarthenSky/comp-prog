# 

# solving: 
# from: https://vjudge.net/contest/418454#problem/E

# NOTE: I should have seen this problem and thought 
# 
# "I can't do this better than n time, since I have to parse all of the input values, so how can I do this in n time?
# Oh yeah, DFS / any graph search runs in n time because it remembers all the nodes it touched and never double counts."
#
# I did think of DFS really quickly, but then I tried to solve the problem in time better than n which was a mistake.

# Uses DFS
def is_digraph_connected(digraph):
    walked = set({0}) # inital item must be in set
    rec_walk_search(0, digraph, walked)

    #print(digraph)
    #print(walked)

    return len(walked) == len(digraph)


# TODO: might need touched & walked
# Returns true if a node is walked
def rec_walk_search(at, digraph, walked):
    if len(digraph[at]) == 0:
        return False

    #print("at: ", at)

    successful_exit = False

    # check adjacent nodes for if expansion should end
    for item in digraph[at]:
        if (item in walked) == True:
            walked.add(at)
            successful_exit = True

    # do an expansion walk
    for item in digraph[at]:
        if (item in walked) == False:
            if rec_walk_search(item, digraph, walked):
                walked.add(at)
                successful_exit = True
        #elif item in walked == True:
        #    walked.add(at)
        #    successful_exit = True

    """
    # search non-walked adjacent elements like dfs.
    for item in digraph[at]:
        if item in walked == False:
            rec_walk_search(item, digraph, walked)
    """

    return successful_exit


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

        print("1" if is_digraph_connected(digraph) else "0")

main()