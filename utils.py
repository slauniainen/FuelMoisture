# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 13:53:57 2021

@author: 03081268
"""
import pandas as pd
import os
import matplotlib.pyplot as plt

def read_sitedata(ffile, siteid=None):
    """
    returns site data as dataframe. Biomasses are as kg ha-1 dm
    """
    
    dat = pd.read_csv(ffile, sep=';', header='infer')
    #dat.index = dat['ID']
    
    if siteid:
        dat = dat[dat.ID==siteid]
        dat = dat.squeeze()
        
    return dat

def read_forcing(scenario, grid_id, fdate=None, ldate=None):
    """
    returns meteorological data as dataframe
    """
    
    ffile =  os.path.join(r'Data\forcing', 'CanESM2_' + scenario, 'weather_id_' +str(grid_id) + '.csv')
    print(ffile)
    dat = pd.read_csv(ffile, sep=',', header='infer')
    dat = dat.rename(columns={'TAir': 'T', 'Precip': 'Prec', 'global_radiation': 'Rg'})
    dat.Prec  /= 86400.

    if fdate:
        dat = dat[dat['date']>=fdate]
    if ldate:
        dat = dat[dat['date']<=ldate]

    tvec = pd.to_datetime(dat['date'], yearfirst=True)
    dat.index = tvec
    dat.date = tvec
    return dat

#def compstats(res, forc, fdate, ldate):    
#    #%% Run model for pallas P
#
#    doy = forc.doy.values
#    y = 
#
##%%
#fig, ax = plt.subplots(5,1)
#
#ax[0].plot(doy0, res0['N2fix'], 'o', color='b', alpha=0.5)
#ax[0].plot(doy1, res1['N2fix'], '.', color='r', alpha=0.5)
#ax[1].plot(doy0, res0['cN2fix'], '.', color='b', alpha=0.5)
#ax[1].plot(doy1, res1['cN2fix'], '.', color='r', alpha=0.5)
#ax[2].plot(doy0, res0['fT'], '.', color='b', alpha=0.5)
#ax[2].plot(doy1, res1['fT'], '.', color='r', alpha=0.5)
#ax[3].plot(doy0, res0['fw'], '.', color='b', alpha=0.5)
#ax[3].plot(doy1, res1['fw'], '.', color='r', alpha=0.5)
#ax[4].plot(doy0, res0['fw']*res0['fT'], '.', color='b', alpha=0.5)
#ax[4].plot(doy1, res1['fw']*res1['fT'], '.', color='r', alpha=0.5)
#
#fig, ax = plt.subplots(5,1)
#
#ax[0].plot(doy0, forc_present['Tair'], 'o', color='b', alpha=0.5)
#ax[0].plot(doy1, forc_future['Tair'], '.', color='r', alpha=0.5)
#ax[1].plot(doy0, forc_present['Prec'], 'o', color='b', alpha=0.5)
#ax[1].plot(doy1, forc_future['Prec'], '.', color='r', alpha=0.5)
#
#ax[2].plot(doy0, res0['swe'], 'o', color='b', alpha=0.5)
#ax[2].plot(doy1, res1['swe'], '.', color='r', alpha=0.5)
#
#ax[3].plot(doy0, res0['N2fix'], 'o', color='b', alpha=0.5)
#ax[3].plot(doy1, res1['N2fix'], '.', color='r', alpha=0.5)
#
