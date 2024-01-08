import re

with open ("../files/grades.txt", "r") as file:
    grades = file.read()
    list_grades = grades.split("\n")
    listB = []
    for grade in list_grades :
        if grade.split(":")[-1].strip() == "B":
            listB.append(grade.split(":")[0])
    print(listB)