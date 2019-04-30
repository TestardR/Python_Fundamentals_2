# Order might change
# Sets don't allow duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)

# Sets are optimized for find methods
print('Math' in cs_courses)

# Intersection
print(cs_courses.intersection(art_courses))

# Difference
print(cs_courses.difference(art_courses))

# Union
print(cs_courses.union(art_courses))
