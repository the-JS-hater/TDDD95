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


// Custom comparison function to be used to sort intervals by starting points
bool cmp_intervals(const Interval& a, const Interval& b) {
	if (a.start == b.start) {
		return a.end < b.end;
	}

	return a.start < b.start;
} 


std::vector<int> cover(Interval interval, std::vector<Interval> intervals) {
	std::vector<int> indices = {};

	//Sort the intervals by their starting points.
	//O(n log n) according to cpprefrence website
	std::sort(intervals.begin(), intervals.end(), cmp_intervals);
	
	//until we've covered the entire goal interval the list of intervals we need to
	//iterate over in the inner loop gets smaller for each iteration of the outer loop. 
	//hence the following section(the nested while loops) should be	O(n log n)
	
	//Initialize current_right to the left boundary of the target interval.
	double current_right = interval.start;
	double target_right = interval.end;
	int i = 0;
	
	//While the target interval is not fully covered:
	while (current_right < target_right) {
    double farthest_right = current_right;
    int bestIndex = -1;
       
		//Select the interval with the farthest end point that starts at or before `current_right`
		//Move current_right to the right end of the chosen interval.
		while (i < intervals.size() && intervals[i].start <= current_right) {
			if (intervals[i].end > farthest_right) {
				farthest_right = intervals[i].end;
				bestIndex = intervals[i].index;
			}
			i++;
		}
		
		// No solution, target interval can't be covered
		if (bestIndex == -1) {
			return {};  
		}

		// Add the best found intervals index 
		indices.push_back(bestIndex);
		current_right = farthest_right;
	}
	return indices;
};


int main() {

	while (cin.peek() != EOF)
	{	
		double a,b;
		int n;
		cin >> a;
		cin >> b;
		Interval target = Interval(a, b, 666); //idx irrelevant
		cin >> n;

		std::vector<Interval> intervals;
		for(int i=0; i <= n; i++)
		{	
			cin >> a;
			cin >> b;
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
	}
}


