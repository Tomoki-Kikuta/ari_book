#include<iostream>
#include<algorithm>
#include<queue>
#define MAX 105
#define ROAD 1<<21
#define WALL 1
using namespace std;
int cal_cost(int start_x,int start_y,int goal_x,int goal_y,int maze[MAX][MAX]){
    queue<pair<int,int> > course;
    course.push(make_pair(start_x,start_y));
    maze[start_x][start_y] = 0;
    while(!course.empty()){
        int now_x = course.front().first;
        int now_y = course.front().second;
        course.pop();
        for(int x=-1;x<=1;x++){
            for(int y=-1;y<=1;y++){
                if((x+y)%2==0){
                    continue;
                }
                int next_x = now_x + x;
                int next_y = now_y + y;
                if(maze[next_x][next_y]==ROAD && maze[next_x][next_y] >= maze[now_x][now_y] + 1){
                    course.push(make_pair(next_x,next_y));
                    maze[next_x][next_y] = maze[now_x][now_y] + 1;
                }
            }
        }
    }
    if(maze[goal_x][goal_y]==ROAD){
        maze[goal_x][goal_y] = -1;
    }
    return maze[goal_x][goal_y];
}
int main(void){
    int height,widch,start_x,start_y,goal_x,goal_y;
    int maze[MAX][MAX];
    cin >> height >> widch;
    for(int i=0;i<=height+1;i++){
        maze[i][0] = WALL;
        maze[i][widch+1] = WALL;
    }
    for(int i=0;i<=widch+1;i++){
        maze[0][i] = WALL;
        maze[height+1][i] = WALL;
    }
    for(int i=1;i<=height;i++){
        for(int j=1;j<=widch;j++){
            char road;
            cin >> road;
            if(road=='S'){
                start_x = i;
                start_y = j;
                maze[i][j] = ROAD;
            }else if(road=='G'){
                goal_x = i;
                goal_y = j;
                maze[i][j] = ROAD;
            }else if(road=='#'){
                maze[i][j] = WALL;
            }else{
                maze[i][j] = ROAD;
            }
        }
    }
    cout << cal_cost(start_x,start_y,goal_x,goal_y,maze) << endl;
    return 0;
}