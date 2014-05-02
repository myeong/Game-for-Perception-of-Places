import zlib
import bz2
import uu
import StringIO
import binascii
import os

text = "201308CLAS170"

def toValue(val):
    return{
        ' ': 0,        
        'A':1, 'B':2,
        'C':3, 'D':4,
        'E':5, 'F':6,
        'G':7, 'H':8,
        'I':9, 'J':10,
        'K':11, 'L':12,
        'M':13, 'N':14,
        'O':15, 'P':16,
        'Q':17, 'R':18,
        'S':19, 'T':20,
        'U':21, 'V':22,
        'W':23, 'X':24,
        'Y':25, 'Z':26,
        '0':27, '1':28, 
        '2':29, '3':30,
        '4':31,'5':32,
        '6':33,'7':34,
        '8':35,'9':36,
    }[val]    
    
def encode(txt):
    nums = txt[:6]
    code = txt[6:]
    compressed = ''
    encoded = ''
    i=9
    
    for nu in nums:
        compressed += format(int(nu), '04b')
                    
    for ch in code:
        compressed += format(toValue(ch), '06b')
    
    #b = bin(int(compressed, 2))
    print compressed       
        
    while i>0:        
        i = i-1
        data = compressed[:8]
        compressed = compressed[8:]
        encoded += chr(int(data, 2))
    return encoded
    

def comptest(s):
    print 'original length:', len(s),' ', s
    print 'zlib compressed length:', len(zlib.compress(s)),' ', zlib.compress(s)
    print 'bz2 compressed length:', len(bz2.compress(s)),' ', bz2.compress(s)
    
    out = StringIO.StringIO()
    infile = StringIO.StringIO(s)    
    uu.encode(infile, out)
    print 'uu:', len(out.getvalue()), out.getvalue()  

def toChar(val):
    return{
        0: ' ',        
        1:'A', 2:'B',
        3:'C', 4:'D',
        5:'E', 6:'F',
        7:'G', 8:'H',
        9:'I', 10:'J',
        11:'K', 12:'L',
        13:'M', 14:'N',
        15:'O', 16:'P',
        17:'Q', 18:'R',
        19:'S', 20:'T',
        21:'U', 22:'V',
        23:'W', 24:'X',
        25:'Y', 26:'Z',
        27:'0', 28:'1', 
        29:'2', 30:'3',
        31:'4', 32:'5',
        33:'6', 34:'7',
        35:'8', 36:'9',
    }[val]  
#comptest(text)
#print [ord(c) for c in text]
print encode(text)
print os.getcwd()