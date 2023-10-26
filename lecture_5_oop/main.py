class complex_number:
    type = "complex_number"
    def __init__(self, a,b):
        self.re = a
        self.im = b
    def __abs__(self):
        return

    def __str__(self):
        return f"по возможности машиночитаемое представление \n {self.type} : re:{self.re}  im:{self.im}"


    def __eq__(self, other):
        return (self.im == other.im and self.re == other.re)

    def __sub__(self, other):
        return complex_number(self.re-other.re, self.im - other.im)

    def __add__(self, other):
        return complex_number(self.re+other.re, self.im+other.im)

    def __repr__(self):
        return "человекачитаемое исполнение"


    def _getRI_(self):
        return self.re, self.im
    def _setRI_(self, value):
        self.re = value.re
        self.im = value.im
    def _delRI_(self):
        self.re = 0
        self.im = 0
    RI = property(
        fget=_getRI_,
        fset=_setRI_,
        fdel=_delRI_,
    )

class integer(complex_number):
    def __init__(self, a):
        super().__init__(a, 0)



if __name__ == "__main__":
    j = complex_number(1,2)
    j.RI = complex_number(4, 3)

    print(j)


