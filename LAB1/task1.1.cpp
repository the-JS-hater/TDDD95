// https://en.wikipedia.org/wiki/Interval_scheduling

#include <vector>
#include <algorithm>

struct Interval {
	double start;
	double end;
	int index; //might have to change depending on input
};


// Custom comparison function to be used to sort intervals by
// starting points
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
