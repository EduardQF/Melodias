#--------------------------------------------------------
BANDWIDTH = 20
#A
A= 865#830
#B
B=950
#CM
CM=1000
#C
C=515
#D
D=563#563
#E
E=622#627
#F
F= 690#665
#G
G=750#750

def pitch(thefreq):
    nota=""
    if(thefreq> C - BANDWIDTH and thefreq < C + BANDWIDTH ):
        nota="C"
        print("C")
    elif (thefreq> D - BANDWIDTH and thefreq < D + BANDWIDTH):
        nota="D"
        print("D")
    elif (thefreq> E - BANDWIDTH and thefreq < E + BANDWIDTH):
        nota="E"
        print("E")
    elif (thefreq> F - BANDWIDTH and thefreq < F + BANDWIDTH):
        nota="F"
        print("F")
    elif (thefreq> G - BANDWIDTH and thefreq < G + BANDWIDTH):
        nota="G"
        print("G")
    elif (thefreq> A - BANDWIDTH and thefreq < A + BANDWIDTH):
        nota="A"
        print("A")
    elif (thefreq> B - BANDWIDTH and thefreq < B + BANDWIDTH):
        nota="B"
        print("B")
    elif (thefreq> CM - BANDWIDTH and thefreq < CM + BANDWIDTH):
        nota="CM"
        print("CM")
    else:
        nota = ""
        print("not note")
    return nota
