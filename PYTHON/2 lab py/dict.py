student = {
    'name' : 'Dias',
    'age' : 18 ,
    'major' : 'A & C'
}
print(student)  #{'name': 'Dias', 'age': 18, 'major': 'A & C'}




for x in student.keys():    #name, age, major
    print(x)
for i in student.values():   #Dias, 18, A & C
    print(i)
for q, w in student.items():  #[('name', 'Dias'), ('age', 18), ('major', 'A & C')]
    print(f"{q}: {w}")