import math
AB = int(input())
BC = int(input())
AC = math.sqrt(AB**2 + BC**2)
MCB = math.asin(BC/AC)*(180/math.pi)
MBC = (180 - 90 - MCB)
if MBC - round(MBC) < 0.5:
    print(round(MBC),chr(176),sep="")
elif MBC - round(MBC) == 0.5:
    print(math.ceil(MBC),chr(176),sep="")
else:
    print(round(MBC),chr(176),sep="")