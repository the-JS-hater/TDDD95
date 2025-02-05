#include <iostream>
#include <vector>
#include <ios>


using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::ios;


struct Fenwick {
	vector<long long> v;
	long long int n;
	
	Fenwick(long long int n) : v{vector<long long>(n, 0LL)}, n{n} {}

	void add(long long int const i, long long int const x)
	{
		for (long long int j {i}; j < n; j = j | (j + 1LL)) v[j] += x;
	}

	long long sum(long long int const i)
	{
		long long sum = 0LL;
		for (long long j {i}; j >= 0LL; j = (j & (j + 1LL)) -1LL) sum += v[j];
		return sum;
	}

	void print() {for(auto e: v) cout << e << " "; cout << endl;}
	
	void printLen() {cout << "length: "<< n << endl;}
};


int main()
{
  ios::ios_base::sync_with_stdio(false); 
  cin.tie(nullptr);
  cout.tie(nullptr);
    
  long long n, q;
  cin >> n >> q;
	Fenwick fw = Fenwick(n);
  
  char oper;
  long long op1, op2;

  for (long long i {0LL}; i < q; i++)
  {	
    cin >> oper;
    switch(oper) {
      case '?': {
				cin >> op1;
        cout << fw.sum(op1 - 1) << "\n";
        break;
      };
      case '+': {
        cin >> op1 >> op2;
        fw.add(op1, op2);
        break;
      }
    }
  }

  return 0;
}
