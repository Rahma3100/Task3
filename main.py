list = []


def num():
    for i in range( 4 ):
        x = int( input( "Enter Number" ) )
        list.append( x )
        len( list )
    return list


n = num()
print( n )
y = int( input( "Enter divisible Number" ) )
for z in list:
    if z % y ==0:
        print(z)
    else:
        pass

