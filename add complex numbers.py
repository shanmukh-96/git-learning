class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result
    
n1 = Complex(9,5)
n2 = Complex(6,3)

add_complex = n1.add(n2)

print("real part :", add_complex.real)
print("imag part :", add_complex.imag)