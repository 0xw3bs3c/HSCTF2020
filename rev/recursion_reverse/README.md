### Recursion Reverse

#### Question
>Jimmy needs some help figuring out how computers process text, help him out!

**File Attached**: AscII.java
 
#### Answer
The function ```flagTransformed()``` does the following things:
1. increases every char by a particular value given by ```pickNum()```
2. reverses the string

Now if that is equal to ```I$N]=6YiVwC``` we get the correct answer.

So basically all we have to do is reverse the process. So I wrote a C++ script for that

```cpp
#include<bits/stdc++.h>
using namespace std;

int num =0;

// this function is the exact copy from the problem
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
    string flag = "I$N]=6YiVwC";

    // reversing the flag (#2)
    for(int i=0; i<=5; i++){
        swap(flag[i], flag[11-i]);
    }

    //subtracting the value that was added during encoding (#1)
    for(int i=0; i<12; i++){
        num=1;
        int value = 127-pickNum(i+1);
        while(value<0) value += 127;
        flag[i] =(char)(((int)flag[i] + value) % 127);	
    }
    cout<<flag;
    return 0;
}
```

**flag**: ```flag{AscII is key}``