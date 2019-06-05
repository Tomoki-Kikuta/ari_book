#include<iostream>
#include<algorithm>
using namespace std;
int cash(int i){
    if(i==5){
        return 500;
    }else if(i==4){
        return 100;
    }else if(i==3){
        return 50;
    }else if(i==2){
        return 10;
    }else if(i==1){
        return 5;
    }else{
        return 1;
    }
    return 0;
}
long int cal_number(long int Coin[6],long int A){
    long int count = 0;
    long int sum_cash = 0;
    int i = 5;
    while(sum_cash!=A){
        if(Coin[i]==0){
            i--;
            continue;
        }else if(sum_cash + cash(i) <= A){
            sum_cash += cash(i);
            count++;
            Coin[i]--;
        }else{
            i--;
        }
    }
    return count;
}
int main(void){
    long int Coin[6];
    long int A;
    for(int i=0;i<6;i++){
        cin >> Coin[i];
    }
    cin >> A;
    cout << cal_number(Coin,A) << endl;
    return 0;
}