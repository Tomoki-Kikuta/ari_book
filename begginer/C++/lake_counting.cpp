#include<iostream>
#include<algorithm>
#define MAX 101
using namespace std;
void cal_lake(int h,int w,char puddle[MAX][MAX]){
    puddle[h][w] = '.';
    for(int x=-1;x<=1;x++){
        for(int y=-1;y<=1;y++){
            if(puddle[h+x][w+y]=='W'){
                h += x;
                w += y;
                cal_lake(h,w,puddle);
            }
        }
    }
}
int main(void){
    int height,widch,count = 0;
    char puddle[MAX][MAX];
    cin >> height >> widch;
    for(int i=0;i<height;i++){
        for(int j=0;j<widch;j++){
            cin >> puddle[i][j];
        }
    }
    for(int i=0;i<=height+1;i++){
        puddle[i][0] = '.';
        puddle[i][widch+1] = '.';
    }
    for(int i=0;i<=widch+1;i++){
        puddle[0][i] = '.';
        puddle[height+1][i] = '.';
    }
    for(int i=1;i<=height;i++){
        for(int j=1;j<=widch;j++){
            if(puddle[i][j]=='W'){
                cal_lake(i,j,puddle);
                count++;
            }
        }
    }
    cout << count << endl;
    return 0;
} 