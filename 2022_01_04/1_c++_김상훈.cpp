#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> sizes) {
	int a = 0; int b = 0;

	for (int i = 0; i < sizes.size(); i++) {
		if (sizes[i][0] < sizes[i][1])swap(sizes[i][0], sizes[i][1]);

		if (sizes[i][0] > a)a = sizes[i][0];
		if (sizes[i][1] > b)b = sizes[i][1];
	}

	return a * b;
}