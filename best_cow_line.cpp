#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(void){
    int n,now_S = 0,now_copy_S;
    string S,T,copy_S;
    cin >> n >> S;
    T = "";
    for(int i=n-1;i>=0;i--){
        copy_S.push_back(S[i]);
    }
    while(T.size()!=n){
        if(S[now_S]<copy_S[now_copy_S]){
            T.push_back(S[now_S]);
            now_S++;
        }else{
            T.push_back(copy_S[now_copy_S]);
            now_copy_S++;
        }
    }
    cout << T.c_str() << endl;
    return 0;
}