#include <vector>
#include <algorithm>
#include <iostream>


using std::cin;
using std::endl;
using std::cout;
using std::vector;


struct Item {
	int value;
	int weight;

	Item(int v, int w) : value{v}, weight{w} {}
};


vector<int> knapsack(int capacity, vector<Item> items) {
	// Input:
	// Values (stored in array v)
	// Weights (stored in array w)
	// Number of distinct items (n)
	// Knapsack capacity (W)
	// NOTE: The array "v" and array "w" are assumed to store all relevant values starting at index 1.


	vector<int> solution = {};

	//array m[0..n, 0..W];
	int matrix[items.size() + 1][items.size() + 1];
	//for j from 0 to W do:
	//    m[0, j] := 0
	for (int i = 0; i <= capacity; i++){
		matrix[0][i] = 0;
	}

	//for i from 1 to n do:
	//    m[i, 0] := 0
	for (int i = 1; i <= items.size(); i++){
		matrix[i][0] = 0;
	}
	
	//for i from 1 to n do:
	//    for j from 1 to W do:
	//        if w[i] > j then:
	//            m[i, j] := m[i-1, j]
	//        else:
	//            m[i, j] := max(m[i-1, j], m[i-1, j-w[i]] + v[i])
	for (int i = 1; i < items.size(); i++){
		for (int j = 1; j < capacity; j++){
			if (matrix[i][j] > j){
				matrix[i][j] = matrix[i - 1][j];
			} else {
				matrix[i][j] = std::max(matrix[i - 1][j], matrix[i - 1][j - items[i - 1].weight] + items[i - 1].value);
			}
		}
	}
	
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


int main() {
	int c, n;
	while(cin >> c >> n) 
	{
		int v, w;
		vector<Item> items;
		for (int i=0; i<n; i++)
		{
			cin >> v >> w;
			items.push_back(Item(v, w));
		}
		vector<int> vec = knapsack(c, items);
		cout << vec.size() << endl;
		for (int idx: vec)
		{
			cout << idx << " ";
		}
		cout << endl;
	}
}
