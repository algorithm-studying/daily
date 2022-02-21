#include <string>
#include <vector>

using namespace std;

int solution(string s) {

    string num[10] = { "zero","one","two","three","four","five","six","seven","eight","nine" };

    for (int i = 0; i < 10; i++) {
        while (s.find(num[i]) != string::npos) {
            s.replace(s.find(num[i]), num[i].size(), to_string(i));
        }
    }

    return stoi(s);
}