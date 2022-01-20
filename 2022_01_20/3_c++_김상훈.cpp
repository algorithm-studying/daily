#include <string>
#include <vector>

using namespace std;

vector<vector<int>> map;
vector<bool> check;

void dfs(int a){
    if(!check[a])return;
    
    check[a]=false;
    
    for(int i=0;i<map.size();i++){
        if(i==a)continue;
        
        if(map[a][i]==1)dfs(i);
    }
}

int solution(int n, vector<vector<int>> com) {
    int answer = 0;
    
    
    map=com;
    vector<bool> c(n,true);
    check=c;
    
    for(int i=0;i<n;i++){
        if(check[i]){
            answer++;
            dfs(i);
        }
    }
    
    return answer;
}