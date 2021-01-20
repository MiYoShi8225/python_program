import os

#実行ディレクトリのパスを表示する
print(os.getcwd())


"""
r 読み取り専用
w　書き込み専用
w+ 読み書き両方
"""
# はじめに open でファイル名とタイプを宣言する
st = open("st.txt", "w")
st.write("Hi from python.")
# openしたものをcloseする
st.close()

"""
st = open("jp.txt", "w", encoding="utf-8")
st.write("これは日本語です")
st.close
"""

#with~で自動でopenしたものcloseする
with open("auto.txt", "w") as f:
    f.write("hello! auto")

