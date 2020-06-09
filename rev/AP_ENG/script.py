
o = '1dd3|y_3tttb5g`q]^dhn3j'
def detranspose(s):
    transpose = [11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9]
    ch_ord = zip(list(s), transpose)
    t = sorted(ch_ord, key = lambda x:x[1])
    actual = ''.join([x[0] for x in t])
    # print(actual)
    return actual
def dexor(s):
    x = ''
    xor = [4,1,3,1,2,1,3,0,1,4,3,1,2,0,1,4,1,2,3,2,1,0,3]
    for i in range(len(xor)):
        x = x + chr(xor[i] ^ ord(s[i]))
    return x
count = 0
for y in range(3):
    o = dexor(o)
    o = detranspose(o)
    count += 2

print(o, count)
# print(detranspose('absadasdas'))