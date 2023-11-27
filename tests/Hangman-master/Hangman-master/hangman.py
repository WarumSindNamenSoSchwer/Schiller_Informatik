# -*- coding: utf-8 -*-
import letters
from random import choice
import turtle
from math import atan, degrees, sin, radians


def create_words_list():
    fin = open('tests/Hangman-master/Hangman-master/words.txt')
    word_list = []
    for word in fin:
        word_list.append(word.strip())
    fin.close()
    return word_list


def choose_random_word(t):
    word = choice(create_words_list())
    print(word)
    word_len = len(word)
    draw_spaces(t, word_len)
    return word


def draw_spaces(t, n):
    t.pu()
    t.goto(-550, -300)
    t.pd()
    for i in range(n):
        letters.draw_horizontal(t, 80)
        t.pu()
        letters.draw_horizontal(t, 15)
        t.pd()


def choose_function(let):
    if let.lower() == 'q':
        return letters.draw_q
    elif let.lower() == 'w':
        return letters.draw_w
    elif let.lower() == 'e':
        return letters.draw_e
    elif let.lower() == 'r':
        return letters.draw_r
    elif let.lower() == 't':
        return letters.draw_t
    elif let.lower() == 'y':
        return letters.draw_y
    elif let.lower() == 'u':
        return letters.draw_u
    elif let.lower() == 'i':
        return letters.draw_i
    elif let.lower() == 'o':
        return letters.draw_o
    elif let.lower() == 'p':
        return letters.draw_p
    elif let.lower() == 'a':
        return letters.draw_a
    elif let.lower() == 's':
        return letters.draw_s
    elif let.lower() == 'd':
        return letters.draw_d
    elif let.lower() == 'f':
        return letters.draw_f
    elif let.lower() == 'g':
        return letters.draw_g
    elif let.lower() == 'h':
        return letters.draw_h
    elif let.lower() == 'j':
        return letters.draw_j
    elif let.lower() == 'k':
        return letters.draw_k
    elif let.lower() == 'l':
        return letters.draw_l
    elif let.lower() == 'z':
        return letters.draw_z
    elif let.lower() == 'x':
        return letters.draw_x
    elif let.lower() == 'c':
        return letters.draw_c
    elif let.lower() == 'v':
        return letters.draw_v
    elif let.lower() == 'b':
        return letters.draw_b
    elif let.lower() == 'n':
        return letters.draw_n
    elif let.lower() == 'm':
        return letters.draw_m
    else:
        return 'wrong'


def pick_letter(prev_letters):
    while True:
        chosen_letter = turtle.textinput('Please input a letter', 'Letter:')
        if chosen_letter is None or chosen_letter == '':
            print('Please input a letter')
            continue
        elif not chosen_letter.isalpha():
            print("That isn't a valid character")
            continue
        elif chosen_letter in prev_letters:
            print("You've already chosen that letter")
            continue
        elif len(chosen_letter) > 1:
            print('Please input just one letter')
            continue
        break
    return chosen_letter.lower()


def draw_wrong_letter(t, i, func_):
    """
    i is the prev_words len
    """
    if i <= 8:
        y = 260
    elif i <= 17:
        y = 190
    else:
        y = 120
    pos = 100 + 50 * (i % 9), y
    t.pu()
    t.goto(pos)
    t.pd()
    func_(t, 1 / 3)


def draw_parts_of_person(t, n_mistake):
    if n_mistake == 0:
        t.pu()
        t.goto(-155, 206.65)
        t.pd()
        t.seth(180)
        letters.draw_arc(t, 35, 360)
    if n_mistake == 1:
        t.pu()
        t.goto(-155, 136.65)
        t.pd()
        letters.draw_vertical(t, -130)
    if n_mistake == 2:
        t.pu()
        t.goto(-155, 115)
        t.pd()
        letters.draw_diagonal(t, 65, 303)
    if n_mistake == 3:
        t.pu()
        t.goto(-155, 115)
        t.pd()
        letters.draw_diagonal(t, 65, 237)
    if n_mistake == 4:
        t.pu()
        t.goto(-155, 6.65)
        t.pd()
        letters.draw_diagonal(t, 85, 230)
    if n_mistake == 5:
        t.pu()
        t.goto(-155, 6.65)
        t.pd()
        letters.draw_diagonal(t, 85, 310)


def draw_square_of_chosen_letters(t):
    t.speed(0)
    t.pu()
    t.goto(80, 110)
    t.pd()
    letters.draw_vertical(t, 200)
    letters.draw_horizontal(t, 470)
    letters.draw_vertical(t, -200)
    letters.draw_horizontal(t, -470)
    t.pu()
    t.goto(90, 85)
    letters.draw_w(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_r(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_o(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_n(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_g(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 25)
    t.pd()
    letters.draw_l(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_e(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_t(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_t(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_e(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_r(t, 0.1)
    t.pu()
    letters.draw_horizontal(t, 12)
    t.pd()
    letters.draw_s(t, 0.1)
    t.speed(6)


def draw_gallow(t):
    t.pu()
    t.goto(-550, -110)
    t.pd()
    feet_length = ((95 ** 2) + (55 ** 2)) ** 0.5
    feet_rot = degrees(atan(55 / 95))
    letters.draw_diagonal(t, feet_length, feet_rot)
    letters.draw_diagonal(t, feet_length, (90 - feet_rot) + 270)
    t.pu()
    letters.draw_horizontal(t, -95)
    t.pd()
    letters.draw_vertical(t, 400)
    letters.draw_horizontal(t, 300)
    start_of_rope_pos = t.pos()
    t.pu()
    letters.draw_horizontal(t, -180)
    t.pd()
    beam_length = ((120 ** 2) + (50 ** 2)) ** 0.5
    beam_rot = degrees(atan(50 / 120))
    letters.draw_diagonal(t, beam_length, 180 + beam_rot)
    t.pu()
    t.goto(start_of_rope_pos)
    t.pd()
    t.seth(260)
    letters.draw_arc(t, 120, 20)
    t.pu()
    go_down_by = -((120 / sin(radians(80))) * sin(radians(20)))
    letters.draw_vertical(t, go_down_by)
    t.seth(80)
    t.pd()
    letters.draw_arc(t, 120, 22)


def write_letters(t, func_, spots):
    t.pensize(1.5)
    for i in spots:
        t.pu()
        t.goto(-547 + i * 95, -295)
        t.pd()
        func_(t, 0.822222222)
    t.pensize(1)


def spots_to_draw(word, letter):
    spots = []
    for i in range(len(word)):
        if letter == word[i]:
            spots.append(i)
    return spots


def reset_game(t, to_delete):
    to_delete.clear()
    del to_delete
    main(t)


def win_or_lose(t, delete, result):
    while True:
        answer = turtle.textinput("You " + result, "Wanna play again?")
        if answer.lower() == 'yes':
            reset_game(t, delete)
        elif answer.lower() == 'no':
            print('Goodbye')
            t.clear()
            delete.clear()
            del t, delete
        else:
            print('Input yes or no')
            continue
        break


def draw_ui(t):
    draw_square_of_chosen_letters(t)
    draw_gallow(t)


def main(t):
    not_bob = turtle.Turtle()
    not_bob.ht()
    word = choose_random_word(not_bob)
    prev_letters = []
    wrong_chosen_letters = []
    right_letters = 0
    while True:
        chosen_letter = pick_letter(prev_letters)
        prev_letters.append(chosen_letter)
        chosen_letter_func = choose_function(chosen_letter)
        if chosen_letter in word:
            spots = spots_to_draw(word, chosen_letter)
            right_letters += len(spots)
            write_letters(not_bob, chosen_letter_func, spots)
            if right_letters == len(word):
                win_or_lose(t, not_bob, 'won')
                break
        else:
            mistakes = len(wrong_chosen_letters)
            draw_wrong_letter(not_bob, mistakes, chosen_letter_func)
            draw_parts_of_person(not_bob, mistakes)
            if mistakes == 5:
                win_or_lose(t, not_bob, 'lost')
                break
            wrong_chosen_letters.append(chosen_letter)



if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.ht()
    draw_ui(bob)
    main(bob)

turtle.mainloop()
