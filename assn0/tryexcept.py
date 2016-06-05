rawstr = raw_input('enter a number ')

try:
    val = int(rawstr)
except:
    val = -1

if val > 0 :
    print 'greater than zero' , val
else:
    print 'less than zero' , val