#!/usr/env python

from sys import argv, stdout
import sys
import numpy as np
from pylab import *

def lorentz(omega, exci, sigma,forza):
    grecopi=3.14159265358979323846264338327950288
    return (sigma*forza)/(grecopi*((omega-exci)**2+sigma**2))

def gaussian(omega, exci, gamma,forza):
    grecopi=3.14159265358979323846264338327950288
    return (forza/(exci*gamma*sqrt(2*grecopi))*exp(-(omega-exci)**2/(2*gamma**2)))*0.02

def Mgaussian(omega, exci, sigma,weight):
    grecopi=3.14159265358979323846264338327950288
    fact=1.0/(sigma*sqrt(2*grecopi))
    #fact=1.0/(exci*sigma*sqrt(2*grecopi))
    func=fact*exp(-(omega-exci)**2/(2*sigma**2))
    return weight*func

def read_file( fd ):

        data = np.genfromtxt(fd)
        exci_SD1 = data[:,0] 
        fCCSD1 = (data[:,1])
        exci_auSD1=exci_SD1*(1.0/27.2114)

        #sigma=0.021207
        #sigma=0.5/(2*sqrt(2*(log(2))))
        #sigma=0.4/(2*sqrt(2*(log(2))))
        gamma = 0.4 #eV
        sigma = gamma/2
        #sigma = sigma*(1.0/27.2114)
        #sigma=0.0125
        n=len(exci_auSD1)
        for i in range(0,n,1):
           fCCSD1[i] = fCCSD1[i]#*3/(2*exci_auSD1[i])

        step = 0.01
#        omega = np.arange(525,550,step) #O3
#        omega = np.arange(525,550,step) #CO_O
#        omega = np.arange(280,300,step) #CO_C
#        omega = np.arange(800,900,step) #Ne
#        omega = np.arange(530,575,step) #water
#        omega = np.arange(400,410,step) #NH3
#        omega = np.arange(270,300,step) #C2H4
#        omega = np.arange(280,295,step) #CH2CHF
        omega = np.arange(680,700,step) #CH2CHF F-edge
#        omega = np.arange(285,295,step) #adenine_C
#        omega = np.arange(398,407,step) #adenine_N
       # omega = omega/27.2114
        speCCSD1 = []

        for i in range(0, len(omega), 1):
               speCCSD1.append(0.0)
#                speCCSDM.append(0.0)
        for i in range(0, len(exci_SD1), 1):
            for n in range(0, len(omega), 1):
#               speCCSD1[n]=speCCSD1[n]+omega[n]*gaussian(omega[n],exci_auSD1[i],hwhm,fCCSD1[i])
#                speCCSDM[n]=speCCSDM[n]+Mgaussian(omega[n],exci_SD1[i],sigma,fCCSD1[i])*omega[n]
                #speCCSDM[n]=speCCSDM[n]+Mgaussian(omega[n],exci_SD1[i],sigma,fCCSD1[i])*step
#                speCCSD1[n]=speCCSD1[n]+lorentz(omega[n],exci_auSD1[i],sigma,fCCSD1[i])*step
                speCCSD1[n]=speCCSD1[n]+lorentz(omega[n],exci_SD1[i],sigma,fCCSD1[i])

#       omega=omega*27.2114 #-(287.385-286.546)

        for i in range(0, len(omega), 1):
#            print omega[i]*27.2114, speCCSD1[i]#/(omega[i]*27.2114)
            print omega[i], speCCSD1[i]#/(omega[i]*27.2114)
#        n=len(exci_auSD1)
#        for i in range(0, n, 1):
#            print exci_SD1[i], fCCSD1[i]

        #for i in xrange (nexc):
        #        print energy[i], f[i]


if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)

