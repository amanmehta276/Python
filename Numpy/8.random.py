import numpy as np

rng=np.random.default_rng()

# seed for repeated and same values
# rng.integers(low,high,size)

# print(np.random.uniform())
# print(rng.integers(1,7,(3,2)))

# print(np.random.uniform(-1,1,(3,2)))

f=np.array(["Apple","Pear"])

f=rng.choice(f,(2,2))

print(f)