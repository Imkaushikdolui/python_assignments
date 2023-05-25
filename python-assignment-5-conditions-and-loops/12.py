# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

total_classes = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / total_classes) * 100

print("Attendance percentage:", attendance_percentage)

if attendance_percentage < 75:
    print("The student is not allowed to sit in the exam.")
else:
    print("The student is allowed to sit in the exam.")
