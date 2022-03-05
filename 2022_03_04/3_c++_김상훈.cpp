#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    
    vector<long long> fib(n);
    
    fib[0]=1; fib[1]=2;
    
    for(int i=2;i<n;i++){
        fib[i]=(fib[i-1]+fib[i-2])%1000000007;
    }
    
    
    
    return fib[n-1];
}