#input var -- rno, sname, s1, s2, s3
#process var -- tot, avg, grade
#output var -- rno, sname, tot, avg, grade

rno=input("Enter REGD No  : ")
sname = input("Enter SNAME  : ")
s1 = int(input("Enter S1 marks  : "))
s2 = int(input("Enter S2 marks  : "))
s3 = int(input("Enter S3 marks  : "))
total = s1 + s2 + s3
avg = total/3
if s1 < 40 or s2 < 40 or s3 < 40:
    grade = "F"
elif avg >= 40 and avg <= 49:
    grade = "D"
elif avg >= 50 and avg <= 59:
    grade = "C"
elif avg >= 60 and avg <= 69:
    grade = "B"
elif avg >= 70 and avg <= 79:
    grade = "A"
elif avg >= 80 and avg <= 89:
    grade = "S"
else:
    grade = "O"
print("RNO   :  ",rno)
print("SNAME :  ",sname)
print("TOTAL :  ",total)
print("AVG   :  ",avg)
print("Grade :  ",grade)


