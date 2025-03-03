/* Morno368 - Morgan Nordberg
 * TODO
 * - Time & Memory complexity
 * - Description of problem
 * - How it works
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
