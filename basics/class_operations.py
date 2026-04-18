# クラス

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name}：ユーザー名")
        print(f"{self.age}：年齢")

name = input("ユーザー名を入力してください")
age = input("年齢を入力してください")

user = Student(name,age)


# 継承
# クラス名の後ろに()をつけて継承したいクラスを記述する
class NewClass(Student):
    pass


# クラスの属性を書き換える方法
user.name = "これで上書き"