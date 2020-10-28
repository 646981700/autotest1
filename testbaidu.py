data={}
#登录功能
def loginfun():
    print('提示：（1）登录  （2）注册')
    num = input('请选择')
    # 注册
    if str(num) == '2':
        while True:
            id = input('请输入账号')
            pwd = input('请输入密码')
            verify = input('请确认密码')
            if id in data.keys():
                print('账号密码已存在,请重新输入')
            else:
                if pwd == verify:
                    data[id] = pwd
                    print('注册成功')
                    break
                else:
                    print('两次密码输入错误，请重新输入')
    # 登录
    elif str(num) == '1':
        while True:
            id = input('请输入账号')
            pwd = input('请输入密码')
            if id in data.keys():
                if pwd == data[id]:
                    print('账号密码正确，登录成功')
                    print('----欢迎登录图书馆里系统----')
                else:
                    print('账号密码输入错误，请重新输入')
            else:
                print('账号密码输入错误，请重新输入')
    else:
        print('输入错误')
#登录方法
def login():
    while True:
        loginfun()

def climbStairs(self, n):
    if n <= 2:
        return n
    temp_list = [0, 1, 2]
    for i in range(3, n + 1):
        temp_list.append(temp_list[-1] + temp_list[-2])
    return temp_list[-1]




if __name__ == '__main__':
    login()

