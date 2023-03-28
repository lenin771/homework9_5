import scipy.stats as status
import numpy as np
import scipy.stats as stats
import pylab

x =np.array([172, 177, 158, 170, 178,175, 164, 160, 169])
y= np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])


print('среднее значение роста матерей', np.mean(x))
print('ско роста матерей', np.std(x, ddof=1))
print()
print('среднее значение роста дочерей', np.mean(y))
print('ско роста дочерей', np.std(y, ddof=1))