from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.title("Jocul Piatra-Hartie-Foarfeca")
app_font = font.Font(size=12)
root.config(bg='pink')
root.geometry('1000x500')

player_score = 0
computer_score = 0
options = [('piatra', 0), ('hartie', 1), ('foarfeca', 2)]

# Afisare titlu joc
Label(text='Jocul Nostru', font=font.Font(size=20), bg='pink').pack()
Label(text='Piatra-Foarfeca-Hartie', font=font.Font(size=20), bg='red').pack()

# defineste functia de alegere a jucatorului


def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text='Ai ales : ' + player_input[0])
    computer_choice_label.config(text='Computerul a ales : ' + computer_input[0])

    if player_input == computer_input:
        winner_label.config(text="Remiza :|")
    elif (player_input[1]-computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text="Ai castigat :) !!!")
        player_score_label.config(text='Scorul tau : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computerul a castigat :( !!!")
        computer_score_label.config(text='Scorul computerului : ' + str(computer_score))

# Functia de alegere aleatorie a computerului


def get_computer_choice():
    return random.choice(options)


# Eticheta care afiseaza cine castiga de fiecare data
winner_label = Label(text="Sa inceapa jocul...!", fg='black', bg='pink', font=font.Font(size=15), pady=8)
winner_label.pack()

input_frame = Frame(root, bg='#FFE873')
input_frame.pack()

# Afisare optiuni jucator
player_options = Label(input_frame, text="Optiunile tale : ", font=app_font, fg='black', bg='#FFE873')
player_options.grid(row=0, column=0, pady=8)

rock_btn = Button(input_frame, text='Piatra', width=15, bd=0, bg='#1560bd', pady=5,
                  command=lambda: player_choice(options[0]))
rock_btn.grid(row=1, column=1, padx=8, pady=5)

paper_btn = Button(input_frame, text='Hartie', width=15, bd=0, bg='gold', pady=5,
                   command=lambda: player_choice(options[1]))
paper_btn.grid(row=1, column=2, padx=8, pady=5)

scissors_btn = Button(input_frame, text='Foarfeca', width=15, bd=0, bg='red', pady=5,
                      command=lambda: player_choice(options[2]))
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

# Afisare scor si alegeri jucator
score_label = Label(input_frame, text='Scorul : ', font=app_font, fg='black', bg='#FFE873')
score_label.grid(row=2, column=0)

player_choice_label = Label(input_frame, text='Ai ales : ---', font=app_font, bg='#FFE873')
player_choice_label.grid(row=3, column=1, pady=5)

player_score_label = Label(input_frame, text='Scorul tau : 0', font=app_font, bg='#FFE873')
player_score_label.grid(row=3, column=2, pady=5)

computer_choice_label = Label(input_frame, text='Computerul a ales : ---', font=app_font, fg='black', bg='#FFE873')
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input_frame, text='Scorul computerului : 0', font=app_font, fg='black', bg='#FFE873')
computer_score_label.grid(row=4, column=2, padx=(10, 0), pady=5)

root.mainloop()
