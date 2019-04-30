courses = ['History', 'Math', 'Physics', 'CompSci']
optional_courses = ['Sport', 'Music']
nums = [1, 4, 5, 9, 3, 2]

# Add
courses.append('Art')
courses.insert(0, 'Poetry')
courses.extend(optional_courses)

# Remove
courses.remove('Math')
popped = courses.pop()
print(popped)

# Reverse
# courses.reverse()
# courses.sort()
nums.sort()
nums.sort(reverse=True)
sorted_courses = sorted(courses)

# Math
print(sum(nums))

# Find
print('CompSci' in courses)
print(courses.index('CompSci'))

# Loop
for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)

print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:3])
print(courses[2:])
print(nums)
print(sorted_courses)
