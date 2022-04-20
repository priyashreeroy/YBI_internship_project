class power:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def cal(self):
        print(self.a**self.b)
    

a=int(input("x: "))
b=int(input("n: "))
pow1=power(a,b)
pow1.cal()