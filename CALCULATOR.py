import math
def add(i,x):
    total=int(x[0:i])+int(x[i+1:len(x)])
    print(total)

def sub(i,x):    
    total=int(x[0:i])-int(x[i+1:len(x)])
    print(total)
def division(i,x):
    total=int(x[0:i])/int(x[i+1:len(x)])
    print(total)

def floor(i,x):
    total=int(x[0:i])//int(x[i+2:len(x)])
    print(total)
def mult(i,x):  
    total=int(x[0:i])*int(x[i+1:len(x)])
    print(total)
def mod(i,x):    
    total=int(x[0:i]) % int(x[i+1:len(x)])
    print(total)
    
def sin(x): 
    total=math.sin(int(x))
    print(total)
def cos(x): 
    total=math.cos(int(x))
    print(total)
def tan(x): 
    total=math.tan(int(x))
    print(total)    
def cosec(x): 
    total=math.cosec(int(x))
    print(total)     
     
                     
def call(x):
    
    for i in range(len(x)):
        if(x[i]=="+"):
            add(i,x)
     
        elif(x[i]=="-"):
            sub(i,x)
    
        elif(x[i]=="*"):
            mult(i,x)
    
        elif(x[i]=="/"):
            if(x[i+1]=="/"):
                floor(i,x)
            else:
                division(i,x)  
    
        elif (x[i]=="%"): 
            mod(i,x)
    
        
        elif(x[i:i+3].capitalize()=="Sin" ):
            sin(x[i+3:len(x)])
        
        elif(x[i:i+3].capitalize()=="Cos" ):
            cos(x[i+3:len(x)])
        
        elif(x[i:i+3].capitalize()=="Tan" ):
            tan(x[i+3:len(x)]) 
        
      
x=input()
call(x)