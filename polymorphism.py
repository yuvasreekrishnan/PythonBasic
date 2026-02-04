class Details:
    # def sampleFunction(self, a):
    #     if(a == 10):
    #         return a*2
    #     else:
    #         print(a)
    #         return a

    # def sampleFunction(self,a,b):
    #     if(a == 10):
    #         return a*b
    #     else:
    #         return a

    def sampleFunction(self, a , b=None):
        if(b == None):
            return a
        else:
            return a*b
        
class parantClass:
    def sampleMethod(self, a):
        print(a)        
        

class childClass(parantClass):
    def sampleMethod(self, a):
        print("This is sample child method")


# detail = Details()
# a = detail.sampleFunction(8)
# print(a)

child = childClass()
child.sampleMethod(10)
        