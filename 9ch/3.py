import csv

with open("st.csv", "w", newline="") as f:
    #delimiter は区切り文字を意味する
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])
    
