class Solution {
    public int solution(int n) {
    int a = 1;
    int b = 1;
    for (int i = 0; i < n - 1; i++) {
        int c = (a + b) % 1000000007;
            a = b;
            b = c;
        }
    return b;
    }
    // F(n-3) = F(n-2) + F(n-1)
}
