#include <iostream>

using std::cin;
using std::cout;
using std::endl;

void solve(long long const n, long long const m)
{
	long long p = 1;
	for (long long i = 2; i <= n and p != 0 and m != 0; ++i)
	{
		p = (p * i) % m;
	}
	if (p <= 0) cout << m << " divides " << n << "!\n";
	else cout << m << " does not divide " << n << "!\n";
}

int main()
{
	long long n,m;
	while (cin >> n >> m)
	{
		solve(n,m);
	}
	cout << endl;
}
