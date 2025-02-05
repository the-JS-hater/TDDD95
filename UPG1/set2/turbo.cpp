#include <iostream>
#include <vector>
#include <ios>
#include <algorithm>
#include <map>


using std::cin;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;
using std::ios;
using std::find;
using std::distance;
using std::map;


struct Fenwick {
	vector<long long> v;
	long long int n;
	
	Fenwick(long long int n) : v{vector<long long>(n + 1, 0LL)}, n{n + 1} {}
	
	void add(long long int const i, long long int const x)
	{
		for (long long int j {i + 1}; j < n; j = j | (j + 1LL)) v[j] += x;
	}
	
	long long sum(long long int const i)
	{
		long long sum = 0LL;
		for (long long j {i}; j > 0LL; j = (j & (j + 1LL)) -1LL) sum += v[j];
		return sum;
	}
};


void solve(Fenwick& fw, vector<int> const& v)
{
	//TODO:
}


int main()
{
  ios::ios_base::sync_with_stdio(false); 
  cin.tie(nullptr);
  cout.tie(nullptr);

	int n;
	cin >> n;
	Fenwick fw = Fenwick(n);
	vector<int> v;
	vector<int> idxs;
	int n2;
	for (int i {n}; i < n; i++)
	{
		cin >> n2;
		v.push_back(n2);
	}

	solve(fw, v);
}
