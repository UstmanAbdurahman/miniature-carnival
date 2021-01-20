class `Algorithms`:
    def FizzBuzz(par1,par2): #the fizz buzz function
        num1 = par1
        num2 = par2
        for i in range(100):
            if i % num1 == 0 and i % num2 == 0: #this prints FizzBuzz IF "i" can be divided by num1 AND num2
                print("FizzBuzz")
            
            elif i % num1 == 0: #this prints Fizz IF "i" can be divided by num1
                print("Fizz")
                
            elif i % num2 == 0: #this prints Buzz IF "i" can be divided by num2
                print("Buzz")
                
            else: #this prints "i"
                print(i)
