#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";

    int n = s.size();

    if (n % 2 == 1) {
        answer += s[n / 2];
        return answer;
    }
    else {
        answer += s[n / 2 - 1];
        answer += s[n / 2];
        return answer;
    }
}