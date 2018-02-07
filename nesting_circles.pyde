psize = 500
center = 500/2
rad = 10
R = 250
xc=250
yc=250
num=3

def setup():
    size(psize, psize)
    noStroke()
    
def draw():
    #first layer deep
    background(0)
    fill(168,143,248)
    ellipse(center, center, width, height)
    #second layer deep
    r=(.7*R/500)*(height-mouseY)
    for i in range(num):
        theta = 2*PI*i/float(num)
        degreesRotated = (2*PI/500)*mouseX
        initRotation = (2.1/4)
        x = xc+(R-r)*cos(theta+degreesRotated+initRotation)
        y = yc+(R-r)*sin(theta+degreesRotated+initRotation)
        fill(161,207,251)
        ellipse(x,y,2*r,2*r)
        #third layer deep
        R2=r
        r2=(.7*r/500)*(height-mouseY)
        for j in range(num):
            theta = 2*PI*j/float(num)
            degreesRotated = (2*PI/500)*mouseX
            #redefine xc & yc
            x2 = x+(R2-r2)*cos(theta+degreesRotated+initRotation)
            y2 = y+(R2-r2)*sin(theta+degreesRotated+initRotation)
            fill(175,252,240)
            ellipse(x2,y2,2*r2,2*r2)
            #fourth layer deep
            R3=r2
            r3=(.7*r2/500)*(height-mouseY)
            for k in range(num):
                theta = 2*PI*k/float(num)
                degreesRotated = (2*PI/500)*mouseX
                #redefine xc & yc
                x3 = x2+(R3-r3)*cos(theta+degreesRotated+initRotation)
                y3 = y2+(R3-r3)*sin(theta+degreesRotated+initRotation)
                fill(188,122,226)
                ellipse(x3,y3,2*r3,2*r3)
                #fifth layer deep
                R4=r3
                r4=(.7*r3/500)*(height-mouseY)
                for l in range(num):
                    theta = 2*PI*l/float(num)
                    degreesRotated = (2*PI/500)*mouseX
                    #redefine xc & yc
                    x4 = x3+(R4-r4)*cos(theta+degreesRotated+initRotation)
                    y4 = y3+(R4-r4)*sin(theta+degreesRotated+initRotation)
                    fill(237,116,209)
                    ellipse(x4,y4,2*r4,2*r4)
                    #sixth layer deep
                    R5=r4
                    r5=(.7*r4/500)*(height-mouseY)
                    for m in range(num):
                        theta = 2*PI*m/float(num)
                        degreesRotated = (2*PI/500)*mouseX
                        #redefine xc & yc
                        x5 = x4+(R5-r5)*cos(theta+degreesRotated+initRotation)
                        y5 = y4+(R5-r5)*sin(theta+degreesRotated+initRotation)
                        fill(250,241,254)
                        ellipse(x5,y5,2*r5,2*r5)
        
    
    