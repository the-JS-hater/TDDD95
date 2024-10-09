// https://en.wikipedia.org/wiki/Longest_increasing_subsequence

#include <vector>

std::vector<int> lis(std::vector<int> input){
	int pred_indices[input.size()];
	int end_indices[input.size() + 1];

	end_indices[0] = -1;

	int longest_seq_length = 0;

	for (int i = 0; i < input.size(); i++){
		int lo = 1;
		int hi = longest_seq_length + 1;

		while (lo < hi) {
			int mid = lo + int((hi - lo)/2);

			if (input[end_indices[mid]] >= input[i]){
				hi = mid;
			} else {
				lo = mid + 1;
			}
		}

		int newL = lo;
		pred_indices[i] = end_indices[newL - 1];
		end_indices[newL] = i;

		if (newL > longest_seq_length){
			longest_seq_length = newL;
		}
	}

	int solution[longest_seq_length];
	int temp_i = end_indices[longest_seq_length];

	for (int j = longest_seq_length - 1; j >= 0; j--) {
		solution[j] = input[temp_i];
		temp_i = pred_indices[temp_i];
	}
	int solution_size = sizeof(solution) / sizeof(solution[0]);

	std::vector<int> converted_solution(solution, solution + solution_size);
	return converted_solution;
}
