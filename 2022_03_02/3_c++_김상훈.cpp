#include <string>
#include <vector>
#include <map>
using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;

    map<int, int, greater<int>> m;
    for (int i : works) {
        if (m.find(i) == m.end())m[i] = 1;
        else m[i]++;
    }

    map<int, int>::iterator iter = m.begin();

    while (n > 0 && iter->first > 0) {
        if (iter->second > n) {
            if (m.find(iter->first - 1) == m.end()) {
                m[iter->first - 1] = n;
                iter->second -= n;
                n = 0;
            }
            else {
                m[iter->first - 1] += n;
                iter->second -= n;
                n = 0;
            }
        }
        else {
            if (m.find(iter->first - 1) == m.end()) {
                m[iter->first - 1] = iter->second;
                n -= iter->second;
                iter++;
            }
            else {
                m[iter->first - 1] += iter->second;
                n -= iter->second;
                iter++;
            }
        }
    }

    for (; iter != m.end(); iter++) {
        answer += iter->first * iter->first * iter->second;
    }

    return answer;
}