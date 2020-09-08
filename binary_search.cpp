#include<cstdio>

using namespace std;

const int MAXN = 11;
// 寻找左侧开始的位置。1. 若存在search_num,则返回左侧第一个位置的索引，否则返回该数字应该插入的位置的索引；
int main(){
    int P[MAXN] = {1, 3, 5, 7, 7, 9, 11};
    int l = 0;
    int h = 7;
    int mid = 0;
    int search_num = 7;
    while(l < h){
        mid = (l + h) / 2;
        if(P[mid] < search_num){
            l = mid + 1;
        }
        else if(search_num < P[mid]){
            h = mid - 1;
        }
        else{
            h = mid;
        }
    }
    printf("%d", l);
    return 0;
}