priceSec = 50
priceUp = 5
priceDown = 0.1
intrest = 0.1
strike = 10

states = []

states.append(priceSec * priceUp)
states.append(priceSec*priceDown)

values = []

i = 0
while i<2:
    v = states[i]-strike
    if( v > 0):
        values.append(v)
    else:
        values.append(0)
    i = i + 1

delta = (values[0]-values[1])/(states[0]-states[1])

bond = (values[1]-delta*states[1])/(1+intrest)

value = delta*priceSec+bond

print(value)
