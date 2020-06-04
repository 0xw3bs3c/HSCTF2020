import cv2
import numpy as np 

img_path = './BinaryWordSearch.png'
img = cv2.imread(img_path, 0)
img_reverted= cv2.bitwise_not(img)
new_img = img_reverted//255

arr = []

for i in range(1000):
    row = []
    for j in range(7, 1000, 8):
        binary_form = ''
        if j+7 <1000:
            for k in range(8):
                binary_form += str(new_img[i][j+k])
            row.append(chr(int(binary_form, 2)))
    arr.append(row)


for i in range(124): 
    for j in range(1, 124):
        if arr[i][j]=='f' and arr[i][j-1]=='l':
            print(i, j)


# print(arr[115][78], arr[115][79], arr[115][80], arr[115][81])

# for coord in lst_f:
#     x = coord[0]+1
#     y = coord[1]
#     if lst_l.count((x, y))>0 : 
#         print(x, y)

#     x = coord[0]-1
#     y = coord[1]
#     if lst_l.count((x, y))>0 : 
#         print(x, y)

#     x = coord[0]
#     y = coord[1]+1
#     if lst_l.count((x, y))>0 : 
#         print(x, y)

#     x = coord[0]
#     y = coord[1]-1
#     if lst_l.count((x, y))>0 : 
#         print(x, y)
    
#     x = coord[0]+1
#     y = coord[1]+1
#     if lst_l.count((x, y))>0 : 
#         print(x, y)
    
#     x = coord[0]-1
#     y = coord[1]-1
#     if lst_l.count((x, y))>0 : 
#         print(x, y)

#     x = coord[0]+1
#     y = coord[1]-1
#     if lst_l.count((x, y))>0 : 
#         print(x, y)

    
#     x = coord[0]-1
#     y = coord[1]+1
#     if lst_l.count((x, y))>0 : 
#         print(x, y)
    
