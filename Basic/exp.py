#1
'''
courses = {'DAA':'CS','AOA':'ME','SVY':'CE'}

# iterate over key-value pair
for k,v in courses.items():
    print(k,v)

# iterate over keys
for k in courses.keys():
    print(k)

# iterate over values
for k in courses.values():
    print(k)

# iterate over keys-shorter
for k in courses:
    print(k)

# enumerate
for i,(k,v) in enumerate(courses.items()):
    print(i,k,"-",v)
'''

#2
'''
courses = {'CS101':'CPP','CS102':'DS','CS201':'OOP',\
           'CS226':'DAA','CS601':'Crypt','CS442':'Web'}

# add, modify, delete
courses['CS444']='Web Services'  #add new key-value pair
courses['CS201']='OOP' #modify value for a key 
for k,v in courses.items():
    print(k,v)
print("\n")
del(courses['CS102']) #delete a key value pair 
for k,v in courses.items():
    print(k,v)
del(courses) #delete dictionary object
'''

#3 Many built in functions
'''
d={'CS101':'CPP','CS102':'DS','CS201':'OOP'}
print(len(d))
print(max(d))
print(min(d))
print(sorted(d))
# print(sum(d))
print(any(d))
print(all(d))
print(reversed(d))
for k,v in reversed(d.items()):
    print(k,v)
'''

#4
'''
c={'CS101':'CPP','CS102':'DS','CS201':'OOP'}
d={'ME126':'HP','ME102':'TOM','ME234':'AEM'}

print(c.get('CS102','Absent')) #print DS
print(c.get('EE102','Absent')) #prints Absent
# print(c['EE102']) #raises error

print(c.update(d))
print(c.popitem()) 
print(c.pop('CS102')) #removes keys and return value
print(c.clear())
'''

#5 Merging two dictionaries
'''
animals = {'Tiger':141,'Lion':152,'leopard':110}
birds = {'Eagle':38,'Crow':3,'Parrot':2}
combined = {**animals,**birds}
print(combined)
'''

#6 Convert list to directory
'''
lst = [12,13,14,15,16]
d = dict.fromkeys(lst,25)
print(d)
'''

# for ch in 'good afternoon':
#     print(ch)

# lst = [10,20,30,40]
# i = lst.__iter__()
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())

# lst = [10,20,30,40]
# i = iter(lst)
# print(next(i))
# print(next(i))
# print(next(i))
# print(hasattr(i,'__next__'))

class Employee :
    def set_data(self, n, a, s) :
        self.name = n
        self.age = a
        self.salary = s
    def display_data(self) :
        print(self.name, self.age, self.salary)
e1 = Employee( )
e1.set_data('Ramesh', 23, 25000)
e1.display_data( )
e2 = Employee( )
e2.set_data('Suresh', 25, 30000)
e2.display_data( )

