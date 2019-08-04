#include<iostream>
#include<algorithm>
#define MAX_N 1001
#define MAX_M 100001
using namespace std;

int main(void){
    int n,m,M,dp[MAX_M][MAX_N];
    cin >> n >> m >> M;
    dp[0][0] = 1;
    for(int i=1;i<=m;i++){
        for(int j=0;j<=n;j++){
            if(j - i >= 0){
                dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % M;
            }else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    cout << dp[m][n] << endl;
    return 0;
} 