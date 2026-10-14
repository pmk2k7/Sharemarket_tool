trad7=[*range(-1,11,1)]
trad1=[*range(11,31,1)]
trad2=[*range(31,46,1)]
trad3=[*range(46,56,1)]
trad4=[*range(56,71,1)]
trad5=[*range(70,91,1)]
trad6=[*range(90,100,1)]
f=10
ft=30
st=45
tt=55
fft=70
sst=90
def doubledowntar(a):
    last1digi=(abs(a)%100)
    fist1digi=a//100
    if last1digi in trad1:
        f1t=str(fist1digi)+str(f)
        return(f1t)
    elif last1digi in trad2:
        f2t=str(fist1digi)+str(ft)
        return(f2t)
    elif last1digi in trad3:
        f3t=str(fist1digi)+str(st)
        return(f3t)
    elif last1digi in trad4:
        f4t=str(fist1digi)+str(tt)
        return(f4t)
    elif last1digi in trad5:
        f5t=str(fist1digi)+str(fft)
        return(f5t)
    elif last1digi in trad6:
        fst=str(fist1digi)+str(sst)
        return(fst)
    elif last1digi in trad7:
        fist1digi=fist1digi-1
        fst=str(fist1digi)+str(sst)
        return(fst)