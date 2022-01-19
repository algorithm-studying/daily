#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s) {
    string answer = "";
    
    while(!s.empty()){
        string tmp=s.substr(0,s.find(' ')!= string::npos ? s.find(' ') : string::npos);
        if(s.find(' ')!=string::npos){    
            s=s.substr(s.find(' '));
        }
        else s.clear();
            
            
        for(int i = 0;i<tmp.size();i++){
            if(i%2==0){
                if(tmp[i]<='z' && tmp[i]>='a')tmp[i]+='A'-'a';
            }
            else{
                if(tmp[i]<='Z' && tmp[i]>='A')tmp[i]+='a'-'A';
            }
        }
        answer += tmp;
        
        while(!s.empty() && s[0]==' '){
            answer+=" ";
            s.erase(0,1);
        }
    }
    
    return answer;
}