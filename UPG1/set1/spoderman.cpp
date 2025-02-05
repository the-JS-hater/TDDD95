#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>


using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::accumulate;
using std::max;


string workout(vector<int> const& v) {
	int m[41][1001];
	int m2[41][1001];

	for (unsigned y {0}; y < 41; y++) {
		for (unsigned x {0}; x < 1001; x++) {
			m[y][x] = 1002;
			m2[y][x] = 0;
		}
	}

	m[0][0] = 0;
	m2[1][v[0]] = 1;

	for (unsigned r {1}; r <= v.size(); r++) {
		for (unsigned c {0}; c <= 1000; c++)
		{	
			if (m[r-1][c] == 1002) continue;
	
			int const dist = v[r-1];
			int const current_max = m[r-1][c];
			int const d = c - dist;
			int const u = c + dist;
		
			if (d >= 0 && current_max < m[r][d]) {
				m[r][d] = current_max;
				m2[r][d] = -1;
			} 
			
			m[r][u] = max(current_max, u);  
			m2[r][u] = 1;  
		}
	}
	
	if (m[v.size()][0] == 1002) return "IMPOSSIBLE";

	unsigned r = v.size();
	unsigned c = 0;
	string path = "";
	
	while (r > 0)
	{	
		if (m2[r][c] == 0) {
			break;
		}
		if (m2[r][c] == 1) {
			c -= v[r - 1]; 
			r--; 
			path.insert(0, "U"); 
		} 
		if (m2[r][c] == -1) {
			c += v[r - 1]; 
			r--; 
			path.insert(0, "D"); 
		} 
	}
	return path;
}


int main() {
	int N, M;
	cin >> N;

	for (unsigned i {0}; i < N; i++)
	{	
		int n;
		cin >> M;
		vector<int> v;
		for (unsigned j {0}; j < M; j++)
		{
			cin >> n;
			v.push_back(n);
		}
		if (accumulate(v.begin(), v.end(), 0) % 2 != 0) {
			cout << "IMPOSSIBLE" << endl;
		}	else {
			string res = workout(v);
			cout << res << endl;
		}
	}
}
