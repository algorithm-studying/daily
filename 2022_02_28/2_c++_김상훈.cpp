#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> sco, int K) {
    int answer = 0;
    
    priority_queue<int,vector<int>,greater<int>> pq;
    for(int i : sco){
        pq.push(i);
    }
    
    while(pq.top()<K){
        if(pq.size()<2)return -1;
        int a,b;
        a=pq.top();
        pq.pop();
        b=pq.top();
        pq.pop();
        pq.push(a+b*2);
        answer++;
    }
    
    return answer;
}