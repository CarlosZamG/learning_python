class MyFraction:
    
    def __init__(self, arg1, arg2 = 1) -> None:
        
        if isinstance(arg1, int) and isinstance(arg2, int):
            if arg2 == 0:
                raise ZeroDivisionError("the denominator should be non-zero") 
            elif arg1 == 0:
                self.numerator = arg1
                self.denominator = 1
            else:
                self.numerator = arg1
                self.denominator = arg2
                self.simplify()
        elif isinstance(arg1, float) and arg2 == 1:
            intarg = int(arg1)
            while arg1 - intarg > 0.00001:
                arg1 *= 10
                arg2 *= 10
                intarg = int(arg1)

            self.numerator = intarg
            self.denominator = arg2
            self.simplify()
        elif isinstance(arg1, MyFraction) and arg2 == 1:
            self.numerator = arg1.numerator 
            self.denominator = arg1.denominator

        

    def simplify(self):
        
        abs_n = abs(self.numerator)
        abs_d = abs(self.denominator)
        d = self.gcd(abs_n,abs_d)
        self.numerator //= d
        self.denominator //= d

        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    
    @staticmethod
    def gcd(a:int, b:int) -> int:
        
        if a<b:
            a,b = b,a
        
        r = a % b
        while r != 0:
            
            a = b
            b = r
            r = a % b

        return b
    

if __name__ == "__main__":
    
    q1 = MyFraction(12,8)
    q2 = MyFraction(q1)
    print(q1)
    print(q2)
