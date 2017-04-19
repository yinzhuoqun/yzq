
from functools import reduce
import re

class Bin(object):
    def __init__(self,n=1):
        if not -128<=n<=127:
            raise ValueError('n is an integer and it must between -128 and 127')
        self.n = n

    @property
    def true_code(self):       #原码
        n=self.n
        s=''
        nag = False
        if n==0:
            return '0000 0000'
        elif n<0:
            n=-n
            nag = True
        while n>0:
            s+=str(n%2)
            n>>=1
        s = s[::-1]
        s = s.zfill(8)
        if nag:
            s = '1' + s[1:]
        return ' '.join([s[:4],s[4:]])

    @property
    def complement_code(self):      #反码
        n=self.n
        s=''
        if n==0:
            return '0000 0000'
        elif n<0:
            n = 255 + n
        while n>0:
            s+=str(n%2)
            n>>=1
        s = s[::-1]
        s = s.zfill(8)
        return ' '.join([s[:4],s[4:]])

    @property
    def complemental_code(self):      #补码
        n=self.n
        s=''
        if n==0:
            return '0000 0000'
        elif n<0:
            n = 256 + n
        while n>0:
            s+=str(n%2)
            n>>=1
        s = s[::-1]
        s = s.zfill(8)
        return ' '.join([s[:4],s[4:]])

    def __xor__(self,other):  # ^
        s = ''
        for (x,y) in zip(self.complemental_code,other.complemental_code):
            if x==' ':
                s+=' '
                continue
            s+='0' if x==y else '1'
        return s

    def __or__(self,other):   #  |
        s = ''
        for (x,y) in zip(self.complemental_code,other.complemental_code):
            if x==' ':
                s+=' '
                continue
            s+='1' if '1' in x+y else '0'
        return s

    def __and__(self,other):  #   &
        s = ''
        for (x,y) in zip(self.complemental_code,other.complemental_code):
            if x==' ':
                s+=' '
                continue
            s+='0' if '0'  in x+y else '1'
        return s

    def __lshift__(self,n):   #<<
        if self.n<<n>127 or self.n<<n<-128:
            raise ValueError('The result %d > 127 or %d <-128'%(self.n<<n,self,n<<n))
        s = self.complemental_code.replace(' ','')
        s = s[0]+s[1:][n:]+'0'*n
        return ' '.join([s[:4],s[4:]])

    def __rshift__(self,n):    #>>
        if self.n<<n>127 or self.n<<n<-128:
            raise ValueError('The result %d > 127 or %d <-128'%(self.n>>n,self,n>>n))
        s = self.complemental_code.replace(' ','')
        s = s[0]+s[0]*n+s[1:][:(7-n)]
        return ' '.join([s[:4],s[4:]])

    @complemental_code.setter
    def complemental_code(self,code):
        code = code.replace(' ','')
        if len(code)!=8:
            raise ValueError('code must be a bin string with length 8')
        if code[0]=='0':
            self.n=reduce(lambda x,y:x*2+y,map(int,code))
        else:
            self.n=reduce(lambda x,y:x*2+y,map(int,code))-256

def main():
    s = input('请输入位计算表达式(只支持8位,支持^|&<<>>运算)：')
    res = re.match(r'(.*)(\^|&|\||<<|>>)(.*)',s)
    argv1, opr, argv2 = res.groups()
    try:
        bin1 = Bin(int(argv1))
        bin2 = Bin(int(argv2))
        assert(opr in ('^','|','&','<<','>>'))
    except:
        print('请输入正确的计算表达式!')
        return
    print('计算开始...')
    print('#'*20)
    print('%s 原码：%s'%(argv1,bin1.true_code))
    print('%s 反码：%s'%(argv1,bin1.complement_code))
    print('%s 补码：%s'%(argv1,bin1.complemental_code))
    if opr not in ('>>',"<<"):
        print('#'*20)
        print('%s 原码：%s'%(argv2,bin2.true_code))
        print('%s 反码：%s'%(argv2,bin2.complement_code))
        print('%s 补码：%s'%(argv2,bin2.complemental_code))
    print('#'*20)
    print('%s %s %s...'%(argv1,opr,argv2))
    if opr not in ('>>',"<<"):
        print('%s %s %s...'%(bin1.complemental_code,opr,bin2.complemental_code))
    res = eval('bin1 %s bin2'%opr) if opr not in ('>>',"<<") else eval('bin1 %s int(argv2)'%opr)
    print('#'*20)
    print('结果补码是:',res)
    ret = Bin()
    ret.complemental_code=res
    print('结果反码是:',ret.complement_code)
    print('结果原码是:',ret.true_code)
    print('结果是: ',ret.n)

if __name__=='__main__':
    while True:
        main()