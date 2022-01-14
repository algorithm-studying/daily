#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    for (int i = 0; i < new_id.size(); i++) {
        if (new_id[i] >= 'A' && new_id[i] <= 'Z')new_id[i] += 'a' - 'A';
    }

    string id = "";
    for (int i = 0; i < new_id.size(); i++) {
        if ((new_id[i] <= 'z' && new_id[i] >= 'a') || (new_id[i] <= '9' && new_id[i] >= '0') || new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.')id += new_id[i];
    }

    for (int i = 1; i < id.size(); i++) {
        if (id[i - 1] == '.' && id[i] == '.') {
            id.erase(i, 1);
            i--;
        }
    }

    while (!id.empty() && id[0] == '.') {
        id.erase(0, 1);
    }
    while (!id.empty() && id.back() == '.') {
        id.pop_back();
    }

    if (id.empty())id = "a";

    while (id.size() >= 16)id.pop_back();

    while (id.back() == '.')id.pop_back();

    while (id.size() < 3) {
        id.append(1, (char)id.back());
    }

    return id;
}