#include <iostream>
#include <vector>
#include <ios>


using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::ios;


int sum(long long const i, vector<long long> const& v)
{
  long long sum = 0LL;
  for (long long j {i-1LL}; j >= 0LL; j = (j & (j + 1LL)) - 1LL) sum += v[j];
  return sum;
}


void add(long long const i, long long const x, vector<long long>& v)
{
  for (long long j {i}; j < (long long)v.size(); j = j | (j + 1LL)) v[j] += x;
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
