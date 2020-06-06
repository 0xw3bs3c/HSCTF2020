#include<bits/stdc++.h>
using namespace std;

int num =0;

int pickNum(int i) {
    for(int x = 0; x <= i; x++)
        num+=x;
    if(num % 2 == 0)
        return num;
    else 
        num = pickNum(num);	
    return num;		
}

int main(){

    string flag = "I$N]=6YiVwC";
    for(int i=0; i<=5; i++){
        swap(flag[i], flag[11-i]);
    }
    cout<<flag<<endl;
    for(int i=0; i<12; i++){
        num=1;
        int value = 127-pickNum(i+1);
        while(value<0) value += 127;
        flag[i] =(char)(((int)flag[i] + value) % 127);	
    }
    cout<<flag;
    return 0;
}