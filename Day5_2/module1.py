try:
    
    def fibo(n):
        a,b=0,1
        while a<n:
            print(a,end=' ')
            a,b=b,a+b
            print()
 
    def fibo_2(n):
        result=[]
        a,b=0,1
        while a<n:
            result.append(a)
            a,b=b, a+b
        return result 
    def fact(n):
        if n==1:
            return n
        else:
            return n*fact(n-1)
        
except FileNotFoundError:
    print(f"The file '{fname}' was not found.")
    print(sys.exc_info()[0].__name__)