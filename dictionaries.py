student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student['country'] = 'FR'
student.update({'name': 'Jane', 'age': 26, 'country': 'IT'})
age = student.pop('age')

print(student)
print(student['courses'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))
print(student['country'])
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())


for key, value in student.items():
    print(key, value)
