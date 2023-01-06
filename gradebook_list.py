#List of last semester classes and grades for gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# List of subjects for this semester gradebook
subjects = ["physics", "Calculus", "Poetry", "History"]
#List of grades for this semester gradebook
grades = [98, 97, 85, 88]
#This semesters gradebook list
gradebook= [["physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]
#Add computer science and grade to this semesters gradelist
gradebook.append(["Computer Science", 100])
#Add Visual arts and grade to this semsters gradebook
gradebook.append(["Visual Arts", 93])
#Change the last item in this semester gradebook list to 98
gradebook[-1][-1] = 98
#remove the grade from this semesters poetry gradebook
gradebook[2].remove(85)
#Add "pass" to Poetry grade in this semesters gradebook
gradebook[2].append("Pass")
#Combine this semesters gradebook to last_semester_gradebook
full_gradebook = gradebook + last_semester_gradebook
#Display the combined list of gradebook and last_semester_gradebook
print(full_gradebook)


