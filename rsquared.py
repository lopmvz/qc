#!/usr/env python

from sys import argv, stdout

def read_gs_density (fd):
    lineit = iter(fd)
    r2_gs_au2 = {}
    xx_gs_au2 = {}
    yy_gs_au2 = {}
    zz_gs_au2 = {}
    s = 0
    for line in lineit:
        if 'Reference state properties' in line:
            gs_au2 = {}
        if 'R-squared (a.u.):' in line:
            
            tmp = line.split()[4]
            gs_au2[0] = float(tmp[:-1])
            tmp = line.split()[6]
            gs_au2[1] = float(tmp[:-1])
            tmp = line.split()[8]
            gs_au2[2] = float(tmp[:-1])
            gs_au2[3] = float(line.split()[2])

            
    return gs_au2


def read_state(fd):
    lineit = iter(fd)
    state = []
    s = 0
    for line in lineit:
        if 'Excited state properties for  CVS-EOMEE-CCSD transition' in line:
            state.append(line.split()[6])
            s+=1
    return state

def read_ee_density(fd):
    lineit = iter(fd)
    r2_ee_au2 = {}
    xx_ee_au2 = {}
    yy_ee_au2 = {}
    zz_ee_au2 = {}
    ee_au2 = {}
    s = 0
    for line in lineit:
        if 'Excited state properties for  CVS-EOMEE-CCSD transition' in line:
            ee_au2[s] = {}
        if 'R-squared (a.u.):' in line:
            r2_ee_au2[s] = float(line.split()[2])
            
            tmp = line.split()[4]
            xx_ee_au2[s] = float(tmp[:-1])
            tmp = line.split()[6]
            yy_ee_au2[s] = float(tmp[:-1])
            tmp = line.split()[8]
            zz_ee_au2[s] = float(tmp[:-1])

            ee_au2[s][0] = xx_ee_au2[s]
            ee_au2[s][1] = yy_ee_au2[s]
            ee_au2[s][2] = zz_ee_au2[s]
            ee_au2[s][3] = r2_ee_au2[s]

            s += 1
    return ee_au2


if __name__ == '__main__':
    with open('CH2CHF_Pbs_r2.out','r') as fd:
        gs_au2 = read_gs_density(fd)
    with open('CH2CHF_ee_Pbs_r2.out','r') as fd:
        state = read_state (fd)
    with open('CH2CHF_ee_Pbs_r2.out','r') as fd:
        ee_au2 = read_ee_density(fd)

    Delta_ee_gs_au2 = {}
    Delta_ee_gs_ang2 = {}
    for s in range(len(ee_au2)):
        print(state[s])
        Delta_ee_gs_au2[s] = {}
        Delta_ee_gs_ang2[s] = {}
        for i in range(len(ee_au2[s])): 
            Delta_ee_gs_au2[s][i] = ee_au2[s][i]-gs_au2[i]
            Delta_ee_gs_ang2[s][i] = Delta_ee_gs_au2[s][i]*0.529177**2
        print ('&', "{0:.2f}".format(Delta_ee_gs_ang2[s][0]), '&', "{0:.2f}".format(Delta_ee_gs_ang2[s][1]), '&', "{0:.2f}".format(Delta_ee_gs_ang2[s][2]), '&', "{0:.2f}".format(Delta_ee_gs_ang2[s][3]))
