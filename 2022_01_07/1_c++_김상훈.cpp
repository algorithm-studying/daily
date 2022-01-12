#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool comp(pair<double, int> a, pair<double, int> b) {
	if (a.first == b.first)return a.second < b.second;
	return a.first > b.first;
}

vector<int> solution(int N, vector<int> stages) {
	vector<int> answer;

	vector<int> tmp(N + 2);
	for (int i : stages) {
		tmp[i]++;
	}

	int x = stages.size();

	vector<pair<double, int>> tmp1;
	for (int i = 1; i < N + 1; i++) {
		if (x != 0 && tmp[i] != 0) {
			tmp1.push_back({ (double)tmp[i] / x,i });
		}
		else tmp1.push_back({ 0,i });

		x -= tmp[i];
	}



	sort(tmp1.begin(), tmp1.end(), comp);

	for (int i = 0; i < N; i++) {
		answer.push_back(tmp1[i].second);
	}

	return answer;
}