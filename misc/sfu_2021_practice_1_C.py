# SOLVED

# solving: 
# from: 

def get_sum(sub_list):
    t = 0
    for v, i in sub_list:
        t += v
    return t

def get_time(sub_list, time):
    t = 0
    for v, i in sub_list:
        t += v
        if t >= time: return i # case: this was song.
    return -1 # ERROR: no time found

def main():
    inlist = input().split(" ")
    n, m = int(inlist[0]), int(inlist[1])

    expanded_playlist = [[]] # a list of list of tuples
    seconds_per_section = 10000 # play with this to get better or worse performance
    head = 0

    for i in range(0, n):
        inlist = input().split(" ")
        #print(inlist)
        ci, ti = int(inlist[0]), int(inlist[1])
        total_time = ti * ci

        while total_time >= (seconds_per_section - get_sum(expanded_playlist[head])):
            inc_amount = seconds_per_section - get_sum(expanded_playlist[head])
            
            expanded_playlist[head] += [(inc_amount, i+1)] # TODO: add another sub list -> 3 layers
            total_time -= inc_amount
            
            # add a new node
            head += 1
            expanded_playlist += [[]]

        expanded_playlist[head] += [(total_time, i+1)]

    #print(expanded_playlist)

    for vi in input().split(" "):
        #print(vi)
        vi = int(vi)
        section = vi // seconds_per_section
        internal_time = vi % seconds_per_section
        print( "{}".format(get_time(expanded_playlist[section], internal_time)) )

main()