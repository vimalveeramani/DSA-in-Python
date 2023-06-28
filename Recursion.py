def fun(x,y):
  if (x==0) :
    return y
  else:
    return fun(x-1,x+y) 

x=int(input("Enter the value of x :")) 
y=int(input("Enter the value of y :"))
print("recursion", fun(x,y)) 
