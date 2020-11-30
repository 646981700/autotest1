

# 1. 一个球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？请用递归实现！
# def rockfall(many, num=1, m=100.00):
#     if many <= num:
#         return m
#     return rockfall(many, num + 1, m / 2) + m + m / 2


# 2. 小明有200元钱 打算买200本书，A类书籍5元一本，B类书籍3元一本，
# C类书籍1元2本，请用程序算出小明一共有多少种买法?（面试笔试题）
num=0
a=5
b=3
c=0.5
for i in range(201):
    for x in range(201-i):
        for y in range(201-i-x):
            if i*c+x*b+y*a<=200 and i+x+y==200:
                num+=1
l=[1 for i in range(201) for x in range(201-i) for y in range(201-i-x) if i*c+x*b+y*a<=200 and i+x+y==200]
print(len(l))