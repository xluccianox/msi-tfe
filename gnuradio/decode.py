import scipy
import matplotlib.pyplot as plt
import numpy as np

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
samples = scipy.fromfile(open("file9_0_0.00034800.dat"), dtype=scipy.uint32)

# print(samples[0:1000])

samples = (samples > 0) * 1

prev = 1
prev_cant = 0
for s in samples:
    if (s != prev):
        print(prev, prev_cant)
        prev_cant = 0
        prev = s
    else:
        prev_cant = prev_cant + 1


grouped_samples= list(chunks(samples[37:], 17))

downsampled = []
for i,s in enumerate(grouped_samples):
    downsampled.append(np.bincount(s).argmax()) 

print(''.join(map(str, downsampled)))

# plt.plot(samples)
plt.plot(samples[37:])
plt.show()


# # print(np.mean(samples.reshape(-1, 16), axis=1))

# #  downsampled.append(np.bincount(samples.slice(i, )).argmax())

# plt.plot(downsampled)
# plt.show()

