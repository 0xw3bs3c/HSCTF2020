### Comments

#### Question
>I found this file on my Keith's computer... what could be inside?

**File Attached**: Comments.zip
 
#### Answer

The title of the challenge reminded me of zip comments. A comment is optional text information that is embedded in a Zip file.
You can look for the comments using the commands ```zipdetails -v``` .
![image](https://github.com/0xw3bs3c/HSCTF2020/blob/arnab/forensics/comments/image1.png)

Now all you have to do is keep unzipping and keep track of the comments. Also you can automate it by writing a python script using the zipfile module

But make sure you have unzipped all the files. Since there are only 8 zips. You can do it manually or by a bash script.

```python
import zipfile

archive = zipfile.ZipFile(r'./Comments.zip', 'r')

print("Flag : ", end="")

for i in range(1, 9):
    file = str(i)+".zip"
    print(str(archive.getinfo(file).comment)[2:3], end='')
    zipFile = './'+file
    archive = zipfile.ZipFile(zipFile, 'r')
```

The output gives the flag
**flag**: ```flag{4n6}```
