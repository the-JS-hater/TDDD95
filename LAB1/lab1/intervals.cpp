#include <iostream>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;


/*
 * Morgan Nordberg (morno368)
 * Interval scheduling is about taking a revieving a target interval to be
 * covered, and a set of available intervals, and returning the indices of the
 * minimal set of intervals to cover the target.
 *
 * I have a struct for representing intervals, and a custom comparison function
 * to use for std::sort. The overall algorithm is to sort the set of intervals
 * by start time, and if equal, by end time. This makes it easier to then
 * select intervals that start at or before our current leftmost target point
 * (initially the start of the target interval) but with the latest possible
 * end time to cover as much as possible. Since the list is ordered we never
 * need to reevaluate intervals at lower indices than the one selecten, hence
 * we never reevaluate the same intervals at the start. 
 *
 * Time complexity is O(n log n) for sorting, and then O(n) for selecting the
 * intervals 
 * */


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
	
	//cpprefrence guarantees std::sort to be worst-case O(n log n) 
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


