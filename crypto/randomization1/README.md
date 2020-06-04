### Comments

#### Question

>Hear ye, for I have constructed another diversionary exercise taking the form of a competition whose contents consist of the repeated divination of an arbitarily and pseudorandomly generated numeric!
>Connect with nc crypto.hsctf.com 6001.

**File Attached**:rand1

### Answer

On connecting to the server it says
```
I heard LCGs were cool so I made my own
Since I'm so generous you get a free number
```

LCG (Linear congruential generator) is an algorithm for generating pseudo random numbers. Here is the [wiki link](https://en.wikipedia.org/wiki/Linear_congruential_generator). The basic formula for the sequence is [img1]

So all we have to do is find a and c. For that I opened up ghidra and decompiled the binary.
The decompiled main function is [img3]

The decompiled next function is [img2]

From the next function we can clearly see that value of a is '%' and c is 0x41, So a = 37 and c = 65.
But still we needed the modulo value. I assumed it was 256, but in order to be sure, I ran the binary a couple of times by a python script and then checked the max value and it was always less than 256. So now all we had to do is use the pwntools and write a final python script that will give us the result. Also one thing if you notice, you will be asked the number 10 times because there is do .. while condition wrapped. 

```python
from pwn import *

io = remote('crypto.hsctf.com', 6001)
io.read()
value = io.read().decode('ASCII').replace('\n', ' ').split(' ')
curr = int(value[10])
nxt = (curr*37+65)%256
for _ in range(10):
    io.sendline(str(nxt))
    print(io.read().decode('ASCII').replace('\n', ' '))
    nxt = (nxt*37+65)%256
```

and you will get the flag.
**flag**: ```flag{l1n34r_c0n6ru3n714l_63n3r470r_f41lur3_4b3bcd43}```
