#include <string>
#include <vector>

using namespace std;

string solution(string phone) {
    for (int i = 0; i < phone.size() - 4; i++) {
        phone[i] = '*';
    }

    return phone;
}