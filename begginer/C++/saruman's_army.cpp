#include<iostream>
#include<algorithm>
#define MAX 1001
using namespace std;
int search(int n,int R,int position[MAX],int i){
    int now_position = position[i];
    int next_position = position[i+1];
    i++;
    while(i<n && now_position + R <= next_position){
        i++;
        next_position = position[i];
    }
    return i;
}
int search_next(int n,int R,int position[MAX],int i){
    int now_position = position[i-1];
    int next_position = position[i];
    while(i<n && now_position + R >= next_position){
        i++;
        next_position = position[i];
    }
    return i;
}
int cal_cost(int n,int R,int position[MAX]){
    int count = 0,i = 0;
    while(i<n){
        i = search(n,R,position,i);
        i = search_next(n,R,position,i);
        count++;
    }
    return count;
}
int main(void){
    int n,R,position[MAX];
    cin >> n >> R ;
    for(int i=0;i<n;i++){
        cin >> position[i];
    }
    sort(position,position+n);
    cout << cal_cost(n,R,position) << endl; 
    return 0;
