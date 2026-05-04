import numpy as np
import matplotlib.pyplot as plt
from photonprops.two_level_system.tls import twolevel_system_pulses

tau1 = 2.4  # pulse duration in ps
tau2 = 3.04
area1 = 22.65*np.pi  # pulse areas
area2 = 19.19*np.pi
det1 = -8.0  # detunings in meV
det2 = -19.164
delay = 0  # no delay between pulses

lifetime = 100  # exciton lifetime
t_end = 30  # end time for simulation in ps

x, p_gx, t = twolevel_system_pulses(dt_1=0.02, tau1=tau1, area1=area1, det1=det1, tau2=tau2, area2=area2, det2=det2, gamma_e=1/lifetime, delay=delay, tend=t_end)

plt.plot(t,x,label='x')  # excited state population
plt.plot(t,np.abs(p_gx),label='p_gx')  # polarization, absolute value, as it can be complex
plt.xlabel("time in ps")
plt.ylabel("population")
plt.legend()
plt.show()
