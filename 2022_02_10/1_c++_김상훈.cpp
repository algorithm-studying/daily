#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> arr, int d) {
    vector<int> answer;

    sort(arr.begin(), arr.end());

    for (int i : arr) {
        if (i % d == 0)answer.push_back(i);
    }


    if (answer.empty())answer.push_back(-1);
    return answer;
}