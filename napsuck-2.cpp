#include<iostream>
#include<algorithm>
#include<vector>
#define MAX_N 101
#define MAX_V 101
#define INF 1<<21
using namespace std;

int cal_value(int n,vector<long int> weight,vector<long int> value,long int W){
    long int dp[n+1][MAX_N * MAX_V];
    int res = 0;
    dp[0][0] = 0;
    for(int i=1;i<MAX_N * MAX_V;i++){
        dp[0][i] = INF;
    }
    for(int i=1;i<=n;i++){
        for(int j=0;j<MAX_N * MAX_V;j++){
            if(value[i-1]>j){
                dp[i][j] = dp[i-1][j];
            }else{
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-value[i-1]] + weight[i-1]);
            }
        }
    }
    for(int i=0;i<MAX_N * MAX_V;i++){
        if(dp[n][i]<=W){
            res = max(res,i);
        }
    }
    return res;
}

int main(void){
    int n;
    long int W;
    vector<long int> weight;
    vector<long int> value;
    cin >> n;
    for(int i=0;i<n;i++){
        long int w,v;
        cin >> w >> v;
        weight.push_back(w);
        value.push_back(v);
    }
    cin >> W;
    cout << cal_value(n,weight,value,W) << endl;
    return 0;
}