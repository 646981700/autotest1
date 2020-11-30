import random

# 1.现在有一个列表 li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22],
# 请将 大于5的数据过滤出来，然后除以2取余数，结果放到新的列表中；
# ------------方案一------------
# li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22]
# li_2 = [i % 2 for i in li if i > 5]
# print(li_2)
# # ------------方案二------------
# class Workrange():
#     def __init__(self, li):
#         self.li=li
#         self.index=0
#         self.new=[]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index>=len(self.li):
#             raise StopIteration
#         if self.li[self.index]>5:
#             self.new.append(self.li[self.index]%2)
#         self.index+=1
#         return self.new
# li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22]
# a=Workrange(li)
# for i in a:
#     print(i)



# 2.使用思维导图梳理可迭代对象、迭代器和生成器相关知识（主要是区别、特点和联系，尤其是__next__的思想）




# 3、算法面试题
# 有一个正整数列表(数据是无序的,并且允许有相等的整数存在),
# 编写能实现下列功能的函数，传入列表和正整数x，返回下面要求的三个数据
# 1)统计并返回在列表中,比正整数x大的数有几个(相同的数只计算一次)，并返回----->返回值中的的count
# 2)计算列表中比正整数X小的所有偶数，并返回列表  ----------->返回值中的li
# 3)将列表中比正整数X小的偶数去掉,未去掉的数添加到新列表中，并返回新列表 ------->返回值中的new_array
# def func(array,x):
#     try:
#         if type(array)==list and type(x)==int:
#             count=0
#             lic=[]
#             li=[]
#             new_array=[]
#             for i in array:
#                 if i>x and i not in lic:
#                     lic.append(i)
#                     count+=1
#                 elif i<x and i%2==0 and i not in li:
#                     li.append(i)
#                 elif i<x and i%2!=0 and i not in new_array:
#                     new_array.append(i)
#                 else:
#                     pass
#             return count, li, new_array
#         else:
#             print("第一个值请传入列表类型，第二个值请传入数字类型")
#     except Exception as e:
#         print(e)
# lia=[random.randint(0,30) for i in range(random.randint(0,30))]
# x=random.randint(15,25)
# print('输入的整数列表及x{},{}'.format(lia,x))
# counta,lia,new_arraya=func(lia,x)
# print("输出结果",counta,lia,new_arraya)




# 4、定义一个函数实现以下功能，第一个元素是数据标识，第二个元素的数值必须大于等于50才返回，
# 不够50往后累加加到最后如果不够50也直接返回，因为没有可加的数据了

# def calnum(x):
#     try:
#         _num = 0
#         _li = []
#         for i in x:
#             if len(i) == 2 and type(i) == list:
#                 _num += i[1]
#                 if _num >= 50:
#                     _li.append([i[0], _num])
#                     _num = 0
#                 elif i == x[-1]:
#                     _li.append([x[-1][0], _num])
#             else:
#                 print('数据非列表或列表数据不是两个')
#         return _li
#     except Exception as e:
#         print(e)
