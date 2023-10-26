

class twoInt():
    def __init__(self, x, y):
        self._x = x
        self._y = y


    @property
    def x(self):
        print("@property")
        return self._x

    @x.setter
    def x(self, value):
        self._x = value._x
        self._y = value._y


    @x.getter
    def x(self):
        print("@x.getter ")
        return self._x



if __name__ == "__main__":
    i = twoInt(1,2)
    j = twoInt(3,4)
    i = j
