You'll get one QR. Scan it and you'll get a zip file.

I cracked the zip file and got pass **qristal**

Use zbarimg or any QR extracting tool
```bash
zbarimg *.png > flags.txt
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

**Flag:** CUCTF{can_you_scan_me?}