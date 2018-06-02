da = list(''.join(list(input().split("-"))))

a,b,c,d,e,f,g,h,i,j = (int(i) for i in da)

if (a+b+c == d+e+f and d+e+f == g+h+i+j):
    print("Goony!")
else:
    print("Pick up the phone!")
