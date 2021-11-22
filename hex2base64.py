class hex2base64:
    def __init__(self,input_str):
        self.input_str = input_str
    def hex2dec(self):
            import numpy as np
            x = str(self.input_str).lower()
            d = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
            L = len(x)
            coeff, expon = [],[]
            t = []
            for i , n in enumerate(x):
                coeff.append(n)
                expon.append(int(L-i-1))

            for i in range(len(coeff)):
                if coeff[i] in d.keys():
                    coeff[i] = d[coeff[i]]
                    coeff[i] = int(coeff[i])
                else:
                    coeff[i] = int(coeff[i])
            for i in range(len(coeff)):
                t.append(coeff[i]*(16**expon[i]))
            return np.sum(t)
    def decToBin(self):
        dec = self.input_str
        cnt = 0
        binary = 0
        while dec > 0:
            binary = int((dec %2))*int((10**cnt)) + binary
            dec = (dec//2)
            cnt +=1
        return binary

    def Bin264(self):
        import numpy as np
        x = self.input_str
        x = str(x)
        six4_dict= {'000000':'A',
                    '000001':'B',
                    '000010':'C',
                    '000011':'D',
                    '000100':'E',
                    '000101':'F',
                    '000110':'G',
                    '000111':'H',
                    '001000':'I',
                    '001001':'J',
                    '001010':'K',
                    '001011':'L',
                    '001100':'M',
                    '001101':'N',
                    '001110':'O',
                    '001111':'P',
                    '010000':'Q',
                    '010001':'R',
                    '010010':'S',
                    '010011':'T',
                    '010100':'U',
                    '010101':'V',
                    '010110':'W',
                    '010111':'X',
                    '011000':'Y',
                    '011001':'Z',
                    '011010':'a',
                    '011011':'b',
                    '011100':'c',
                    '011101':'d',
                    '011110':'e',
                    '011111':'f',
                    '100000':'g',
                    '100001':'h',
                    '100010':'i',
                    '100011':'j',
                    '100100':'k',
                    '100101':'l',
                    '100110':'m',
                    '100111':'n',
                    '101000':'o',
                    '101001':'p',
                    '101010':'q',
                    '101011':'r',
                    '101100':'s',
                    '101101':'t',
                    '101110':'u',
                    '101111':'v',
                    '110000':'w',
                    '110001':'x',
                    '110010':'y',
                    '110011':'z',
                    '110100':'0',
                    '110101':'1',
                    '110110':'2',
                    '110111':'3',
                    '111000':'4',
                    '111001':'5',
                    '111010':'6',
                    '111011':'7',
                    '111100':'8',
                    '111101':'9',
                    '111110':'+',
                    '111111':'/'}
        if (len(x)%6) != 0:
            padding = ("0"*(6-(len(x)%6)))
            x = padding + x
        base64 = []
        for i in range(0,len(x),6):
            base64.append(six4_dict[x[i:i+6]])
        base64 = ''.join(map(str, base64))
        return base64


