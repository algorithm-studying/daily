#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
	vector<int> answer;

	int pic = 0;
	int zero = 0;

	set<int> s;
	for (int i : win_nums) {
		s.insert(i);
	}

	for (int i : lottos) {
		if (i == 0)zero++;
		if (s.find(i) != s.end())pic++;
	}

	if (pic + zero > 1)answer.push_back(7 - pic - zero);
	else answer.push_back(6);

	if (pic > 1)answer.push_back(7 - pic);
	else answer.push_back(6);

	return answer;
}