#include<iostream>
#include<algorithm>
#define MAX 100005
using namespace std;
int cal_time(int n,pair<long int,long int> sort_f[MAX]){
    int count = 0;
    long int now_time = 0;
    for(int i=0;i<n;i++){
        if(now_time < sort_f[i].second){
            count++;
            now_time = sort_f[i].first;
        }
    }
    return count;
}
int main(void){
    int n;
    pair<long int,long int> sort_f[MAX];
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> sort_f[i].second;
    }
    for(int i=0;i<n;i++){
        cin >> sort_f[i].first;
    }
    sort(sort_f,sort_f+n);
    cout << cal_time(n,sort_f) << endl;
    return 0;
}