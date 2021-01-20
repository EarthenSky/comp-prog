# SOLVED

# solving: https://vjudge.net/contest/418454#problem/B
# from: https://codeforces.com/problemset/problem/476/B

# max 2**10
def pos_ends(sent_pos, recieved_pos, varience_values):
    if varience_values == 0:
        return (1 if sent_pos == recieved_pos else 0)
    else:
        return pos_ends(sent_pos, recieved_pos+1, varience_values-1) + pos_ends(sent_pos, recieved_pos-1, varience_values-1)

def main():
    sent = input().strip()
    recieved = input().strip()

    sent_pos = 0
    recieved_pos = 0
    varience_values = 0

    for i in range(0, len(sent)):
        if sent[i] == '+':
            sent_pos += 1
        else:
            sent_pos -= 1
        
        if recieved[i] == '+':
            recieved_pos += 1
        elif recieved[i] == '-':
            recieved_pos -= 1
        else:
            varience_values += 1
        
    if varience_values == 0 and sent_pos == recieved_pos:
        print("1.0")
        return 

    #print("{} {} {}".format(sent_pos, recieved_pos, varience_values))

    num_valid_positions = pos_ends(sent_pos, recieved_pos, varience_values)
    print("{}".format(num_valid_positions / (2**varience_values)))
    return

main()