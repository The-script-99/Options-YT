from decimal import Decimal 

#Enter data
priceSec = 50
priceUp = 2
priceDown = 1/2
time = 1000
intrest = 0.25
strike = 50

#returns the value of a Call option by using the risk neutral probabilities and Pascal triangle to speed up the process.
def getCallRiskPascal(price,t,u,d,intrest,strike):

    p = (1+intrest-d)/(u-d)
    q = 1-p
    i,j = t,0
    row = getRow(t)
    print(row)
    value = 0

    if(not(0<d<1+intrest<u)):
        return "N/A. 0<d<1+r<u"

    for x in row:
        x = Decimal(x)
        v = price*pow(u,i)*pow(d,j)
        v = v-strike
        
        if(v>0):
            v = Decimal(v*pow(p,i)*pow(q,j))
            o = Decimal(v*x)
            de = Decimal(pow(1+intrest,t))
            o = o/de
            value = value + o
        j+=1
        i-=1

    return value

#returns the N row of a Pascal triangle
def getRow(N):

    l = []
    prev = 1
    l.append(prev)

    for i in range(1, N + 1):
        curr = (prev * (N - i + 1)) // i
        l.append(curr)
        prev = curr

    return l

print(getCallRiskPascal(priceSec,time,priceUp,priceDown,intrest,strike))