class calculator:
    def __init__(self):
        self.x=1
        self.y=1
    def sum(self):
        return self.x+self.y
    def subtraction(self):
        return self.x-self.y
    def production(self):
        return self.x*self.y
    def division(self):
        if self.y!=0:
            return self.x/self.y
        else:
            return 'syntax error'
    def mod(self):
        return self.x%self.y
    def power(self):
        return self.x**self.y
    def setnumbers(self):
        self.x,self.y=map(float,input().split())
        return ''

m='no'
p=calculator()

print('''
    CHOOSE YOUR ACTION
0.Menu
1.sum 
2.subtraction
3.production
4.division
5.module
6.power
7.setnumbers
8.exit
    ''')

while True:
    m=input()
    
    if m=='0':
        print('''
    CHOOSE YOUR ACTION
0.exit
1.sum 
2.subtraction
3.production
4.division
5.module
6.power
7.setnumbers
    ''')
    if m=='1':
        print(p.sum())
    elif m=='2':
        print(p.subtraction())
    elif m=='3':
        print(p.production())
    elif m=='4':
        print(p.division())
    elif m=='5':
        print(p.mod())
    elif m=='6':
        print(p.power())
    elif m=='7':
        print(p.setnumbers())
    elif m=='8':
        break
    

    
    