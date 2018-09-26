import hashlib
str1 = "wozuishuai"
h1 = hashlib.md5()
h1.update(str1.encode(encoding = 'utf-8'))
print('jiami',h1.hexdigest())
