grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


a=sorted(students)
keys=a
values=grades
b=(values)
info = dict(zip(a,b))
info['Aaron'] = (sum(info['Aaron'])) / len((info['Aaron']))
info['Bilbo'] = (sum(info['Bilbo'])) / len((info['Bilbo']))
info['Johnny'] = (sum(info['Johnny'])) / len((info['Johnny']))
info['Khendrik'] = (sum(info['Khendrik'])) / len((info['Khendrik']))
info['Steve'] = (sum(info['Steve'])) / len((info['Steve']))
print(info)
