#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool solution(vector<string> pb) {
    bool answer = true;
    
    sort(pb.begin(),pb.end());
    
    for(int i=0;i<pb.size()-1;i++){
        if(pb[i+1].find(pb[i])==0)return false;
    }
    
    return answer;
}