// https://en.wikipedia.org/wiki/Longest_increasing_subsequence

#include <vector>


std::vector<int> lis(std::vector<int> input){
	// Memory complexity is O(3N) since it needs two additional arrays
	int predIdx[input.size()];
	int minEndIdx[input.size() + 1];

	minEndIdx[0] = -1;
	int longestSeqLen = 0;
	
	// Iterate over the entire input O(n)
	for (int i = 0; i < input.size(); i++){
		int lowerBound = 1;
		int higherBound = longestSeqLen + 1;
		
		// Iterate over a subset of the input, which gets smaller
		// each iteration, hence O(n log n), when combined with
		// the outer for-loop
		while (lowerBound < higherBound) {
			int mid = lowerBound + int((higherBound- lowerBound)/2);

			if (input[minEndIdx[mid]] >= input[i]){
				higherBound = mid;
			} else {
				lowerBound = mid + 1;
			}
		}

		int newLen = lowerBound;
		predIdx[i] = minEndIdx[newLen - 1];
		minEndIdx[newLen] = i;

		if (newLen > longestSeqLen){
			longestSeqLen = newLen;
		}
	}

	int solution[longestSeqLen];
	int i = minEndIdx[longestSeqLen];
	
	// Linear time complexity relative to the longest
	// found increasing sequence. Not relevant for
	// overall time complexity
	for (int j = longestSeqLen - 1; j >= 0; j--) {
		solution[j] = input[i];
		i = predIdx[i];
	}

	// One would imagine converting between int[] and std::vec<int> would be simpler...
	int solutionSize = sizeof(solution) / sizeof(solution[0]);
	std::vector<int> convertedSolution(solution, solution + solutionSize);
	
	return convertedSolution;
}
