You'll get one png file which contains QR code. Scan it using **zbarimg** and a link to **google drive** will appear.

**Download** the zip file from the google drive.

**Crack** the zip file with any file cracking tool.

After cracking the file, you'' get pass **qristal**.

**Extract** the zip file and you'll get a lot of png files which were all QR codes.


Use zbarimg or any QR extracting tool
```bash
zbarimg *.png > flags.txt

Note: I replaced "QR-Code:" from all the lines using a text editor.
```


You'll see many duplicate texts. So let's carve out the duplicates and get the unique ones only using python.

```python
sanitized = []
unique = []

with open('flags.txt', 'r') as f:
    x = f.readlines()
    for i in x:
        sanitized.append(i.replace('\n', ''))

for i in sanitized:
    if i not in unique:
        unique.append(i)

print(unique)
```

**Output:**
```text
['CUCTF{This_is_fake_flag}', 'CUCTF{This_is_wrong_one}', 'CUCTF{Not_this_one}', 'CUCTF{can_you_scan_me?}'] 
```

**Flag:**  CUCTF{can_you_scan_me?}