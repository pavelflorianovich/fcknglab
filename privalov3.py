from graph import *
canvasSize(500, 700)
windowSize(500, 700)


def sky():
    brushColor(135, 206, 250)
    rectangle(0, 0, 500, 700)


def grass():
    brushColor(60, 179, 113)
    rectangle(0, 330, 500, 700)


# (x1, y1) are coordinates of the left-top edge of the fence
# (x2, y2) are coordinates of the right-bottom edge of the fence


def fence(x1, y1, x2, y2, n):  # n is the number of pickets in the fence
    for i in range(n):
        brushColor(218, 165, 32)
        rectangle(x1 + (x2-x1)*i//n, y1, x1 + (x2-x1)*(i+1)//n, y2)


def house():
    brushColor(238, 180, 40)
    polygon([(295, 370), (395, 400), (425, 370), (375, 285), (333, 309)])
    line(395, 400, 333, 309)
    brushColor(218, 165, 32)
    polygon([(295, 370), (295, 480), (395, 530), (425, 460), (425, 370), (395, 400), (295, 370)])
    line(395, 530, 395, 400)
    brushColor("black")
    changeCoords(circle(0, 0, 14), [(310, 410), (370, 480)])
    chain()


def chain():
    brushColor(218, 165, 32)
    changeCoords(circle(0, 0, 14), [(298, 471), (305, 482)])
    brushColor("grey")
    brushColor(60, 179, 113)
    changeCoords(circle(0, 0, 14), [(296, 482), (302, 492)])
    changeCoords(circle(0, 0, 14), [(293, 492), (300, 504)])
    changeCoords(circle(0, 0, 14), [(291, 503), (301, 516)])
    changeCoords(circle(0, 0, 14), [(275, 514), (295, 523)])
    changeCoords(circle(0, 0, 14), [(260, 517), (278, 524)])
    changeCoords(circle(0, 0, 14), [(250, 518), (263, 525)])
    changeCoords(circle(0, 0, 14), [(243, 515), (252, 535)])
    changeCoords(circle(0, 0, 14), [(223, 525), (244, 530)])
    changeCoords(circle(0, 0, 14), [(209, 528), (224, 533)])


# (x, y) here and further on are the coordinates
# of the left-top edge of the rectangle
# in which the object lies


def dog(x, y, n, a):                 # n is the zoom factor
    brushColor(105, 105, 105)        # a is the parameter of orientation:
    legs(x, y + n*25, n, a)          # 1 for the left-oriented, -1 for the right-oriented dog
    body(x + a*n*7, y + n*15, n, a)
    head(x, y, n, a)


def front_leg(x, y, n, a):
    changeCoords(circle(0, 0, 14), [(x + a*n*6, y), (x + a*n*28, y + n*55)])
    changeCoords(circle(0, 0, 14), [(x, y + n*55), (x + a*n*21, y + n*65)])


def rear_leg(x, y, n, a):
    changeCoords(circle(0, 0, 14), [(x, y), (x + a*n*26, y + n*33)])
    changeCoords(circle(0, 0, 14), [(x + a*n*19, y + n*25), (x + a*n*26, y + n*65)])
    changeCoords(circle(0, 0, 14), [(x + a*n*9, y + n*65), (x + a*n*26, y + n*73)])


def legs(x, y, n, a):
    penSize(0)
    front_leg(x - a*n*5, y + n*9, n, a)
    front_leg(x + a*n*34, y + n*30, n, a)
    rear_leg(x + a*n*82, y - n*14, n, a)
    rear_leg(x + a*n*118, y + n*13, n, a)


def body(x, y, n, a):
    penSize(0)
    changeCoords(circle(0, 0, 14), [(x + a*n*70, y), (x + a*n*130, y + n*37)])
    changeCoords(circle(0, 0, 14), [(x, y), (x + a*n*90, y + n*50)])


def head(x, y, n, a):
    penSize(1)
    rectangle(x + a*n*8, y, x + a*n*58, y + n*50)
    changeCoords(circle(0, 0, 14), [(x, y), (x + a*n*12, y + n*16)])
    changeCoords(circle(0, 0, 14), [(x + a*n*54, y), (x + a*n*66, y + n*16)])
    brushColor("white")
    polyline([(x + a*n*16, y + n*30), (x + a*n*24, y + n*37), (x + a*n*33, y + n*36), (x + a*n*42, y + n*37), (x + a*n*50, y + n*30)])
    brushColor("black")
  
# main part of the doc
sky()
grass()

z0=10
while z0<300:
    fence(100, z0, 500, z0 + 20, 20)
    z0+=20
z1=170
while z1<370:
    fence(0, z1, 260, z1 + 13, 20)
    z1+=13
z2=200
while z2<390:
    fence(240, z2, 500, z2 + 10, 30)
    z2+=10
z3=270
while z3<400:
    fence(0, z3, 200, z3 + 8, 25)
    z3+=8


dog(200, 520, 1.2, -1)

dog(30, 350, 1, 1)
dog(500, 330, 1, -1)
house()
dog(330, 510, 5, 1)
brushColor(255,255,255)
circle (50, 370, 5)
circle (72, 370, 5)
circle (148, 540, 6)
circle (174, 540, 6)
circle (457, 350, 5)
circle (480, 350, 5)
circle (430, 585, 12)
brushColor(0,0,0)
circle (50, 370, 2)
circle (72, 370, 2)
circle (148, 540, 3)
circle (174, 540, 3)
circle (457, 350, 2)
circle (480, 350, 2)
circle (430, 585, 6)
run()
