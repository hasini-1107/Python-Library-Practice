import numpy as np
Marks = np.array([[90, 97, 95],
                 [98, 67, 80],
                 [78, 93, 56],
                 [56, 68, 65]])
Student_Marks = np.mean(Marks, axis=1)
print("STUDENT AVERGE MARKS: ")
for i in range(len(Student_Marks)):

    print("Student", i+1, " : ", int(Student_Marks[i]))
print("\nSUBJECT AVERGE MARKS: ")
subject = np.mean(Marks, axis=0)
for j in range(len(subject)):

    print("Subject", j+1, " : ", int(subject[j]))
print("Highest marks: ", np.max(Marks))
print("Least marks: ", np.min(Marks))
fail = Marks < 60
print("Subjects Failed: ", fail)
print(Marks.shape)
