import matplotlib.pyplot as plt
#importing matplotlib as plt

#taking marks as the input
math_s = int(input('Score in Mathematics (out of hundred)'))
science_s = int(input('Score in Science (out of hundred)'))
english_s = int(input('Score in English (out of hundred)'))
history_s = int(input('Score in History (out of hundred)'))
PE_s = int(input('Score in PE (out of hundred)'))

#setting the categories
subjects = ['Math', 'Science', 'English', 'History', 'PE']
scores = [math_s, science_s, english_s, history_s, PE_s]

student_name = input('Enter the name of the student: ')

#setting the colors and then assigning the colors to the labels
colxrs = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#cc99ff']
plt.pie(scores, labels=subjects, colors=colxrs)
plt.title(student_name+'\'s result')

#shows the pie chart
plt.show()