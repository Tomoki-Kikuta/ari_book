#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
static const int N = 101;
int dp[N][N]={0};
int main(void){
    int n,w,v,W;
    vector<int> weight;
    vector<int> value;
    long int score = 0;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> w >> v;
        weight.push_back(w);
        value.push_back(v);
    }
    cin >> W;
    for(int i=0;i<n;i++){
        for(int j=0;j<=W;j++){
            for(int k=0;k*weight[i]<=j;k++){
                dp[i+1][j] = max(dp[i+1][j],dp[i][j-k*weight[i]]+k*value[i]);
            }
        }
    }
    cout << dp[n][W] << endl;
    return 0;
}