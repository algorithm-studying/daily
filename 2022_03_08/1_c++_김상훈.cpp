#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    int p=0; int y=0;

    for(int i=0;i<s.size();i++){
        if(s[i]=='p' || s[i]=='P')p++;
        if(s[i]=='y' || s[i]=='Y')y++;
    }

    if(p==y)return true;
    else return false;
}