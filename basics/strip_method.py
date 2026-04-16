# stripについて(文字列(str)に対してのメソッド)

# 文字列の最初と最後の空欄を除去してくれる。
name = input("名前を入力してください。")
print(name)
strip_name = name.strip()
print(strip_name)

# 引数を指定すると削除対象が引数で指定したものになる。。
eng_name = input("英語で名前を入力してください。")
print(f"{eng_name}：削除される前")
delete_text = input("削除したいアルファベット(削除は最初と最後に対してだけ)")
format_eng_name = eng_name.strip(delete_text)
print(f"{format_eng_name}：指定したアルファベットが削除されたもの。")
