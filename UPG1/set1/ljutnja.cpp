#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <numeric>
#include <iterator>


using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::sort;
using std::equal_range;
using std::transform;
using std::accumulate;
using std::distance;


unsigned long long ljutnja(vector<long long> v, long long m) {
	auto cmp = [](long long a, long long b){return a > b;};
	auto decrement = [](long long a){return a - 1;};
	auto square = [](long long a){return a * a;};
	
	sort(v.begin(), v.end(), cmp);

	while (m != 0)
	{		
		long long t = v.at(0);
		auto [s,e] = equal_range(v.begin(), v.end(), t, std::greater{});
	
		if (e == v.end()) {
			if (m > distance(s, e)) {
				long long diff = m / distance(s, e); 
				long long rest = m % distance(s, e);
				auto feed = [&diff](long long a){return a - diff;};

				transform(v.begin(), v.end(), v.begin(), feed);
				transform(v.begin(), v.begin() + rest, v.begin(), decrement);
			} else {
				transform(v.begin(), v.begin() + m, v.begin(), decrement);
			}
			break;
		}	else {
			long long b = *e;
			long long diff = t - b;
			long long cost = distance(s, e) * diff;
			
			if (cost > m) {
				long long diff = m / distance(s, e); 
				long long rest = m % distance(s, e);
				auto feed = [&diff](long long a){return a - diff;};
				
				transform(s, e, s, feed);
				transform(v.begin(), v.begin() + rest, v.begin(), decrement);
				break;
			} else {
				auto feed = [&diff](long long a){return a - diff;};
				transform(s, e, s, feed);
				m -= distance(s, e) * diff;
			}
		}
	}
	
	transform(v.begin(), v.end(), v.begin(), square);
	return accumulate(v.begin(), v.end(), 0LLU);
}


int main() {
	long long M, N, n;
	cin >> M >> N;
	vector<long long> v;
	for (long long i = 0; i < N; i++)
	{
		cin >> n;
		v.push_back(n);
	}

	unsigned long long res = ljutnja(v, M);
	cout << res << endl;
}
