from turtle import fd, lt,rt,goto,up,down
def draw_triangle_down(x,y,size):
    up()
    goto(x,y)
    down()
    fd(size)
    rt(120)
    fd(size)
    rt(120)
    fd(size)
    rt(120)


def draw_triangle_up(x,y,size):
    up()
    goto(x,y)
    down()
    fd(size)
    lt(120)
    fd(size)
    lt(120)
    fd(size)
    lt(120)


draw_triangle_down(0,100,100)

draw_triangle_up(0,100,100)

