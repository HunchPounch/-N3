def File(filename):
    inp = open(filename, 'r')

    xa, ya = map(float, inp.readline().split())
    xb, yb = map(float, inp.readline().split())
    xo, yo = map(float, inp.readline().split())
    r = float(inp.readline())
    inp.close()

    if(((xa-xo)**2+(ya-yo)**2<r**2) and ((xb-xo)**2+(yb-yo)**2<r**2)):
        return 0
#----
    if(((xa-xo)**2+(ya-yo)**2<r**2) and ((xb-xo)**2+(yb-yo)**2>r**2)):
        return 1
    
    if(((xb-xo)**2+(yb-yo)**2<r**2) and ((xa-xo)**2+(ya-yo)**2>r**2)):
        return 1

    #if(((xa-xo)**2+(ya-yo)**2==r) and ((xb-xo)**2+(yb-yo)**2>r)):
    #    return 1

    #if(((xa-xo)**2+(ya-yo)**2>r) and ((xb-xo)**2+(yb-yo)**2==r)):
    #    return 1
#-----
    if(((xa-xo)**2+(ya-yo)**2==r**2) and ((xb-xo)**2+(yb-yo)**2<r**2)):
        return 1

    if(((xa-xo)**2+(ya-yo)**2<r**2) and ((xb-xo)**2+(yb-yo)**2==r**2)):
        return 1

    if(((xa-xo)**2+(ya-yo)**2==r**2) and ((xb-xo)**2+(yb-yo)**2==r**2)):
        return 2
#-----

    if(((xa-xo)**2+(ya-yo)**2==r**2) and ((xb-xo)**2+(yb-yo)**2>r**2)):
        
        if(ya>=yo):
            if((xa-xo)*(xb-xa)+(ya-yo)*(yb-ya)>0):
                return 1

        if(ya<=yo):
            if((xa-xo)*(xb-xa)+(ya-yo)*(yb-ya)<0):
                return 1

    if(((xb-xo)**2+(yb-yo)**2==r**2) and ((xa-xo)**2+(ya-yo)**2>r**2)):
        
        if(yb>yo):
            if((xb-xo)*(xa-xb)+(yb-yo)*(ya-yb)>0):
                return 1

        if(ya<yo):
            if((xb-xo)*(xa-xb)+(yb-yo)*(ya-yb)<0):
                return 1  


    

    # если обе точки отрезка вне окружности  
    xba = xb - xa
    yba = yb - ya

    if(yba*(xo-xa)==xba*(yo-ya)):
        if((xa-xo)*(xb-xo)+(ya-yo)*(yb-yo)<=0):
            return 2
        else:
            return 0
    
    # удвоенная площадь треугольника ABO == 2*S
    s_abo = abs((xa-xo)*yba - (ya-yo)*xba)
 
    # квадрат длины отрезка AB
    dab = xba*xba + yba*yba
    if(dab == 0):
        return 0
 
    # высота треугольника ABO из вершины О
    # равна -> h = 2*S/AB
    # сравниваем (2S)^2 и AB^2*R^2
    fun = s_abo*s_abo - r*r*dab
    if fun < 0:
        return 2
    elif fun == 0:
        return 1
    else:
        return 0


def AutoTest1():

    TEST1 = 0
    
    TEST1 = File('TEST1.txt')

    if (TEST1 == 2):
        print("AutoTest1 - passed\n")
        return 1
    else:
        print("AutoTest1 - not passed\n")
        return 0

def AutoTest2():

    TEST2 = 0
    
    TEST2 = File('TEST2.txt')

    if (TEST2 == 0):
        print("AutoTest2 - passed\n")
        return 1
    else:
        print("AutoTest2 - not passed\n")
        return 0

def AutoTest():
    if (AutoTest1() * AutoTest2() == 1):
        print("AutoTests - passed\n")
        return 1
    else:
        print("AutoTests - not passed\n")
        return 0

if (AutoTest() == 1):
    namefile = input("Enter name of file\n")
    answer = File(namefile)

    if(answer >= 0):
        print("Answer - ", answer, "\n")


