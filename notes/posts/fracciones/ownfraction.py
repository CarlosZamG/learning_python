from functools import singledispatchmethod

class MyFraction:

    @singledispatchmethod
    def __init__(self, arg1, arg2) -> None:
        raise TypeError(f"unsupported type of arguments")

    @__init__.register(int)
    def from_integers(self, p:int, q:int = 1) -> None:

        if not isinstance(q,int):
          raise TypeError("the denominator should be an integer")

        if q == 0:
            raise ZeroDivisionError("the denominator should be non-zero")
        elif p == 0:
            self.numerator = p
            self.denominator = 1
        else:
            self.numerator = p
            self.denominator = q
            self.simplify()

    @__init__.register(float)
    def from_float(self, f:float):

        denominator = 1
        intarg = int(f)
        while f - intarg > 0.00001:
            f *= 10
            denominator *= 10
            intarg = int(f)

        self.numerator = intarg
        self.denominator = denominator
        self.simplify()

    @classmethod
    def from_fraction(cls, fraction):

        if isinstance(fraction, MyFraction):
            return cls(fraction.numerator, fraction.denominator)
        else:
            raise TypeError("argument should be an instance of MyFraction")


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
    print(q1)

    q2 = MyFraction(32,-8)
    print(q2)

    q3 = MyFraction(3.14)
    print(q3)

    q4 = MyFraction.from_fraction(q2)
    print(q4)