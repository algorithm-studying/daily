#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int i = 1;

    for (; i < n; i++) {
        if (n % i == 1)break;
    }

    return i;
}