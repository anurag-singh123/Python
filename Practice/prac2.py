# 5
'''
class Circle():
  def __init__(self, r):


    self.radius = r
  def area(self):


    return self.radius**2*3.14


  def perimeter(self):


    return 2*self.radius*3.14
NewCircle = Circle(8)
print("Area = ", NewCircle.area())
print("Perimeter = ", NewCircle.perimeter())
'''

# 4
'''
class py_solution:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack)==0
print("(){}[]",end="   ")
print(py_solution().is_valid_parenthese("(){}[]"))
print("()[{)}",end="   ")
print(py_solution().is_valid_parenthese("()[{)}"))
print("()",end="   ")
print(py_solution().is_valid_parenthese("()"))
'''

#1
'''
class Test:
    val=0
    def count_val():
        val = 10
        return val
Test.d = classmethod(Test.count_val)
count = Test.count_val()
print('Value returned by the method =',count)
'''

#2

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)