"""
Same as snr.py

"""
import numpy as np
import pickle,gzip,glob
import sys
from scipy.optimize import curve_fit
from pylab import *
# assuming c has to be 0
def fit_func(x,a,b): 
	return a*(x-b)**2

ff = sys.argv[1]
data = pickle.load(gzip.open('%s'%(ff)))
results = data['results']
mass = lnlike = np.zeros(len(results.keys())-1)
res_arr = np.zeros( (len(results.keys())-1,2) )
cnt =0
for key in sorted( results.keys() ):
	if float(key)!= 5.:
		res_arr[cnt,0] = float(key)
		res_arr[cnt,1] = float(results[key])
		cnt += 1


mass = np.asarray( res_arr[:,0] );lnlike = np.asarray( res_arr[:,1] );best_fit = mass[np.argmax(lnlike)];delta_chisq = 2*(max(lnlike)-lnlike);inds = np.where(delta_chisq<2)[0]

params = curve_fit(fit_func,mass[inds],delta_chisq[inds],p0=[1,best_fit])[0]
m_ip = np.arange(min(mass[inds]),max(mass[inds]),0.01);res_ip = fit_func(m_ip,params[0],params[1]);linds, uinds = np.where(m_ip<=best_fit)[0], np.where(m_ip>=best_fit)[0];req_val =1
l_err = np.interp(req_val,res_ip[linds][::-1], m_ip[linds][::-1]);u_err = np.interp(req_val,res_ip[uinds], m_ip[uinds]); width = u_err - l_err
print "mass uncen = %s"%(width/2.)
plot(mass,delta_chisq,'k');plot(m_ip,res_ip,'r');show()


