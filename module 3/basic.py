class Student :
    def __init__(self,n,cg):
          self.name=n
          self.cgpa=cg
    def show_info(self):
         print(f"{self.name} got cgpa {self.cgpa}")
    def dean_list(self):
         return self.cgpa>3
    
s1=Student("a",3.32)
s2=Student("b",2.3)
# print(s1.name)
# print(s1.cgpa)
# s1.show_info()
print(s1.dean_list())
print(s2.dean_list())