#include<iostream>
#include<algorithm>
#define MAX 1001
using namespace std;
int count(int n,long int words[MAX]){
    int count = 0;
    int dp[MAX];
    for(int i=0;i<n;i++){
        dp[i] = 1;
        for(int j=0;j<i;j++){
            if(words[j]<words[i]){
                dp[i] = max(dp[i],dp[j]+1);
            }
        }
        count = max(count,dp[i]);
    }
    return count;
}
int main(void){
    int n;
    long int words[MAX];
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> words[i];
    }
    cout << count(n,words) << endl;
    return 0;
} 