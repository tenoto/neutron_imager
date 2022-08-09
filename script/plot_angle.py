#!/usr/bin/env python

import numpy as np 
import pandas as pd
#import ephem
import matplotlib.pylab as plt 

Rmoon = 1738 #km
d_min = 10
d_max = 2000.0
d_nbin = 1990
altitude = np.linspace(0,d_max,d_nbin)
theta_moon = np.degrees(2.0*np.arcsin(Rmoon/(Rmoon+altitude)))
size_100km_on_moon = 100 # km
resolution_100km_moon = np.degrees(size_100km_on_moon/(Rmoon+altitude))
size_10km_on_moon = 10 # km
resolution_10km_moon = np.degrees(size_10km_on_moon/(Rmoon+altitude))

pixel_size = 6 # mm 
pixel_number = 8 
detector_size = pixel_number * pixel_size
print(detector_size)
mask_size = 2 * detector_size
focal_length = 30 # mm 
angular_resolution = np.sqrt(5)*pixel_size/focal_length
full_field_ov_view = np.degrees(np.arctan(detector_size/2.0/focal_length))
partical_field_ov_view = np.degrees(np.arctan((detector_size+mask_size)/2.0/focal_length))
print(partical_field_ov_view)
print(full_field_ov_view)
print(angular_resolution)

fig = plt.figure(figsize=(11.69,8.27),tight_layout=True)
plt.rcParams["mathtext.fontset"] = "dejavuserif"	
plt.rcParams["font.size"] = 14
plt.rcParams["font.family"] = "serif"
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8

plt.axhline(full_field_ov_view,ls='-',color='r',label='Full FoV (%.1f deg)'%full_field_ov_view )
plt.axhline(partical_field_ov_view,ls='-.',color='r',label='Partical FoV')
plt.axhline(angular_resolution,ls='--',color='r',label='Angular resolution')

plt.plot(altitude,theta_moon, color='k',ls='-',lw=2,label="Moon diameter")
plt.plot(altitude,resolution_100km_moon, color='k',ls='--', lw=2,label="100 km on the moon")
plt.plot(altitude,resolution_10km_moon, color='k',ls='-.', lw=2,label="10 km on the moon")
plt.tight_layout(pad=2)
plt.xlabel(r"Altitude from the lunar surface (km)", labelpad=18)
plt.ylabel(r"Angular diameter (degree)", labelpad=18)
plt.xlim(0,d_max)
plt.yscale('log')
title  = 'Imager design\n'
title += 'pixel size = %.1f mm\n' % pixel_size
title += 'number of pixel = %dx%d\n' % (pixel_number,pixel_number)
title += 'detector size = %.1f mm\n' % detector_size
title += 'mask rize = %.1f mm\n' % mask_size
title += ' (pediodic)\n'
title += 'focal length = %.1f mm\n' % focal_length
plt.legend(bbox_to_anchor=(1.05, 1.0),loc='upper left',title=title)

plt.tick_params(axis="both", which='major', direction='in', length=8)
#plt.tick_params(axis="both", which='minor', direction='in', length=5)
plt.grid(True,which='major',linestyle='-')
#plt.minorticks_on()

plt.savefig('angular_evaluation.pdf')