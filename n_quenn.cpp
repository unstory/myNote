#include <cstdio>
#include<cmath>

using namespace std;

const int MAXN = 11;
int hashTable[MAXN] = {false};
int P[MAXN] = {0};
int n = 5;
int count = 0;


void generateP(int index){
    if(index == n + 1){
        count ++;
        for(int i=1; i<=n; i++){
            printf("%d", P[i]);
        }
        printf("%s", "----------\n");
    }
    for(int x=1; x <= n; x ++){
        if(hashTable[x] == false){
            bool flag = false;
            for(int pre=1; pre < index; pre ++){
                if(abs(pre - index) == abs(x - P[pre])){
                    flag = true;
                    break;
                }
            }
            if(!flag){
                P[index] = x;
                hashTable[x] = true;
                generateP(index + 1);
                hashTable[x] = false;
            }
        }
    }
}

int main(){
    generateP(1);
    printf("%d", count);
    return 0;
}

