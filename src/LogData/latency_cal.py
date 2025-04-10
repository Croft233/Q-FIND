import copy,time
import matplotlib.pyplot as plt
import numpy as np

# with ec
# is_ec = 1
# hops = 2
# x=[0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
# ec = 24.43
# original_link = [5.3083992,  6.07580185, 5.59616566, 7.14322805, 6.94592953, 7.71859407,
#  9.18097496, 8.12281609, 8.86528492]
# new_link = [ 5.3083992,   6.07678413,  8.51039886, 14.89730358, 18.5106349,  26.44520998,
#  30.13351202, 30.22016764, 34.94460583]

# is_ec = 1
# hops = 1
# x=[0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
# ec = 24.43
# original_link = [5.67520618, 7.08653688, 5.92849493, 5.9567976,  5.51722765, 6.91407204,
#  7.08954096, 7.65491724, 7.35997915]
# new_link = [ 5.67520618,  7.08653688,  5.92849493,  5.9567976,   6.5391469,  13.03269148,
#  15.86521864, 23.07266712, 26.82850838]
# latency_ori = [0,0,0,0,0,0,0,0,0]
# latency_new = [0,0,0,0,0,0,0,0,0]

# without ec
# is_ec = 0
# hops = 1
# x=[0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
# ec = 24.43
# original_link = [6.0625155,  6.45352149, 6.25528407, 6.77867937, 6.62847376, 7.0923779,
#  7.25382829, 7.15336156, 7.25769401]
# new_link = [ 6.06148791,  7.57188272, 13.38977981, 16.29068351, 20.76609254, 24.51492023,
#  24.87391829, 25.50157881, 25.34362841]
# latency_ori = [0,0,0,0,0,0,0,0,0]
# latency_new = [0,0,0,0,0,0,0,0,0]

is_ec = 0
hops = 1
x=[0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
ec = 24.43
original_link = [8.28255415, 8.92043209, 8.40971661, 8.51647043, 8.53306627, 8.46613622,
 8.44727349, 8.46370387, 8.0644412 ]
new_link = [28.09543586, 33.2097919,  32.68446445, 33.97753406, 32.89957309, 34.48005939,
 35.45191002, 34.88105774, 32.80595851]
latency_ori = [0,0,0,0,0,0,0,0,0]
latency_new = [0,0,0,0,0,0,0,0,0]

if is_ec == 1:
    for i in range(len(x)):
        latency_ori[i] = original_link[i] + (ec*hops)
        latency_new[i] = new_link[i] + (ec*hops)
else:
    for i in range(len(x)):
        latency_ori[i] = original_link[i]
        latency_new[i] = new_link[i]

fig = plt.figure()

plt.plot(x, latency_ori, color='red')
# plt.plot(x, [], color='green')
plt.plot(x, latency_new, color='black')
plt.title("")
plt.xlabel('fth')
plt.ylabel('expect latency')
plt.show()