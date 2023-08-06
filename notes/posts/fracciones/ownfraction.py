class MyFraction:
    
    def __init__(self, numerator:int, denominator:int = 1) -> None:
        self.numerator = numerator
        self.denominator = denominator

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
    
    q1 = MyFraction("hola",3)
    q2 = MyFraction(3.14, 2.72)
    print(q1)
    print(q2)

    r = MyFraction.gcd(220,140)
    print(r)