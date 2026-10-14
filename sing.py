tars1=[*range(0,3,1)]
tars2=[*range(3,7,1)]
tars3=[*range(7,10,1)]
ft=3
st=7
tt=9
fdt=0
def singtar(a):
    last1digi=(abs(a)%10)
    fist1digi=a//10
    if last1digi in tars1:
        f1t=str(fist1digi)+str(ft)
        return(f1t)
    elif last1digi in tars2:
        f2t=str(fist1digi)+str(st)
        return(f2t)
    elif last1digi in tars3:
        if last1digi==9:
            f3t=a+4
            return(f3t)
        else:
            f3t=str(fist1digi)+str(tt)
            return(f3t)


    