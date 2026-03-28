# 文字列の操作

# 小文字への変換 lower()
def str_method_1():
    name = "TUJI"
    name_komoji = name.lower()
    print(f"{name_komoji}：これは小文字")

# 大文字への変換 upper()
def str_method_2():
    name = "tuji"
    name_oomoji = name.upper()
    print(f"{name_oomoji}：これは大文字")


# 分割処理 split()
# 引数で渡された文字で区切ったリストが返される
def str_method_3():
    dates = "2024/03/01-2024/03/02-2024/03/03"
    date_list = dates.split("-")
    print(type(date_list))
    for date in date_list:
        print(f"{date}日")