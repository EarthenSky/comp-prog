def sum_of_squares(seq):
    return sum([s*s for s in seq])

def square_of_sum(seq):
    return sum(seq) * sum(seq)

print(square_of_sum(range(1, 11)) - sum_of_squares(range(1, 11)))
print(square_of_sum(range(1, 101)) - sum_of_squares(range(1, 101)))