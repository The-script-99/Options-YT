priceSec = 50
priceUp = 2
priceDown = 1/2
intrest = 0.25
strike = 50
time = 20

#return value of an option with replicating portfolio 
def getOptionValue(p,t,pUp,pDown,intrest,strike):

    outcomes = getOutcomes(t,pUp,pDown,p)
    print(outcomes)
    values = setSubOptionValue(outcomes,strike)
    print(values)

    if((pDown/p>0 and pDown/p<1+intrest) and 1+intrest<pUp/p):
        return "N/A. 0<d<1+r<u"

    if(len(values)>1):
        i = len(values)-2
        while i>=0:
            j = 0
            l = []
            while j<len(values[i]):
                l.append(getValue(outcomes[i][j],outcomes[i+1][j*2],outcomes[i+1][j*2+1],values[i+1][j*2],values[i+1][j*2+1],intrest))
                j+=1
            values[i] = l
            i-=1
    print(values)
    return getValue(p,outcomes[0][0],outcomes[0][1],values[0][0],values[0][1],intrest)

#returns the value of sub branch
def getValue(p,pUp,pDown,vUp,vDown,i):
    value = 0

    #price parameters
    delta = (vUp-vDown)/(pUp-pDown)
    bond = (vDown-delta*pDown)/(1+i)
    
    value = delta*p+bond

    if(value<0):
        return 0

    return value

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

getOptionValue(priceSec,time,priceUp,priceDown,intrest,strike)