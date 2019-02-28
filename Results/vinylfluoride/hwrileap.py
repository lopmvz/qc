#!/usr/env python

from sys import argv, stdout

def read_file( fd ):
        lineit = iter(fd)
        E1 = {}
        f1 = {}
        if1 = 0
        jf1 = 0
        sym1 = {} 
        n = {}
        s = 0
        lineit = iter(fd)
        for line in lineit:
                if 'NEXAFS ' in line:
                    bs = line.split()[-1]
                    print (bs)
                if 'Solving for CVS-EOMEE-CCSD' in line:
                        sym1[s] = line.split()[3]
                if 'CVS-EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:
                        for i in range(3):
                            curline = next(lineit)
                            if 'LinDepThresh=1.00e-15' in curline:
                                for j in range(3):
                                    curline = next(lineit)
                        n[s] = int(curline.split()[0])
                        for i in range(4):
                            next(lineit)
                        conv = int(next(lineit).split()[1])
                        while conv != n[s]:
                            curline = next(lineit)
                            if 'complex' in curline:
                                conv = conv
                            else:
                            #    tmpconv = curline.split()[1]
                                conv = int(curline.split()[1])
                                if conv == n[s]:
                                    E1[s] = {}
                                    for i in range(conv):
                                        e = curline.split()[4+i]
                                        e = e[:-1]
                                        E1[s][i] = float(e)
                        s += 1

                if 'Oscillator strength' in line:
                    f1[if1][jf1] = float(line.split()[3])
                    print (f1[if1][jf1])
                    if (jf1 != len(E1[if1])-1):
                      jf1 += 1
                    else:
                      jf1 = 0
                      if1 += 1

        for a in range(len(E1)):
            #print (sym[a])
            for b in range (len(E1[a])):
                if (bs == 'aug-cc-pvtz' or bs =='aug-cc-pVTZ'):
                    print ("&", sym1[a],"&", "{0:.2f}".format(E1[a][b]),"&", "{0:.5f}".format(f1[a][b],5), "\\"+"\\") 
#                   print ("&", sym1[a][0]+ "$_"+ sym1[a][1]+"$","&", "{0:.2f}".format(E1[a][b]),"&", "{0:.4f}".format(f1[a][b],4),  "\\"+"\\")
#                    print ("&", sym1[a][0]+ "$_"+ sym1[a][1]+"$"+ sym1[a][2],"&", "{0:.2f}".format(E1[a][b]),"&", "{0:.4f}".format(f1[a][b],4), "\\"+"\\") 
                else:
                    print ("&", sym1[a],"&", "{0:.2f}".format(E1[a][b]),"&", "{0:.5f}".format(f1[a][b],5))
#                    print ("&", sym1[a][0]+ "$_"+ sym1[a][1]+"$","&", "{0:.2f}".format(E1[a][b]),"&", "{0:.4f}".format(f1[a][b],4))
#                    print("&", sym1[a][0]+ "$_"+ sym1[a][1]+"$"+ sym1[a][2],"&", "{0:.2f}".format(E1[a][b]), "&", "{0:.4f}".format(f1[a][b],4)) 


if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)
