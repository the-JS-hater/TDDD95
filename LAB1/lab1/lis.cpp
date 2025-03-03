/* Morno368 - Morgan Nordberg
 * TODO
 * - Time & Memory complexity
 * - Description of problem
 * - How it works
 * */



#include <vector>
#include <iostream>
#include <cmath>


using std::vector;
using std::cin;
using std::cout;
using std::endl;

const int INF = 1e9;

vector<int> lis(vector<int> v){
	unsigned n = v.size();
	vector<int> l(n + 1, INF); 
	l[0] = -INF;
	vector<int> p(n, -1);

	for (unsigned i {0}; i < n; i++)
	{
		for (unsigned j {1}; j <= n; j++)
		{
			if (l[j - 1] < v[i] && v[i] < l[j]) {
				l[j] = v[i];
				p[i] = j;
			}
		}
	}

	int a = l[0];
	int pos = 0;
	for (unsigned i {1}; i < n; i++)
	{
		if (l[i] > a){
			a = l[i];
			pos = i;
		}
	}

	vector<int> idx_l;
	while (pos != -1)
	{
		idx_l.push_back(pos);
    pos = p[pos];
	}
	
	return idx_l;
}


int main() {
	int n;
	while(cin >> n) 
	{
		vector<int> seq;
		for (unsigned i {0}; i < n; i++)
		{
			cin >> n;
			seq.push_back(n);
		}
		vector<int> res = lis(seq);
		cout << res.size() << endl;
		for (int e: res) cout << e << " ";
		cout << endl;
	}
}

