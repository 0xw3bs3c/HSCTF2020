### My First Calculator

#### Question
>I'm really new to python. Please don't break my calculator!
>nc misc.hsctf.com 7001
>There is a flag.txt on the server.

**File Attached**: calculator.py
 
#### Answer

It was a python2.x script running and eval() function of python is very vulnerable.Basically it takes a string which has a valid python expression, and evaluates it as a regular python code. A simpler way to understand it would be to run the python script in local machine or use the server, when asked for the first number enter 1 and then for the second number enter "first" without the quotes, you will get the result ```1 + 1 = 2```. You might think that it should give an error because the variable second is assigned a string "first", but its not the case instead, ```second = first``` . i.e it recognises first as a variable and it does a simple assignment operation.

In python 2.x input() is equivalent to eval(raw_input()) so basically if you enter a valid python expression in the input section it will first evaluate that expression. This gives us an oppurtunity to get a bash shell.
So just type this ```__import__('os').system('bash -i')``` in the input section and it will open up a shell.

For more you info can read this [article1](https://medium.com/@GallegoDor/python-exploitation-1-input-ac10d3f4491f), [article2](http://vipulchaskar.blogspot.com/2012/10/exploiting-eval-function-in-python.html)

![image](https://github.com/0xw3bs3c/HSCTF2020/blob/arnab/misc/my_first_calculator/image1.png)

**flag**: ```flag{please_use_python3}```
