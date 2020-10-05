from turtle import fd, lt,rt,goto,up,down
def draw_Triangle(x,y,size):
    up()
    goto(x,y)
    down()
    rt(60)
    fd(size)
    rt(60)
    fd(size)
    rt(60)
    fd(size)
    up()
    goto(x,y)
    down()
draw_Triangle

