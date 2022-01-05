#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {

	vector<vector<long long>> map(m + 1, vector<long long>(n + 1));
	vector<vector<bool>> check(m + 1, vector<bool>(n + 1, true));

	for (int i = 0; i < puddles.size(); i++) {
		check[puddles[i][0]][puddles[i][1]] = false;
	}

	map[1][1] = 1;

	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= n; j++) {
			if (check[i - 1][j])map[i][j] += map[i - 1][j];
			if (check[i][j - 1])map[i][j] += map[i][j - 1];

			map[i][j] %= 1000000007;
		}
	}



	return map[m][n];
}