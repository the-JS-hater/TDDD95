// Implement a function that computes what to pack in a capacity limited knapsack to maximize the total value of all the items packed. Each item has an integer value and an integer weight. The total weight of all items packed must be less than or equal to the capacity (which is a real number).
//
//Suggested API:
//int[] knapsack(capacity, value/weight[])
//The returned vector contains the indices of the chosen items.
//
//Recommended time complexity: O(n·capacity).
//

// Input:
// Values (stored in array v) # Item.value
// Weights (stored in array w) # Item.Weights
// Number of distinct items (n) # items.size()
// Knapsack capacity (W) # capacity
// NOTE: The array "v" and array "w" are assumed to store all relevant values starting at index 1.

// array m[0..n, 0..W];
// for j from 0 to W do:
//     m[0, j] := 0
// for i from 1 to n do:
//     m[i, 0] := 0
// 
// for i from 1 to n do:
//     for j from 1 to W do:
//         if w[i] > j then:
//             m[i, j] := m[i-1, j]
//         else:
//             m[i, j] := max(m[i-1, j], m[i-1, j-w[i]] + v[i])


#include <vector>
#include <algorithm>

struct Item {
	int value;
	int weight;
};


std::vector<int> knapsack(float capacity, std::vector<Item> items) {
	std::vector<int> solution = {};
	
	int matrix[items.size()][(int) capacity];
	for (int j = 0; j < capacity; j++){
		matrix[0][j] = 0;
	}

	for (int i = 1; i < items.size(); i++){
		matrix[i][0] = 0;
	}
	
	for (int i = 1; i < capacity; i++) {
		for (int j = 1; j < capacity; j++) {
			if (items[i].weight > j) {
				matrix[i][j] = matrix[i - 1][j];
			} else {
				matrix[i][j] = std::max(matrix[i - 1][j], matrix[i - 1][j - items[i].weight] + items[i].value); 
			}
		}
	}

	return solution;
}
