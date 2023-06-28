def fun(x,y):
  if (x==0) :
    return y
  else:
    return fun(x-1,x+y) 

x,y=input("Enter the value of x and y :")
print("recursion", fun(x,y)) 
