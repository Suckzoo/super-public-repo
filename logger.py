import vessl
import math

vessl.init()
for i in range(100):
    s = math.sin(2*math.pi*i/100)
    vessl.log({
        'sin_thing': 100*s*s,
        'linear_thing': i,
        'exp_thing': 100*(1-math.exp(-i/30)),
    })
