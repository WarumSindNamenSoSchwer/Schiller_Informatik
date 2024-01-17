from turtle import Turtle, Screen
import random as r
import time

# Global variables
balance = 100.0
screen = Screen()
tut_turtle = Turtle()
tut_turtle.ht()
font_style = ('Arial', 15 , 'normal')
current_step = 0

def initialize_turtles():
    tColours = ["red", "green", "blue", "pink", "yellow", "magenta", "orange"]
    yPos = [-260, -172, -85, 2, 85, 172, 260]
    all_turtles = []

    for i in range(7):
        t = Turtle()
        t.ht()
        t.shape("turtle")
        t.speed(0)
        t.shapesize(3)
        t.color(tColours[i])
        t.penup()
        t.goto(-350, yPos[i])
        all_turtles.append(t)

    for t in all_turtles:
        t.st()

    return all_turtles

def continue_tutorial(x, y):
    global current_step
    tut_turtle.clear()

    tutorial_steps = [
        'This is the tutorial.',
        'You will see seven colored turtles pop up.',
        'You will be asked to choose a colored turtle.',
        'You will then be asked to place a bet,\nyou have a balance of 100TC (Turtle Coin).',
        'After you place your bet, the turtles will race.',
        'If the turtle that you chose wins,\nyou will get 50% more than you bet back.',
        'If the turtle that you chose loses, you will lose your bet.',
        'If you understood the tutorial, click to continue.'
    ]

    if current_step < len(tutorial_steps):
        tut_turtle.write(tutorial_steps[current_step], align='center', font=font_style)
        current_step += 1
    else:
        tut_turtle.clear()
        time.sleep(1)
        initialize_game()

def tutorial_screen():
    screen.setup(width=800, height=600)
    screen.title('Tutorial')

    tut_turtle.write("Welcome to the turtle race!/Click to continue.", align='center', font=font_style)
    screen.listen()

    screen.onclick(continue_tutorial)

    screen.mainloop()

def money_cheat():
    global balance
    balance += 10000

def get_bet_input():
    global balance

    bet_color = screen.textinput('Bet', 'Welcome to the turtle race! Place your bet: \nred, green, blue, pink, yellow, magenta, orange\n')

    while True:
        bet_amount = screen.numinput('Bet', f'How much money do you want to place? Your balance is at {balance} TC\n')

        rounded_bet = round(bet_amount, 2)
        print(rounded_bet)
        if balance == 0 or rounded_bet == 0 or rounded_bet > int(balance) or rounded_bet < 0:
            bet_amount = screen.numinput('Bet', f'Invalid input!\nHow much money do you want to place? Your balance is at {balance} TC\n')
        else:
            break

    balance -= float(rounded_bet)

    return bet_color, rounded_bet

def initialize_game():
    global balance

    screen.title("Turtle Race")
    screen.bgpic('Improved_Fixed/road.gif')

    while True:
        all_turtles = initialize_turtles()
        bet_color, bet_amount = get_bet_input()

        is_on = True
        while is_on:
            for i in range(7):
                random_distance = r.randint(0, 15)
                all_turtles[i].forward(random_distance)

                if all_turtles[i].xcor() > 350:
                    is_on = False
                    winner = all_turtles[i].pencolor()
                    if all_turtles[i].pencolor() == bet_color:
                        betxtwo = bet_amount * 2
                        balance += (betxtwo)
                        all_turtles[i].pencolor("white")
                        all_turtles[i].write(f"Well done! {bet_color} has won! Your new balance is {balance} TC!    ", align='right', font=('Arial', 16, 'normal'))
                    else:
                        all_turtles[i].pencolor("white")
                        all_turtles[i].write(f"Uff {winner} has won! Your balance is {balance} TC.    ", align='right', font=('Arial', 16, 'normal'))
                    break

        time.sleep(3)

        for t in all_turtles:
            t.clear()
            t.ht()

        if balance == 0:
            screen.title("Uff, Better luck next time. You lost all your money.")
            time.sleep(3)
            break
        else:
            again = screen.textinput('Again', 'Wanna play again? Yes/No')

        if again.lower() == 'yes':
            pass
        elif again.lower() == 'no':
            time.sleep(1)
            screen.title('Closing program in 3 seconds...')
            tut_turtle.write('Closing program in 3 seconds...', align='center', font=font_style)
            time.sleep(3)
            screen.bye()
            break
        elif again.lower() == 'money!':
            money_cheat()
            pass
        else:
            time.sleep(1)
            screen.title('Unknown input. Closing program in 3 seconds...')
            time.sleep(3)
            print("Error 404!")
            break

if __name__ == "__main__":
    tutorial_screen()
