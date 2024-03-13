#include <iostream>
#include <list>

// a sudoku solver!,part of the sudoku.cpp file
std::pair<int,int> approx(int i,int j){
 int x,y;
 if ((i+1)%3 == 0){
  int x = i+1; 
 }else if ((i-1)%3 == 0){
  int x = i-1;
 }
 if ((j+1)%3 == 0){
  int y = j+1;
 }else if((j-1)%3 == 0){
  int y = j-1;
 }
 std::cout << x << y << '\n';
 return std::pair<int,int> {x,y};
}


// We returned an array here
std::list<int, std::allocator<int>> get_pos(int* arr,int i,int j){
 std::list<int> l = {1,2,3,4,5,6,7,8,9}; 
 for(int x = 0;x < 9;x++){
  l.remove_if([arr,i,x,j](int k){return (k == *(arr + 9*i + x) or k == *(arr + 9*x + j)); });
 };
 auto p = approx(i,j);
 for(int a = -1; a < 2; a++){
  for(int b = -1; b < 2;b++){
    l.remove_if([arr,a,b,p](int k){return *(arr + 9*p.first+ p.second + 9*a + b) == k;});
 }} 
 return l;
}

int main(){
 int map[9][9];
 for(int i=0;i < 9;i++){
  std::cin >> map[i][0] >> map[i][1] >> map[i][2] >> map[i][3] >> map[i][4] >> map[i][5] >> map[i][6] >> map[i][7] >> map[i][8];
 };
 for(int i =0;i < 9;i ++){
  for (int j=0;j<9;j++){
    std::cout << i << j << '<';
    std::list<int, std::allocator<int>> l = get_pos(*map, i,j);
    for(int k:l){
     std::cout << k;
    }
    std::cout << '\n';
  }
 }
}