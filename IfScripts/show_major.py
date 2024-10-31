# # Define known values
# student = [
#     {'student name': 'Craig', 'student major': 'ENG'},
#     {'student_name': 'John', 'student_major': 'BIOL'},
#     {'student_name': 'Jane', 'student_major': 'CSCI'},
#     {'student_name': 'Tim', 'student_major': 'HIST'},
#     {'student_name': 'Tom', 'student_major': 'MKT'}
# ]

# student_major = [
#     {'BIOL': 'Biology', 'dept_office': 'Science Bldg, Room 310'},
#     {'CSCI': 'Computer Science', 'dept_office': 'Sheppard Hall, Room 314'},
#     {'ENG': 'English', 'dept_office': 'Kerr Hall, Room 201'},
#     {'HIST': 'History', 'dept_office': 'Kerr Hall, Room 114'},
#     {'MKT': 'Marketing', 'dept_office': 'Westly Hall, Room 310'}
# ]

# # Calculate unknown values
# if student_major == 'BIOL':
#     print(student_major['dept_office'])

# print(student['student_name'])






# Define known values
student_name = input('Student name is? ')
student_major = input('Major Code is? ')

if student_major == 'BIOL':
    major = 'Biology'
    dept_office = 'Science Bldg, Room 310'
    print(f'{major}, {dept_office}')
elif student_major == 'ENG':
    major = 'English'
    dept_office = 'Kerr Hall, Room 201'
    print(f'{major}, {dept_office}')
elif student_major == 'HIST':
    major = 'History'
    dept_office = 'Kerr Hall, Room 114'
    print(f'{major}, {dept_office}')
elif student_major == 'MKT':
    major = 'Marketing'
    dept_office = 'Westly Hall, Room 310'
    print(f'{major}, {dept_office}')
elif student_major == 'CSCI':
    major = 'Computer Science'
    dept_office = 'Sheppard Hall, Room 314'
    print(f'{major}, {dept_office}')
else:
    major = '<unknown>'
    dept_office = ''
    print(f'{major}, {dept_office}')

    