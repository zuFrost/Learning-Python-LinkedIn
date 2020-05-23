# def Calc(currency,*rates):
#   for i in rates:
#     print(currency*i)


# class myClass():
#   def method1(self):
#     print("myClass method1")

# class simple():
#     def add(self, a, b):
#         return a+b

# class advanced(simple):
#     def inverse (self,x,y):
#         return (1/simple.add(self,x,y))
#         # return (1/simple.add(x,y))



  


class Person:
  def __initialize__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex   


  

    


def main():
    print("hello!")
#   c = Calc(100, 10, 5)
    # c = simple()
    # c.add(3,4)
    # print(c.add(3,4))
    # a = advanced()
    # print(a.inverse(3,4))

    def inc(a,b=1):
        return(a+b)
    a=inc(1)
    a=inc(a,a)
    print(a)


  
if __name__ == "__main__":
  main()