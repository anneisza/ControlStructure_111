#1. Write a PYTHON program to evaluate the student performance

    # If % is >=90 then Excellent performance

    # If % is >=80 then  Very Good performance

    # If % is >=70 then Good performance

    # If % is >=60 then average performance 

percentage = float(input("Masukkan persentase nilai siswa: "))

if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print(" Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Needs Improvement")