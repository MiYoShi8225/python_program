import csv

lists = [["トップガン","リスキービジネス","マイノリティーリポート"],["Titanic","TheRevenant","Inception"],["TrainingDay","ManonFire","Flight"]]

#with open("./9ch-test-/practice2.csv", "w", encoding="utf-8") as f:
with open("./9ch-test-/practice3.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for i in lists:
        w.writerow(i)