#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int napsuck(int n,int W,vector<int> weight,vector<int> value){
    int cost[weight.size()+1][W+1];
    for(int i=0;i<=weight.size();i++){
        for(int j=0;j<=W;j++){
            cost[i][j] = 0;
        }
    }
    for(int i=1;i<=weight.size();i++){
        for(int j=1;j<=W;j++){
            if(weight[i-1]<=j){
                cost[i][j] = max(cost[i][j - weight[i-1]] + value[i-1],cost[i-1][j]);
            }else{
                cost[i][j] = cost[i-1][j];
            }
        }
    }
    return cost[weight.size()][W];
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