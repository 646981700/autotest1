import requests

# 1、实现一个网络请求超时重试的装饰器retry，
# 装饰下面的功能函数 如果请求网络超时，或者连接超时，
# 可以重新发送请求，如果重试三次之后，还是超时，抛出对应的异常。
#


#  2、 请设计一个装饰器 ,可以给函数扩展登录认证的功能（提示输入账号密码，然后进行校验），
# 多个函数同时使用这个装饰器， 调用函数的时候，只要登录成功一次，
# 后续的函数无需再进行登录（默认的认证账号：qwe123，密码：123456）
class LoginVerify:

    def __init__(self,fun):
        self.fun=fun
        self._token = None

    def __call__(self, *args, **kwargs):
        if not self._token:
            self.login()
        else:
            _attr=self.fun(*args,**kwargs)
            return _attr

    def login(self):
        print('请登录')
        use=input('账号：')
        pwd=input('密码：')
        if use=='qwe123'and pwd=='123456':
            print('登录成功')
            self._token=1
        else:
            print('密码错误，请重新输入')
            self.login()


@LoginVerify
def func(attr):
    print(attr)
    return attr

func(31241)
func(22222222)
func(22222222)


