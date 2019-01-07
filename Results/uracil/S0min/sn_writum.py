from sys import argv, stdout

def read_file( fd ):
    s0 = 0
    n0 = {}
    E0 = {}
    sn = 0
    nn = {}
    En = {}
    E1 = {}
    f1 = {}
    E2 = {}
    f2 = {}
    ios = 0
    ios1 = 0
    ios11 = 0    
    ios2 = 3
    ios22 = 0
    lineit = iter(fd)
    for line in lineit:
        if '   EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:
            s0 += 1
            for i in range(3):
                curline = next(lineit)
                if 'LinDepThresh=1.00e-15' in curline:
                    for j in range(3):
                        curline = next(lineit)
                    n0[s0-1] = int(curline.split()[0])
                    for i in range(4):
                        next(lineit)
                    conv = int(next(lineit).split()[1])
                    while conv != n0[s0-1]:
                        curline = next(lineit)
                        if 'complex' in curline :
                            curline = next(lineit)
                        conv = int(curline.split()[1])
                        if conv == n0[s0-1]:
                            E0[s0-1] = {}
                            for i in range(conv):
                                e = curline.split()[4+i]
                                e = e[:-1]
                                E0[s0-1][i] = e

        if 'CVS-EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:
            sn += 1
            for i in range(3):
                curline = next(lineit)
                if 'LinDepThresh=1.00e-15' in curline:
                    for j in range(3):
                        curline = next(lineit)
                    nn[sn-1] = int(curline.split()[0])
                    for i in range(4):
                        next(lineit)
                    conv = int(next(lineit).split()[1])
                    while conv != nn[sn-1]:
                        curline = next(lineit)
                        if 'complex' in curline :
                            curline = next(lineit)
                        conv = int(curline.split()[1])
                        if conv == nn[sn-1]:
                            En[sn-1] = {}
                            for i in range(conv):
                                e = curline.split()[4+i]
                                e = e[:-1]
                                En[sn-1][i] = e
            for j in range(len(En)):
                E1[j] = {}
                f1[j] = {}
                for k in range(len(En[j])):
                    E1[j][k] =  float(En[j][k]) - float(E0[0][0])
                    f1[j][k] =  0.0
    
            for j in range(len(En)):
                E2[j] = {}
                f2[j] = {}
                for k in range(len(En[j])):
                    E2[j][k] = float(En[j][k]) - float(E0[1][0]) 
                    f2[j][k] = 0.0 

        if 'State A: eomee_ccsd/rhfref/singlets: 1/A\'' in line:
            if 'State B: cvs_eomee_ccsd/rhfref/singlets: ' in next(lineit):
                for i in range(4):
                    curline = next(lineit)
                if (ios < len(E1[0])):
                    f1[0][ios1] = float(curline.split()[3])
                    ios1+=1
                elif (ios < ( len(E1[1]) + len(E1[0]) ) ):
                    f1[1][ios11] = float(curline.split()[3])
                    ios11+=1  
                ios+=1             

        if 'State A: eomee_ccsd/rhfref/singlets: 1/A"' in line:
            if 'State B: cvs_eomee_ccsd/rhfref/singlets: ' in next(lineit):
                for i in range(4):
                    curline = next(lineit)
                if (ios2 < (len(E2[0]) )):
                    f2[0][ios2] = float(curline.split()[3])
                elif (ios2 < ( len(E2[1]) + len(E2[0]) ) ):
                    f2[1][ios22] = float(curline.split()[3])
                    ios22+=1  
                ios2+=1  

    print(E1)
    print(E2)
    print("S2")
    for a in range(len(E1)):
        for b in range (len(E1[a])):
            print (E1[a][b],  f1[a][b]) 
    print("S1")
    for a in range(len(E2)):
        for b in range (len(E2[a])):
            print (E2[a][b],  f2[a][b])

if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)