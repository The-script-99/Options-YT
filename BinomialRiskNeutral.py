#Enter data
priceSec = 50
priceUp = 2
priceDown = 1/2
time = 2
intrest = 0.25
strike = 50

def getCallRisk(p,t,pUp,pDown,intrest,strike):

    values = getOutcomes(t,pUp,pDown,p)
    values = setSubOptionValue(values,strike)

    if((pDown/p>0 and pDown/p<1+intrest) and 1+intrest<pUp/p):
        return "N/A. 0<d<1+r<u"
    
    if(len(values)>1):
        i = len(values)-2
        while i>=0:
            j = 0
            l = []
            while j<len(values[i]):
                l.append(getValueRisk(pUp,pDown,values[i+1][j*2],values[i+1][j*2+1],intrest))
                j+=1
            values[i] = l
            i-=1
    return getValueRisk(pUp,pDown,values[0][0],values[0][1],intrest)

#returns all possible states
def getOutcomes(time,stepUp,stepDown,price):
    outcomes = []

    i = 1
    while i<=time:
        if(i==1):
            outcomes.append(getSubOutcomes(stepUp,stepDown,price))
            i+=1
            continue
        list = []
        for x in outcomes[i-2]:
            for y in getSubOutcomes(stepUp,stepDown,x):
                list.append(y)
        
        outcomes.append(list)
        i+=1
    
    return outcomes

#returns next two possible states
def getSubOutcomes(stepUp,stepDown,price):
    
    list = []

    i = 1
    j = 1
    z = i
    y = 0
    while j<=pow(2,i):
        x = price * pow(stepUp,z)*pow(stepDown,y)
        z -= 1
        y += 1
        j += 1
        list.append(x)

    return list

#sets value of the last vector for Call
def setSubOptionValue(out,strike):
    
    list = []
    p = 0
    for x in out[len(out)-1]:
        p = x-strike
        if(p<0):
            list.append(0)
            continue
        list.append(p)
    out = out*1
    out[len(out)-1] = list

    return out

#returns value of an option with risk neutral probabilities
def getValueRisk(pUp,pDown,vUp,vDown,i):

    u = pUp
    d = pDown
    p = (1+i-d)/(u-d)
    q = (u-1-i)/(u-d)

    v = (p*vUp+q*vDown)/(1+i)
    if(v<0):
        return 0

    return v

getCallRisk(priceSec,time,priceUp,priceDown,intrest,strike)