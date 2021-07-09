#include <stdio.h>

int main() {
	int array[20] = {42, 41, 22, 43, 34, 7, 47, 24, 36, 47, 1, 25, 6, 4, 16, 12, 7, 1, 23, 5};
	int out = maxProfit(&array, 20);
	printf("%d", out);
	return 0;
}

int maxProfit(int* prices, int pricesSize){
	int largestVal = -1;
	int largestDifference = 0;
	
	for (int i = pricesSize-1; i >= 0; i--) {
		largestVal = prices[i] > largestVal ? prices[i] : largestVal;
		largestDifference = (largestVal - prices[i]) > largestDifference ? (largestVal - prices[i]) : largestDifference;	
	}

	return largestDifference;
}
