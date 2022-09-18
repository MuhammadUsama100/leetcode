import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:['a','b','c'] , 3:['d','e','f'] , 4:['g','h', 'i'] , 5:['j','k','l'] , 
             6:['m' ,'n', 'o'] , 7:['p','q','r','s'] , 8:['t','u','v'] , 9:['w','x','y','z']}
        cartesionProduct = []
        if(len(digits) == 0):
            cartesionProduct = []
        elif(len(digits) == 1):
            cartesionProduct = d[int(digits)]
        elif(len(digits) == 2):
            cartesionProduct = list(itertools.product(d[int(digits[0])],d[int(digits[1])]))
        elif(len(digits) == 3):
            cartesionProduct = list(itertools.product(d[int(digits[0])],d[int(digits[1])] ,d[int(digits[2])]))
        else:
            cartesionProduct = list(itertools.product(d[int(digits[0])],d[int(digits[1])] , 
                                   d[int(digits[2])] ,d[int(digits[3])]))
        outputList = []
        for c in cartesionProduct:
            output = ""
            for v in c:
                output = output + v
            outputList.append(output)
            
        print(len(outputList))
        return outputList