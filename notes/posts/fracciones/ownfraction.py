class MyFraction:
    
    def __init__(self, arg1, arg2 = 1) -> None:
        
        if isinstance(arg1, int) and isinstance(arg2, int):
            d = self.gcd(arg1, arg2) 
            self.numerator = arg1//d
            self.denominator = arg2//d
        

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
    
    q1 = MyFraction(6, 3)
    q2 = MyFraction(3, 6)
    print(q1)
    print(q2)
