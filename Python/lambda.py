#cube1=lambda x:x**3
#print(cube1(5))

#def cube(x):
    #return x*x*x
#print("cube :",cube(10))

#ans=lambda a,b:a if a>b else b
#print(ans(10,20))

num1=lambda a: f"{a}is odd" if a%2==0 else f"{a}even"
print(num1(20))

ans=lambda a,b,c: a if a>b and a>c else(b if b>c else c)
print(ans(10,20,30))