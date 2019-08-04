#include<iostream>
#include<algorithm>
#define MAX 21
using namespace std;
bool cal_number(int n,long int k,long int number[MAX],int p,long int sum){
    bool flag;
    if(sum==k){
        flag = true;
        return flag;
    }
    if(p<n){
        flag = cal_number(n,k,number,p+1,sum);
        if(!flag){
            flag = cal_number(n,k,number,p+1,sum+number[p]);
        }
    }else{
        flag = false;
    }
    return flag;
}
int main(void){
    int n,k;
    long int number[MAX];
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> number[i];
    }
    cin >> k;
    if(cal_number(n,k,number,0,0)){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}