#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::pair;
using std::make_pair;
using std::abs;
using std::sqrt;
using std::setprecision;


struct Edge
{
	double w = INFINITY;
	double t = -1;
};
	
	
double calc_w(pair<double, double> a, pair<double, double> b)
{
	return sqrt(abs(a.first - b.first ) * abs(a.first - b.first) + (abs(a.second - b.second) * abs(a.second - b.second)));
}


vector<vector<double>> calc_adj(vector<pair<double, double>> vertices)
{
	vector<vector<double>> adj(vertices.size());
	for (unsigned i = 0; i < vertices.size(); ++i)
	{	
		vector<double> row(vertices.size());
		for (unsigned j = 0; j < vertices.size(); ++j)
		{
			row[j] = calc_w(vertices[i], vertices[j]);
		}
		adj[i] = row;
	}
	return adj;
}


double prims(vector<pair<double, double>> vertices)
{	
	vector<vector<double>> adj = calc_adj(vertices);

	vector<bool> selected(vertices.size(), false);
	vector<Edge> min_e(vertices.size());
	double total = 0.0f;
	min_e[0].w = 0.0f;
	
	for (unsigned i = 0; i < vertices.size(); ++i)
	{
		unsigned best_idx = -1;
		for (unsigned j = 0; j < vertices.size(); ++j)
		{
			if (not selected[j] and ((best_idx  == -1) or (min_e[j].w < min_e[best_idx].w))) best_idx = j;
		}

		selected[best_idx] = true;
		total += min_e[best_idx].w;

		for (unsigned k = 0; k < vertices.size(); ++k)
		{
			if (adj[best_idx][k] < min_e[k].w) min_e[k] = {adj[best_idx][k], best_idx};
		}
	}

	return total;
}


int main()
{
	unsigned n;
	cin >> n;
	unsigned m;
	for (unsigned i = 0; i < n; ++i)
	{
		cin >> m;
		double a,b;
		vector<pair<double, double>> vec;
		
		for (unsigned j = 0; j < m; ++j)
		{	
			cin >> a >> b;
			vec.push_back(make_pair(a,b));
		}
		
		cout << setprecision(14) << prims(vec) << endl;
	}
}
