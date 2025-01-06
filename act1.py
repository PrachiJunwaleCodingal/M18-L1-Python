#Exam eligibility check

med=input("Any medical cause (Y or N) for absentees: ")
att = int(input("Enter the attendance: "))

if med == 'Y': 
  print ("Allowed for exam")
else:
  if att>=75:  
    print ("Allowed for exam")
  else:
    print ("Not allowed for exam")