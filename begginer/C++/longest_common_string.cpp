#include<iostream>
#include<algorithm>
#include<string>
#define MAX 1005
using namespace std;
int count(int n,int m,string A,string B){
    int dp[MAX][MAX];
    for(int i=0;i<=n;i++){
        for(int j=0;j<=m;j++){
            dp[i][j] = 0;
        }
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(A[i-1] == B[j-1]){
                dp[i][j] = dp[i-1][j-1] + 1;
            }else{
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }
    return dp[n][m];
}
int main(void){
    int n,m;
    string A,B;
    cin >> n >> m >> A >> B;
    cout << count(n,m,A,B) << endl;
    return 0;
} 