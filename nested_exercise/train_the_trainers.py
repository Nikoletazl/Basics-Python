count_jury = int(input())
presentation = input()
sum_all_grades = 0
count_all_grades = 0
while presentation != "Finish":
    sum_grade = 0
    for jury in range(1, count_jury + 1):
        grade = float(input())
        count_all_grades += 1
        sum_grade += grade
        sum_all_grades += grade
    average_grade = sum_grade / count_jury
    print(f"{presentation} - {average_grade:.2f}.")
    presentation = input()
else:
    average_all = sum_all_grades / count_all_grades
    print(f"Student's final assessment is {average_all:.2f}.")
