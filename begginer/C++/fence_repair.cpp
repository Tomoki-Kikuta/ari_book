#include<iostream>
#include<algorithm>
#define MAX 20001
using namespace std;
int cal_cost(int n,int L[MAX],int sum){
    int cost = 0;
    while(n!=1){
        int now_L = 0;
        int now_R = 1;
        if(L[now_L] > L[now_R]){
            swap(now_L,now_R);
        }
        for(int i=2;i<n;i++){
            if(L[i]< L[now_L]){
                now_R = now_L;
                now_L = i;
            }else if(L[i] < L[now_R]){
                now_R = i;
            }
        }
        cost += L[now_L] + L[now_R];
        if(now_L==n-1){
            swap(now_L,now_R);
        }
        L[now_L] += L[now_R];
        L[now_R] = L[n-1];
        n--;
    }
    return cost;
}
int main(void){
    int n,L[MAX],sum=0;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> L[i];
        sum += L[i];
    }
    if(n==1){
        cout << sum << endl;
    }else{
        cout << cal_cost(n,L,sum) << endl;
    }
    return 0;
} 
