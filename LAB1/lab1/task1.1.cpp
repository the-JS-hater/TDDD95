#include <iostream>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;


struct Interval {
	double start;
	double end;
	int index;

	Interval(double start, double end, int index) : start{start}, end{end}, index{index} {}
};


bool cmp_intervals(const Interval& a, const Interval& b) {
	if (a.start == b.start) {
		return a.end < b.end;
	}
	return a.start < b.start;
} 


std::vector<int> cover(Interval interval, std::vector<Interval> intervals) {
	std::vector<int> indices = {};
	
	std::sort(intervals.begin(), intervals.end(), cmp_intervals);
	
	double current_right = interval.start;
	double target_right = interval.end;
	
	int i = 0;
	do {
		double farthest_right = current_right; 
    int bestIndex = -1;
		
		while (i < intervals.size() && intervals[i].start <= current_right) {
			if (intervals[i].end >= farthest_right) {
				farthest_right = intervals[i].end;
				bestIndex = intervals[i].index;
			}
			i++;
		}
		
		if (bestIndex == -1) {
			return {};  
		}
		
		indices.push_back(bestIndex);
		current_right = farthest_right;
	} while (current_right < target_right);

	return indices;
};


int main() {
	double a,b;
	int n;

	while (cin >> a >> b)
	{	
		Interval target = Interval(a, b, 666); //idx irrelevant
		cin >> n;

		std::vector<Interval> intervals;
		for(int i=0; i < n; i++)
		{	
			cin >> a >> b;
			Interval tmp_interval = Interval(a, b, i);
			intervals.push_back(tmp_interval);
		}

		std::vector<int> res = cover(target, intervals);
		if (res.size() == 0) cout << "impossible" << endl;
		else cout << res.size() << endl; 

		for (int idx: res)
		{
			cout << idx << " ";
		}
		cout << endl;
	}
}


