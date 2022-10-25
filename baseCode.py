# 基础语法
# CTRL + SHIFT + F10 运行当前py 文件
# CTRL + F10 运行 已经运行过的文件
# CTRL + ALT + L  格式化文件
# ALT + J  选择相同内容   vscode 中的  CTRL + SHIFT + D
import os.path
from sys import stdout
import sys
import keyword  # import 全局 模块

import poplib
import email.parser
import email.policy

import tool
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

# 将某个模块中的全部函数导入，格式为： from somemodule import *


def printKeyword():  # def 函数名
    print(keyword.kwlist)  # 缩进语法
    # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
    # 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
    # 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# printKeyword()


class GetType:  # class 类名称 首字母大写  getType => GetType
    def if_Else(self, flag):  # 命名规范  abc_abc 用下划线 连接  --- 这时候有代码校验报错 原因是 self 没有使用
        if flag:
            print("Answer")
            print("True")
        else:
            print("Answer")
            print("False")

    @staticmethod  # 这个是去掉 auto_pep8 校验问题，self 不使用, 但是也去掉其他 入参的判断
    def hello(self, flag):
        print(123)

    def number(self):
        # int      整数
        # bool     布尔
        # float    浮点数
        # complex  复数
        print(123)

    def string(self):
        str1 = 'abc'
        str2 = '''
abd
            efg
        '''
        # print(str)  # 输出字符串
        # print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
        # print(str[0])  # 输出字符串第一个字符
        # print(str[2:5])  # 输出从第三个开始到第五个的字符
        # print(str[2:])  # 输出从第三个开始的后的所有字符
        # print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)
        # print(str + "TEST")  # 连接字符串
        # print(str1, str2)

    def get_all(self):
        str1 = '''
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
        '''
        print(str1)

    def list(self):  # append()、pop()
        list1 = [1, 2, 3, 4, 5, 6]  # 列表     数组 array
        print(list1)

    def tuple(self):  # 前端没有的类型 元组
        tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
        print(tuple1)

    def set(self):  # 前端没有的类型 集合------------  有点像对象  也像 元祖
        # sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
        # print(sites)
        a = set('abracadabra')
        b = set('alacazam')
        print(a)
        print(a - b, 'a 和 b 的差集')  # a 和 b 的差集
        print(a | b, 'a 和 b 的并集 ')  # a 和 b 的并集
        print(a & b, 'a 和 b 的交集')  # a 和 b 的交集
        print(a ^ b, 'a 和 b 中不同时存在的元素')  # a 和 b 中不同时存在的元素

    def dict(self):  # 前端的对象
        # dict.items()
        dict1 = {}
        dict1['one'] = "1 - 菜鸟教程"
        dict1[2] = "2 - 菜鸟工具"
        tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
        print(dict1['one'])  # 输出键为 'one' 的值
        print(dict1[2])  # 输出键为 2 的值
        print(tinydict)  # 输出完整的字典
        print(tinydict.keys())  # 输出所有键
        print(tinydict.values())  # 输出所有值

    def ranger(self):
        list1 = []
        for i in range(10):
            list1.append(i)

        multiples = [i for i in range(30) if i % 3 == 0]
        print(multiples, list1)

    def while2(self, count=20):  # count 设置默认值
        while count < 9:
            count = count + 1
            if count == 4:
                print(count, 'ddd')
                # break  # 打断循环
                continue  # 跳过一次循环
            print(count, " 小于 9")
        else:
            print(count, " 大于或等于 9")

    def iter(self):
        list1 = range(10)
        # id(list1)  获取变量id地址，当 重新赋值 id 会变
        k = iter(list1)  # 创建迭代器对象
        print(next(k), 1)
        print(next(k), 2)
        print(next(k), 3)
        print(next(k), 4)

    def printinfo(arg1, *vartuple):
        "打印任何传入的参数"
        print("输出: ")
        print(arg1)
        print(vartuple)

        # printinfo(1,2,3,4,5)  # 输出   1   (2,3,4,5)

    def printinfo(arg1, **vardict):  # 加了两个星号 ** 的参数会以字典的形式导入
        "打印任何传入的参数"
        print("输出: ")
        print(arg1)
        print(vardict)

        # 调用printinfo 函数
        # printinfo(1, a=2, b=3)
        # 1
        # {'a': 2, 'b': 3}


# x = lambda a : a + 10  匿名函数  类似 (i)=>{a+10}
# x(5)  # 15
test = GetType()

# test.iter()


class UserAction:  # 用户交互 对实际文件操作
    def __init__(self):
        self.name = '用户交互'

    def input(self):
        message = input('222')
        print(message)

    def open(self):
        # a 后面加   r =read  w=write  r+ 读写
        with open('./img/123.txt', mode='a', encoding='utf-8') as file:
            file.write('3333 \n 你好')
            # print(file.read())

    def dir(self, xx):
        multiples = [i for i in dir(xx)]
        print(self.name)
        # print(dir(xx), multiples)
        # multiples = [i for i in dir(xx) if '__' not in i]
        for i in multiples:
            if '__' not in i:
                print(i)  # CreateAdb create_driver

    def sys(self):
        print(sys.ps1, sys.ps2)  # 不明白

    def os(self, path):
        p = os.path.abspath(path)  # 返回文件绝对路径  img/123.txt
        print(p)
        print(sys.argv, 'argv')


# action = UserAction()
# action.dir(tool)
# action.sys()


# stdout.write('xxxx')


conn = poplib.POP3_SSL('pop.163.com', 995)


conn.user('xiaolin0903106@163.com')
conn.pass_('UVIWVTYEGVAVEITQ')  # 注意输入的是邮箱授权码而不是真实 QQ 密码


response, maillist, r = conn.list()
print('响应：', response)
print('邮件列表：', maillist)

msg = email.parser.BytesParser(policy=email.policy.default).parsebytes(data)
for part in msg.walk():
    # multipart 代表邮件内容的容器，无需处理
    if part.get_content_type().split("/", 1)[0] == 'multipart':
        continue
    elif part.get_content_type().split("/", 1)[0] == 'text':
        print(part.get_content())
    else:
        filename = part.get_filename()
        print(filename)
        with open(filename, 'wb') as f:
            f.write(part.get_payload(decode=True))



'''














































'''
