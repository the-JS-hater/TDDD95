#include <iostream>
#include <vector>
#include <ios>


using std::cin;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;
using std::ios;


struct Fenwick {
	vector<long long> v;
	long long int n;
	
	Fenwick(long long int n) : v{vector<long long>(n + 1, 0LL)}, n{n + 1} {}
	
	// To increase the value at a given idx, we also need to jump forward and
	// increase the values of the indices representing the sums of subranges that
	// depend on the value at i. So we need to continually jump forward in the
	// underlying array until we get an invalid index that's outside of the
	// bounds of the array. The "jumps" are achieved by bit magic
	void add(long long int const i, long long int const x)
	{
		for (long long int j {i + 1}; j < n; j = j | (j + 1LL)) v[j] += x;
	}
	
	// Various Indexes in the underlying array represent the sum of specific
	// subranges. So to compute the prefix some of some index i, we start at that
	// idx and then by means of bit magic jump "backwards" through the array to
	// sum all the previous subranges that the one at i depend on
	long long sum(long long int const i)
	{
		long long sum = 0LL;
		for (long long j {i}; j > 0LL; j = (j & (j + 1LL)) -1LL) sum += v[j];
		return sum;
	}
	
	// I used these for debug purposes
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
				cout << fw.sum(op1) << "\n";
        break;
      };
      case '+': {
        cin >> op1 >> op2;
        fw.add(op1, op2);
        break;
      }
    }
  }
	fw.print();
  return 0;
}
