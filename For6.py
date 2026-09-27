import numpy as np

price = float(input("введите цену "))

for i in np.arange(1.2, 2, 0.2):
    curr = price * round (i,2)
    print(curr)
