class MyFraction:
    
    def __init__(self, numerator:int, denominator:int = 1) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    

if __name__ == "__main__":
    
    q1 = MyFraction(5,3)
    q2 = MyFraction(8)
    print(q1)
    print(q2)