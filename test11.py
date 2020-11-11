# #冒泡排序
# lista=[0,1,2,888,5,1,2,54,4,5,7,8,9,6,3,2,1,4,11,55,88,77,987,2,23,54,87,98]
# listput=[]
#
# for i in range(len(lista)-12):
#     for j in range(len(lista)-1):
#         if lista[j]>lista[j+1]:
#             lista[j], lista[j+1] = lista[j+1], lista[j]
#         else:
#             pass
#
#
# def bubbleSort(array):
#     sort = True
#     while sort:
#         sort = False
#         for i in range(len(array) - 1):
#             if array[i] > array[i + 1]:
#                 temp = array[i + 1]
#                 array[i + 1] = array[i]
#                 array[i] = temp
#                 sort = True
#
#
# bubbleSort(lista)

#爬楼梯

# def climb_stairs(n):
#     nums = [0, 1, 2]
#     if n == 1:
#         return nums[1]
#     elif n == 2:
#         return nums[2]
#     else:
#         for i in range(3, n + 1):
#             nums.append(nums[i - 1] + nums[i - 2])
#     return nums[n]

# def climbStairs(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     if n <= 2:
#         return n
#     temp_list = [0, 1, 2]
#     for i in range(3, n + 1):
#         temp_list.append(temp_list[-1] + temp_list[-2])
#     return temp_list[-1]
# print(climbStairs(11))














