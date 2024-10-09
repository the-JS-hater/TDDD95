// https://en.wikipedia.org/wiki/Knapsack_problem

#include <vector>
#include <algorithm>


struct Item {
	int value;
	int weight;
};


std::vector<int> knapsack(int capacity, std::vector<Item> items) {
	std::vector<int> solution = {};
	int matrix[items.size() + 1][items.size() + 1];
	
	// Following 2 loops don't affect the overall time
	// complexity, explaination furter down (nested loop)
	// O(capacity)
	for (int i = 0; i <= capacity; i++){
		matrix[0][i] = 0;
	}

	// O(n)
	for (int i = 0; i <= items.size() - 1; i++){
		matrix[i][0] = 0;
	}
	
	// O(n * capacity) since the outer loop is
	// n number of iterations and the inner loop
	// is capcaity number of iterations
	// O(capacity) + O(n) + O(n * capacity) = O(n * capacity)
	for (int i = 1; i < items.size(); i++){
		for (int j = 1; j < capacity; j++){
			if (matrix[i][j] > j){
				matrix[i][j] = matrix[i - 1][j];
			} else {
				matrix[i][j] = std::max(matrix[i - 1][j], matrix[i - 1][j - items[i - 1].weight] + items[i - 1].value);
			}
		}
	}
	
	// backtrack to collect indices
	// O(n) time. So overall complexity not affected
	// since O(n) + O(n * capacity) == O(n * capacity)
	int i = items.size();
	int j = capacity;
	while (i > 0 && j > 0){
		if (matrix[i][j] != matrix[i - 1][j]){
			solution.push_back(i);
			j -= items[i].weight;
		}
		i -= 1;
	}

	return solution;
}
