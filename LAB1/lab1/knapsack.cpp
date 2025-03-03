/* Morno368 - Morgan Nordberg
 * 
 * Memory complexity is O(N * M), where n is the the capacity and m is the
 * number of items. Since we always construct a M*N matrix
 *
 * Time complexity is also O(N * M), since we will have to fill out the matrix
 * values. Afterwards, backtracking through it to provide the actual indexes is
 * trivial in complexity
 *
 * The algorithm works by creating a matrix with the capacity on one axis, and
 * the other axis will repsent items chosen. We then for each capacity, up to
 * the given maximum capacity, fill the rows with the optimal choice of items.
 *
 * - Description of problem
 * We wanna pick the indexes of items, with given weights, such that we
 * maximize the sum of the items given values, given a limited capacity of
 * total weight we can accumulate
 * */



#include <vector>
#include <algorithm>
#include <iostream>


using std::cin;
using std::endl;
using std::cout;
using std::vector;
using std::reverse;
using std::max;


struct Item {
	int value;
	int weight;

	Item(int v, int w) : value{v}, weight{w} {}
};


vector<int> knapsack(int capacity, vector<Item> items) {
	int m[items.size() + 1][capacity + 1];
	
	for (int j = 0; j <= capacity; j++) m[0][j] = 0;
	for (int i = 0; i <= items.size(); i++) m[i][0] = 0;

	for (int i = 1; i <= items.size(); i++)
	{
		for (int j = 1; j <= capacity; j++)
		{
			if (items[i-1].weight > j) m[i][j] = m[i-1][j];
			else m[i][j] = max(
					m[i-1][j],
					m[i-1][j-items[i-1].weight] + items[i-1].value
			);  
		}
	}

	int i = items.size();
	int j = capacity;
	vector<int> idx_vec;
	while (i > 0 && j > 0)
	{
		if (m[i][j] > m[i-1][j])
		{
			idx_vec.push_back(i - 1);
			j -= items[i-1].weight;
		}
		i--;
	}
	return idx_vec;
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
		reverse(vec.begin(), vec.end());
		cout << vec.size() << endl;
		for (int idx: vec) cout << idx << " ";
		cout << endl;
	}
}
