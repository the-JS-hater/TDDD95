#include <iostream>
#include <vector>
#include <ios>


using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::ios;


int sum(long long i, vector<long long> const& v)
{	
	long long sum = 0LL;
	for (; i >= 0LL; i = (i & (i + 1LL)) -1LL) sum += v[i];
  return sum;
}


void add(long long i, long long const x, vector<long long>& v)
{
  for (; i < (long long)v.size(); i = i | (i + 1LL)) v[i] += x;
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
        cout << sum(op1 - 1, v) << "\n";
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
