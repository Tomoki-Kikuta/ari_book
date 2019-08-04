#include<iostream>
#include<algorithm>
#include<vector>
#define MAX_N 101
#define MAX_NUMBER 100001
#define INF 1<<21
using namespace std;

void input(int n,vector<int> &number){
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        number.push_back(a);
    }
}

bool cal_number(int n,vector<int> &sum,vector<int> &number,int K){
    bool flag;
    pair<int,int> dp[MAX_NUMBER];
    dp[0] = make_pair(0,0);
    for(int j=1;j<=K;j++){
        dp[j] = make_pair(0,INF);
    }
    for(int i=1;i<=n;i++){
        for(int j=0;j<=K;j++){
            dp[j].first = 0;
        }
        for(int j=0;j<=K;j++){
            if(j>=number[i-1] && dp[j-number[i-1]].second!=INF){
                dp[j].first = dp[j-number[i-1]].first + 1;
                dp[j].second = min(dp[j].second,dp[j-number[i-1]].second + 1);
            }
            if(dp[j].first==sum[i-1]){
                break;
            }
        }
    }
    if(dp[K].second!=INF){
        flag = true;
    }else{
        flag = false;
    }
    return flag;
}
int main(void){
    int n,K;
    vector<int> number;
    vector<int> &rnumber = number;
    vector<int> sum;
    vector<int> &rsum = sum;
    cin >> n;
    input(n,rnumber);
    input(n,rsum);
    cin >> K;
    if(cal_number(n,rsum,rnumber,K)){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
} 