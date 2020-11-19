


a=800
b=215
for i in range(b):
    if a/b==11:
        print(f'{i+1}年前，父亲{a}岁，儿子{b}岁')
    a -= 1
    b -= 1
    if a==0 or b==0:
        break