# 书籍类 定义def方法要加self,调用def方法不需要,
from abc import ABC, abstractmethod
import json

class Book:
    def __init__(self,id_book,title,author,total_num):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    def borrow_book(self):# 用户与书的交互self(代表借阅的书)
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):
        self.__available_num += 1

    def get__available_num(self):
        return self.__available_num


# 抽象类: 一种只能被继承不能被实例化的类,作用:规定子类必须实现的方法,强制子类必须遵循统一的代码规范
# Python中没有内置的抽象类,但可以使用abc模块来实现抽象类
# from abc import ABC, abstractmethod
# 会员类

class Member(ABC):# 继承ABC:标识抽象类
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.__password = password
        self.__borrowed_books = []

    def borrow_book(self,book):
        # 判断当前会员借阅数量已经达到最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print(f'当前会员{self.name}借阅数量已经达到最大限制')
            return False
        # 判断当前图书是否可借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            return True
        else:
            print(f'当前图书{book.title}已经借完')
            return False

    def return_book(self,book):
        # 判断当前会员是否借阅了该书籍
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            return True
        else:
            print(f'当前会员{self.name}未借阅该图书')
            return False
    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books


    # 获取当前会员可借阅的最大数量(子类中实现)
    @abstractmethod  # 标识抽象方法 装饰器:规定子类必须实现该方法 (类似于老师规定的作业,pass是没有答案)
    def get_max_books(self) -> int:
        pass


# 普通会员
class Norm_Menber(Member):

    def get_max_books(self) -> int: # (抽象类:子类类似于学生必须完成作业,才能实现实例对象)
        return 3

# vip
class Vip_Menber(Member):
    def __init__(self,id,name,password,vip_level: int):
        Member.__init__(self,id,name,password)
        self.vip_level: int = vip_level
    def get_max_books(self) -> int:
        return 6 + self.vip_level

# 图书馆管理系统
class Library_System:
    def __init__(self):
        self.books = {}    # 书籍列表 --->{"AI001":Book对象,"AI002":Book对象...}(dict)
        self.members = {}  # 会员列表 --->{"001":Member对象,"002":Member对象...}
        self.current_member:Member = None  # 当前会员
        # 加载数据(书籍,会员)
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        # 加载data目录下的数据-->存入self.books字典中
        with open('data/books.json','r',encoding='utf-8') as f:
            books_data = json.load(f) # 书籍列表
            for book_data in books_data: # 单个书籍
                self.books[book_data['编号']] = Book(book_data['编号'],book_data['标题'],book_data['作者'],book_data['数量'])
            print('加载书籍数据成功!')


    def load_members_data(self):
        with open('data/members.json','r',encoding='utf-8') as f:
            members_data = json.load(f) # json.load(f)将json文件中的数据加载为python对象
            for member_data in members_data:
                if member_data['卡号'].startswith('N') :# 判断是否为普通会员
                    self.members[member_data['卡号']] = Norm_Menber(member_data['卡号'], member_data['姓名'],member_data['密码'])
                elif member_data['卡号'].startswith('V'):
                    self.members[member_data['卡号']] = Vip_Menber(member_data['卡号'], member_data['姓名'],member_data['密码'],member_data['会员等级'])
            print('加载会员数据成功!')

    def login(self):
        # while True:
        #     print('[登录]')
        #     member_id = input('请输入会员卡号: ')
        #     password = input('请输入密码: ')
        #     if member_id in self.members and self.members[member_id].get_password() == password:
        #         self.current_member = self.members[member_id]
        #         print(f'登录成功!欢迎{self.current_member.name}')
        #         return True
        #     else:
        #         print('登录失败!卡号或密码错误')
        #         continue

        while True:
            print("\n【登录】")
            member_id = input("请输入会员卡号：")
            password = input("请输入会员密码：")

            # 判断会员卡号是否存在
            if member_id not in self.members:
                print("登录失败，会员卡号不存在！")
                continue

            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() == password:
                print(f"登录成功！欢迎{member.name}")
                self.current_member = member
                return True
            else:
                print("登录失败，密码错误！")
                continue

    def borrow_book(self):
        # 1.展示图书馆可以借阅的图书列表
        for book in self.books.values():
            print(f'编号:{book.id_book},标题:{book.title},数量:{book.total_num},可借数量:{book.get__available_num()}')

        # 2.获取用户输入的图书编号,执行借阅操作
        book_id = input('请输入要借阅的图书编号: ')
        if book_id not in self.books:
            print('图书编号不存在!')
            return
        self.current_member.borrow_book(self.books[book_id])
        print(f'借阅成功!当前会员{self.current_member.name}借阅了《{self.books[book_id].title}》')

    def return_book(self):
        # 1.展示当前会员借阅的图书列表
        print('您已借阅的图书列表:')
        for book in self.current_member.get_borrowed_books():
            print(f'编号:{book.id_book},标题:{book.title},数量:{book.total_num},可借数量:{book.get__available_num()}')

        # 2.获取用户输入的图书编号,执行归还操作
        book_id = input('请输入要归还的图书编号: ')
        if book_id not in self.books:
            print('图书编号不存在!')
            return
        self.current_member.return_book(self.books[book_id])
        print(f'归还成功!当前会员{self.current_member.name}归还了《{self.books[book_id].title}》')

    def query_borrowed_books(self): #查看某会员的借阅记录
        borrow_books = self.current_member.get_borrowed_books()
        if len(borrow_books) > 0:
            print('您已借阅的图书列表:')
            for book in borrow_books:
                print(f'编号:{book.id_book},标题:{book.title},数量:{book.total_num},可借数量:{book.get__available_num()}')
        else:
            print('您当前没有借阅任何图书')



    def run(self):
        if self.login():
            while True:
                print('\n【图书馆管理系统】')
                print('1. 借阅图书')
                print('2. 归还图书')
                print('3. 查询借阅')
                print('4. 退出系统')
                choice = input('请输入你的选择: ')
                match choice:
                    case '1':
                        self.borrow_book()
                    case '2':
                        self.return_book()
                    case '3':
                        self.query_borrowed_books()
                    case '4':
                        print('退出系统,886')
                        break
                    case _:
                        print('输入错误，请重新选择')









if __name__ == '__main__':
    ls = Library_System() # 创建图书馆管理系统对象
    ls.run()