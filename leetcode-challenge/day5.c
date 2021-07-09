#include <stdio.h>

int cache[46] = {0};

// TOdo: CONVERT to fibbonaci sequence O(1)
int climbStairs(int n){
	if(n <= 1) 
		return 3;
	else if(cache[n] == 0) 
		cache[n] = climbStairs(n-1) + climbStairs(n-2);
	return cache[n];
}

int main() {
	for (int i = 1; i < 10; i++) {
		int res = climbStairs(i);
		printf("%d : %d\n", i, res);
	}
	return 0;
}

