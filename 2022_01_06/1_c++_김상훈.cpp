#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> nums) {
	int answer = 0;

	vector<bool> prime(3005, true);
	for (int i = 2; i < prime.size(); i++) {
		if (prime[i]) {
			for (int j = i * 2; j < prime.size(); j += i) {
				prime[j] = false;
			}
		}
	}

	int tmp;

	for (int i = 0; i < nums.size() - 2; i++) {
		for (int j = i + 1; j < nums.size() - 1; j++) {
			for (int k = j + 1; k < nums.size(); k++) {
				tmp = nums[i] + nums[j] + nums[k];
				if (prime[tmp])answer++;
			}
		}
	}

	return answer;
}