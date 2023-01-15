class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1       =   int(num1[0:num1.find('+')])
        imaginary1  =   int(num1[num1.find('+') + 1: num1.find('i')])
        real2       =   int(num2[0:num2.find('+')])
        imaginary2  =   int(num2[num2.find('+') + 1: num2.find('i')])
        
        resultReal = real1 * real2 - imaginary1 * imaginary2
        resultImaginary = real1 * imaginary2 + real2 * imaginary1
        
        return str(resultReal) + '+' + str(resultImaginary) + 'i'