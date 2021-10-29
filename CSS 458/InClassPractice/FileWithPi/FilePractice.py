import math

fobj2 = open ('AngleSineCosine.txt', 'w')
i = 0
while i < math.pi:
    sine = format(math.sin(i), '.5')
    
    # in angle
    fobj2.write('angle: ')
    fobj2.write(format(str(i), '.5') + '\t\t')
    
    # in sin
    fobj2.write('sin: ')
    fobj2.write(str(sine) + '\t\t')
    
    # in cos
    fobj2.write ('cos: ')
    fobj2.write(str(format(math.cos(i), '0.5')) + '\t\t' + '\n')
    i += 0.1
    
fobj2.close()