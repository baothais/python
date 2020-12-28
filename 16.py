def USCLN(a, b):
        # if b == 0:
        #     return a
        # return USCLN(self, b, a % b)
        while a*b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b

print(USCLN(10, 5))
