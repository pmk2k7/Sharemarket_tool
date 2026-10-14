trad0=[*range(0,10,1)]
trad1=[*range(10,30,1)]
trad2=[*range(30,45,1)]
trad3=[*range(45,55,1)]
trad4=[*range(55,70,1)]
trad5=[*range(70,99,1)]

f=10
ft=30
st=45
tt=55
fft=70
sst=90
def doubletar(a):
    last1digi=(abs(a)%100)
    fist1digi=a//100
   # print(last1digi)
    if last1digi in trad1:
        f1t=str(fist1digi)+str(ft)
        return(f1t)
    elif last1digi in trad0:
    	f1t=str(fist1digi)+str(f)
    	return(f1t)
    elif last1digi in trad2:
        f2t=str(fist1digi)+str(st)
        return(f2t)
    elif last1digi in trad3:
        f3t=str(fist1digi)+str(tt)
        return(f3t)
    elif last1digi in trad4:
        f4t=str(fist1digi)+str(fft)
        return(f4t)
    elif last1digi in trad5:
    	if last1digi==90:
    		f5t=a+20
    		return(f5t)
    	else:
        	f5t=str(fist1digi)+str(sst)
        	return(f5t)
