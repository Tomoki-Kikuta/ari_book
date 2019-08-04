#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 1001
using namespace std;
int count(int n,int m,vector<int>number_sum,int M){
    int count = 0;
    
} 
int main(void){
    int n,m,M;
    vector<int> number_sum;
    cin >> n >> m;
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        number_sum.push_back(a);
    }
    cin >> M;
    cout << count(n,m,number_sum,M) << endl;
    return 0;
}