list=raw_input().split()
dict={0:0,1:0,2:0}
print dict[0]
for x in list:
    if int(x)==0:
		dict[0] = dict.get(0)+1
    if int(x)==1:		
		dict[1] = dict.get(1)+1
    if int(x)==2:
	       dict[2] = dict.get(2)+1
print dict
result=[]
for x in range(dict[0]):
    result.append(0)
for x in range(dict[1]):	
    result.append(1)
for x in range(dict[2]):
    result.append(2)
for x in result:	
    print "Value is ",x	
		
