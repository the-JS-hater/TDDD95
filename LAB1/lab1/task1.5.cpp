#include <iostream>
#include <vector>
#include <ios>


using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::ios;


long long sum(long long i, vector<long long> const& v)
{
	long long sum = 0LL;
	// j & (j + 1) - 1 does bit magic to find the next valid index each index in
	// the array stores the sum of a specific range of indices. So here we move
	// backwards, summing the various subranges until we reack index 0
	for (long long j {i}; j >= 0LL; j = (j & (j + 1LL)) - 1LL) sum += v[j];
	return sum;
}


void add(long long int i, long long int x, vector<long long int>& v)
{
	// starting at the index i, we use bit magic once again (i | (i + 1)) to find
	// the index of the next subrange that needs updating since it depends on sum i,
	// and an increase in the sum of the subrange represented at index i
	// contributes to the subranges that follow. So we continue moving forward
	// until the end of the array
	for (long long int j {i}; j < (long long)v.size(); j = j | (j + 1LL)) v[j] += x;
}


int main()
{
	ios::ios_base::sync_with_stdio(false); 
  cin.tie(nullptr);
  cout.tie(nullptr);
	
	long long n, q;
	cin >> n >> q;
	std::vector<long long> v(n, 0LL);
	
	char oper;
	long long op1, op2;

	for (long long i {0LL}; i < q; i++)
	{
		cin >> oper;
		switch(oper) {
			case '?': {
				cin >> op1;
				cout << sum(op1, v) << "\n";
				break;
			};
			case '+': {
				cin >> op1 >> op2;
				add(op1, op2, v);
				break;
			}
		}
	}

	return 0;
}
