import os

answer = input("文字を入力！:")

with open("./9ch-test-/ans.txt", "w") as f:
    f.write(answer)
