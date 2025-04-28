import random

student_scores = []
for i in range(10):
    student_scores.append(random.randint(1,100))

print(student_scores)

maxx = 0
for i in range(len(student_scores)):
    if maxx < student_scores[i]:
        maxx = student_scores[i]
print(f"Maximum number in the list is {maxx}")

# #OUTPUT
# [66, 18, 24, 40, 90, 83, 8, 57, 96, 29]
# Maximum number in the list is 96