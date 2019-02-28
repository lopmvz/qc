#!/usr/env python

from sys import argv, stdout

def read_file( fd ):
        lineit = iter(fd)
        energy = {}
        f = {}
        for line in lineit:
                if '.NCCEXC' in line:
                        nexc = int(lineit.next())
                if 'CCSD       Excitation energies' in line:
                        lineit.next()
                        lineit.next()
                        lineit.next()
                        for i in xrange (nexc):
                                energy[i] = lineit.next().split()[5]
                if 'CCSD       Length   Gauge Oscillator Strength' in line:
                        lineit.next()
                        lineit.next()
                        lineit.next()
                        for i in xrange (nexc):
                                f[i] = lineit.next().split()[7]
        for i in xrange (nexc):
                print energy[i], f[i]



if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)
