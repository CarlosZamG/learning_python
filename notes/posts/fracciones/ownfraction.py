class MyFraction:
    
    def __init__(self, numerator:int, denominator:int = 1) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    

if __name__ == "__main__":
    
    q1 = MyFraction(5,3)
    print(q1)