tars1=[*range(8,10,1)]
tars2=[*range(4,8,1)]
tars3=[*range(-1,4,1)]
ft=3
st=7
tt=9
fdt=0
def singdowntar(a):
    last1digi=(abs(a)%10)
    fist1digi=a//10
    
    if last1digi in tars1:
    	fdt=str(fist1digi)+str(st)
    	return(fdt)
    elif last1digi in tars2:
    	fdt=str(fist1digi)+str(ft)
    	return(fdt)
    elif last1digi in tars3:
    	
    		fist1digi=fist1digi-1
    		fdt=str(fist1digi)+str(tt)
    		return(fdt)
    	#else:
    		#fdt=str(fist1digi)+str(tt)
    		#return(fdt)