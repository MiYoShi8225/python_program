
import csv

lists = [["TopGun","RiskyBusiness","MinorityReport"],["Titanic","TheRevenant","Inception"],["TrainingDay","ManonFire","Flight"]]

with open("./9ch-test-/practice.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for i in lists:
        w.writerow(i)