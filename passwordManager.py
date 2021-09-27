key = input("Enter your Master Key: ")
app = input("Enter the name of the App: ")
alpS = 'abcdefghijklmnopqrstuvwxyz'
alpC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
syb = '@#$&*()_+'
num = '123456789'
all = alpS , syb , alpC, num

def equalizeString(a,b):
    if len(a) > len(b):
        dif = len(a)-len(b)
        cut = b[0:dif]
        b += cut if len(cut) == dif else cut * (int(dif/len(cut)))

    elif len(b) > len(a):
        dif = len(b)-len(a)
        cut = a[0:dif]
        a += cut if len(cut) == dif else cut * (int(dif/len(cut)))
    return (a,b)


def interlace(a, b):
    a,b = equalizeString(a,b)
    st = ''
    for i in range(len(a)-1):
        st += b[i]+a[i]
    return st


def turnToAscii(a):
    asc = ''
    for i in range(len(a)):
        asc += str(ord(a[i]))
    return asc

def _encode(code):
    global all,syb,alpS,alpC,key
    if len(code)%3 != 0:
        code+=code[0:3-int(len(code)%3)]
    pwd = ''
    for i in range(1,int(len(code)/3)):
        cursor = code[3*(i-1):3*i]
        i1 = int(cursor[0])
        i2 =  int(cursor[1:])
        i1 = int(3 * (i1/9))
        lst = all[i1]
        i2 = int(len(lst)*i2/99)
        pwd += lst[i2-1]

    symFlag = [i for i in syb if i in pwd]
    alpcFlag = [i for i in alpC if i in pwd]
    alpsFlag = [i for i in alpS if i in pwd]
    numFlag = [i for i in num if i in pwd]
    if symFlag != [] and alpcFlag != [] and alpsFlag != [] and numFlag != []:
        return pwd
    else:
        return _encode(turnToAscii(interlace(key, pwd)))

def encode(s):
    hash = turnToAscii(interlace(key, s))
    return _encode(hash)



print(encode(app))
input()