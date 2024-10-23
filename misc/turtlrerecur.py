def draw_circle(rad):
    import turtle as t
    if rad == 0:
        return rad
    else:
        t.speed(0)
        t.up()
        t.goto(0,-rad)
        t.down()
        t.circle(rad)
        draw_circle(rad-20)



def main():
    rad = 100
    draw_circle(rad)
    input()


if __name__ == '__main__':
    main()