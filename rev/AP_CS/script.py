op = "inagzgkpm)Wl&Tg&io"
x = ''
def unshift(s):
    x = ''
    for i in range(len(s)):
        r = chr((ord(s[i])) + i)
        x = x + r
    return x

def unshift2(s):
    y = ''
    for i in range(len(s)):
        c = ord(s[i])
        c1 = len(str(ord(s[i])))
        y = y+chr(c-c1)
    return y
print((unshift(unshift2(op))))