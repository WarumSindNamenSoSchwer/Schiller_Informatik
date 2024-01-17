import turtle
import math

def_height = 130
def_width = 90


def draw_arc(t, r, rot):
    circumference = 2 * math.pi * r * (rot / 360)
    n = int((circumference / 4) + 3)
    turn = rot / n
    width = circumference / n
    t.lt(turn / 2)
    for i in range(n):
        t.fd(width)
        t.lt(turn)
    t.rt(turn / 2)


def draw_diagonal(t, n, rot):
    t.seth(rot)
    t.fd(n)


def draw_vertical(t, n):
    draw_diagonal(t, n, 90)


def draw_horizontal(t, n):
    draw_diagonal(t, n, 0)


def goto_initial_pos(t, initial_pos):
    t.pu()
    t.goto(initial_pos)
    t.seth(0)
    t.pd()


def draw_a(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    diagonal_line_width = math.sqrt(height ** 2 + (width / 2) ** 2)
    rotation = math.asin(height / diagonal_line_width)
    draw_diagonal(t, diagonal_line_width, math.degrees(rotation))
    draw_diagonal(t, diagonal_line_width, 360 - math.degrees(rotation))
    middle_line_width = 70 * n
    middle_line_height = math.tan(rotation) * middle_line_width / 2
    t.pu()
    t.goto(initial_pos[0] + (10 * n), initial_pos[1] + (height - middle_line_height))
    t.pd()
    draw_horizontal(t, middle_line_width)
    goto_initial_pos(t, initial_pos)


def draw_b(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_vertical(t, height)
    draw_diagonal(t, height, 270)
    draw_horizontal(t, width / 2)
    draw_arc(t, height / 4, 180)
    t.goto(initial_pos[0], initial_pos[1] + height / 2)
    draw_horizontal(t, width / 2)
    draw_arc(t, height / 4, 180)
    t.goto(initial_pos[0], initial_pos[1] + height)
    goto_initial_pos(t, initial_pos)


def draw_c(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_horizontal(t, width)
    draw_vertical(t, height)
    t.pd()
    t.seth(180)
    draw_diagonal(t, width - (height / 2), 180)
    draw_arc(t, height / 2, 180)
    draw_horizontal(t, width - (height / 2))
    goto_initial_pos(t, initial_pos)


def draw_d(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_horizontal(t, width - (height / 2))
    draw_arc(t, height / 2, 180)
    draw_diagonal(t, width - (height / 2), 180)
    draw_diagonal(t, height, 270)
    goto_initial_pos(t, initial_pos)


def draw_f(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_vertical(t, height)
    draw_horizontal(t, width)
    t.pu()
    t.goto(initial_pos[0], initial_pos[1] + (height / 2))
    t.pd()
    draw_horizontal(t, width / 2)
    goto_initial_pos(t, initial_pos)


def draw_e(t, n=1):
    initial_pos = t.pos()
    width = def_width * n
    draw_f(t, n)
    draw_horizontal(t, width)
    goto_initial_pos(t, initial_pos)


def draw_g(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_c(t, n)
    t.pu()
    draw_horizontal(t, width)
    t.pd()
    draw_vertical(t, height / 2)
    draw_diagonal(t, width / 2, 180)
    goto_initial_pos(t, initial_pos)


def draw_h(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_vertical(t, height)
    draw_diagonal(t, height / 2, 270)
    draw_horizontal(t, width)
    draw_diagonal(t, height / 2, 270)
    draw_vertical(t, height)
    goto_initial_pos(t, initial_pos)


def draw_i(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_horizontal(t, width)
    draw_diagonal(t, width / 2, 180)
    draw_vertical(t, height)
    draw_diagonal(t, width / 2, 180)
    draw_horizontal(t, width)
    goto_initial_pos(t, initial_pos)


def draw_j(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_vertical(t, width / 2)
    t.pd()
    t.seth(270)
    draw_arc(t, width / 2, 180)
    draw_vertical(t, height - (width / 2))
    draw_diagonal(t, width, 180)
    goto_initial_pos(t, initial_pos)


def draw_k(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_vertical(t, height)
    draw_diagonal(t, height / 2, 270)
    height_of_diagonal_lines = math.sqrt((height / 2) ** 2 + width ** 2)
    rotation = math.atan((height / 2) / width)
    draw_diagonal(t, height_of_diagonal_lines, math.degrees(rotation))
    t.pu()
    draw_diagonal(t, height_of_diagonal_lines, math.degrees(rotation) + 180)
    t.pd()
    draw_diagonal(t, height_of_diagonal_lines, 360 - math.degrees(rotation))
    goto_initial_pos(t, initial_pos)


def draw_l(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_vertical(t, height)
    goto_initial_pos(t, initial_pos)
    draw_horizontal(t, width)
    goto_initial_pos(t, initial_pos)


def draw_m(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    t.goto(initial_pos[0] + width, initial_pos[1])
    t.pd()
    draw_vertical(t, height)
    goto_initial_pos(t, initial_pos)
    draw_vertical(t, height)
    width_of_diagonal_lines = math.sqrt((height / 2) ** 2 + (width / 2) ** 2)
    rotation = math.atan((width / 2) / (height / 2))
    draw_diagonal(t, width_of_diagonal_lines, 270 + math.degrees(rotation))
    draw_diagonal(t, width_of_diagonal_lines, 90 - math.degrees(rotation))
    goto_initial_pos(t, initial_pos)


def draw_n(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_vertical(t, height)
    width_of_diagonal_line = math.sqrt(height ** 2 + width ** 2)
    rotation = math.atan(width / height)
    draw_diagonal(t, width_of_diagonal_line, 270 + math.degrees(rotation))
    draw_vertical(t, height)
    goto_initial_pos(t, initial_pos)


def draw_o(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_vertical(t, width / 2)
    t.seth(270)
    t.pd()
    draw_arc(t, width / 2, 180)
    draw_vertical(t, height - width)
    draw_arc(t, width / 2, 180)
    draw_diagonal(t, width / 2, 270)
    goto_initial_pos(t, initial_pos)


def draw_p(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_vertical(t, height)
    draw_diagonal(t, height / 2, 270)
    draw_horizontal(t, width - (height / 4))
    draw_arc(t, height / 4, 180)
    draw_diagonal(t, width - (height / 4), 180)
    goto_initial_pos(t, initial_pos)


def draw_q(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_o(t, n)
    t.pu()
    t.goto(initial_pos[0] + width / 2, initial_pos[1] + width / 2)
    t.pd()
    t.goto(initial_pos[0] + width, initial_pos[1])
    goto_initial_pos(t, initial_pos)


def draw_r(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_p(t, n)
    t.pu()
    draw_horizontal(t, width)
    t.seth(90)
    t.pd()
    draw_arc(t, height / 2, 90)
    goto_initial_pos(t, initial_pos)


def draw_s(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    draw_horizontal(t, width / 2)
    draw_arc(t, height / 4, 180)
    t.pu()
    t.goto(initial_pos[0] + width, initial_pos[1] + height)
    t.pd()
    draw_diagonal(t, width / 2, 180)
    t.seth(180)
    draw_arc(t, height / 4, 180)
    goto_initial_pos(t, initial_pos)


def draw_t(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_horizontal(t, width / 2)
    t.pd()
    draw_vertical(t, height)
    t.pu()
    draw_diagonal(t, width / 2, 180)
    t.pd()
    draw_horizontal(t, width)
    goto_initial_pos(t, initial_pos)


def draw_u(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_vertical(t, width / 2)
    t.pd()
    draw_vertical(t, height - width / 2)
    t.pu()
    draw_diagonal(t, height - width / 2, 270)
    t.pd()
    draw_arc(t, width / 2, 180)
    draw_vertical(t, height - width / 2)
    goto_initial_pos(t, initial_pos)


def draw_v(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_vertical(t, height)
    t.pd()
    width_of_line = math.sqrt(height ** 2 + (width / 2) ** 2)
    rotation = math.atan((width / 2) / height)
    draw_diagonal(t, width_of_line, 270 + math.degrees(rotation))
    draw_diagonal(t, width_of_line, 90 - math.degrees(rotation))
    goto_initial_pos(t, initial_pos)


def draw_w(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_vertical(t, height)
    t.pd()
    width_of_lines = math.sqrt(height ** 2 + (width / 4) ** 2)
    rotation = math.atan((width / 4) / height)
    draw_diagonal(t, width_of_lines, 270 + math.degrees(rotation))
    draw_diagonal(t, width_of_lines, 90 - math.degrees(rotation))
    draw_diagonal(t, width_of_lines, 270 + math.degrees(rotation))
    draw_diagonal(t, width_of_lines, 90 - math.degrees(rotation))
    goto_initial_pos(t, initial_pos)


def draw_x(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    width_of_lines = math.sqrt(height ** 2 + width ** 2)
    rotation = math.atan(width / height)
    draw_diagonal(t, width_of_lines, 90 - math.degrees(rotation))
    t.pu()
    draw_diagonal(t, width, 180)
    t.pd()
    draw_diagonal(t, width_of_lines, 360 - (90 - math.degrees(rotation)))
    goto_initial_pos(t, initial_pos)


def draw_y(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_horizontal(t, width / 2)
    t.pd()
    draw_vertical(t, height / 2)
    width_of_daigonal_lines = math.sqrt((height / 2) ** 2 + (width / 2) ** 2)
    rotation = math.atan((width / 2) / (height / 2))
    draw_diagonal(t, width_of_daigonal_lines, 90 + math.degrees(rotation))
    t.pu()
    draw_diagonal(t, width_of_daigonal_lines, 360 - (90 - math.degrees(rotation)))
    t.pd()
    draw_diagonal(t, width_of_daigonal_lines, 90 - math.degrees(rotation))
    goto_initial_pos(t, initial_pos)


def draw_z(t, n=1):
    initial_pos = t.pos()
    height = def_height * n
    width = def_width * n
    t.pu()
    draw_vertical(t, height)
    t.pd()
    draw_horizontal(t, width)
    width_of_diagonal_line = math.sqrt(height ** 2 + width ** 2)
    rotation = math.atan(height / width)
    draw_diagonal(t, width_of_diagonal_line, 180 + math.degrees(rotation))
    draw_horizontal(t, width)
    goto_initial_pos(t, initial_pos)
    t.pu()
    draw_vertical(t, height / 2)
    draw_horizontal(t, width / 4)
    t.pd()
    draw_horizontal(t, width / 2)
    goto_initial_pos(t, initial_pos)


# height of letters --> 130
# width of letters --> 90
# bob starts at --> -550, -300
# separation within letters --> 10

"""
func_list = (draw_a(bob, n), change_pos(bob), draw_b(bob, n), change_pos(bob), draw_c(bob, n), change_pos(bob),
             draw_d(bob, n), change_pos(bob), draw_e(bob, n), change_pos(bob), draw_f(bob, n), change_pos(bob),
             draw_g(bob, n), change_pos(bob), draw_h(bob, n), change_pos(bob), draw_i(bob, n), change_pos(bob),
             draw_j(bob, n), change_pos(bob), draw_k(bob, n), change_pos(bob), draw_l(bob, n), change_pos(bob),
             draw_m(bob, n), change_pos(bob, True), draw_n(bob, n), change_pos(bob), draw_o(bob, n), change_pos(bob),
             draw_p(bob, n), change_pos(bob), draw_q(bob, n), change_pos(bob), draw_r(bob, n), change_pos(bob),
             draw_s(bob, n), change_pos(bob), draw_t(bob, n), change_pos(bob), draw_u(bob, n), change_pos(bob),
             draw_v(bob, n), change_pos(bob), draw_w(bob, n), change_pos(bob), draw_x(bob, n), change_pos(bob),
             draw_y(bob, n), change_pos(bob), draw_z(bob, n))"""






