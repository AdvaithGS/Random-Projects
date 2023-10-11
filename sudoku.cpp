#include <iostream>
#include <list>
#include <algorithm>
#include <array>

int main(){
 std::cout << "Enter map" << '\n';
 int map[9][9];
 for(int i=0;i < 9;i++){
  for(int j =0;j < 9;j++){
   if(j == 0){
    std::cout << '\n'; 
   }
   std::cin >> map[i][i];
  }
 };
 sudoku(*map,0,0);
 int* i = *map;
 for(int j = 0;j< 81;j++){
  if(j%9 == 0){
   std::cout << '\n';
  };
  std::cout << *i << ' ';

 }
}

// We returned a list here
std::list<int, std::allocator<int>> get_pos(int* arr,int i,int j){
 std::list<int> l = {1,2,3,4,5,6,7,8,9}; 
 for(int x = 0;x < 9;x++){
  l.remove_if([arr,i,x,j](int k){return (k == *(arr + 9*i + x) or k == *(arr + 9*j + x)); });
 };
 return l;
}


int add(int i, int j){
 if((j+1)%9 < j){
  return 1;
 }else{
  return 0;
 }
}

bool sudoku(int* map, int i, int j){
 if(i == 9){
  return 1;
 }
 if ((*(map + (9*i) + j)) != 0){
  // (j + 1)%9  i + ((j+1)%9 < (j))
  return sudoku(map,i + add(i,j), (j+1)%9 );
 }else{
  std::list<int, std::allocator<int>> l = get_pos(map,i,j);
  if (l.empty()){
   return 0;
  }
  for( int i : l){
   *(map + (9*i) + j) = i;
   if ((sudoku(map,i + add(i,j), (j+1)%9 )) == 1){
    return 1;
   }else{
    *(map + (9*i) + j) = 0;
   }
  }
 }
}

