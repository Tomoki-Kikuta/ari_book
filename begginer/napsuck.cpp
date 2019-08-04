#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int napsuck(int n,int W,vector<int> weight,vector<int> value){
    int cost[n+1][W+1];
    for(int i=0;i<=n;i++){
        for(int j=0;j<=W;j++){
            cost[i][j] = 0;
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<=W;j++){
            cost[i+1][j] = max(cost[i+1][j],cost[i][j]);
            if(weight[i] + j <= W){
                cost[i+1][j+weight[i]] = max(cost[i][j+weight[i]] + value[i],cost[i][j]);
            }
        }
    }
    return cost[n][W];
}
int main(void){
    int n,W;
    vector<int> weight;
    vector<int> value;
    cin >> n;
    for(int i=0;i<n;i++){
        int w,v;
        cin >> w >> v;
        weight.push_back(w);
        value.push_back(v);
    }
    cin >> W;
    cout << napsuck(n,W,weight,value) << endl;
    return 0;
}