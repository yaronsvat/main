def func (str,i,j):
    if (i < len(str)):
        func (str, i+1, j*-1)
        if (j==1):
            print (str[i],end="")

print(func("Hello World",0,1))