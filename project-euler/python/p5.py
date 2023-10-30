def smallest_evenly_divisible(numbers):
	out = 1
	for n in numbers:
		for i in range(0, len(numbers)):
			if numbers[i] % n == 0:
				numbers[i] = numbers[i] // n
		out *= n
	return out

print(smallest_evenly_divisible( list(range(1,11)) ))
print(smallest_evenly_divisible( list(range(1,21)) ))

