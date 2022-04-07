from tkinter import *
import random

root = Tk()
root.title('Виселица :)')
canvas = Canvas(root, width=600, height=600)
canvas.pack()
textt = 'Давай сыграем в игру!'
canvas.create_text(300, 260, text=textt, fill='black', font=('Arial', 24))

def game():
    width = 1000
    height = 700
    margin = 100
    label_word = []
    bth_alpha = []
    color = 'pink'
    color2 = 'grey'

    def vicel():
        line1 = canvas.create_line(margin, height - margin, margin, margin, width=4, fill='orange')
        line2 = canvas.create_line(margin, margin, width // 3, margin, width=4, fill='orange')
        line3 = canvas.create_line(width // 3, margin, width // 3, margin * 2, width=4, fill='black')
        root.update()

    def alphabet():
        x1 = 0
        y1 = 0
        count = 0
        for i in range(ord('А'), ord('Я') + 1):
            btn = Button(text=chr(i), font=('Arial', 20))
            btn.place(x=height - margin * 2 + x1,
                      y=margin * 3.4 - y1)
            btn.bind('<Button-1>', lambda event: check(event, word))
            bth_alpha.append(btn)
            x1 += 45
            count += 1

            if (count == 8):
                x1 = count = 0
                y1 -= 60
        root.update()

    def start_word():
        f = open('word.txt')
        count = 0

        for i in f:
            count += 1

        num = random.randint(1, count)
        word = ''
        count = 0
        f = open('word.txt', encoding='utf-8')
        for i in f:
            count += 1

            if (count == num):
                word = i[:len(i) - 1:]

        word = word.upper()
        print(word)
        return word
        root.update()

    def start_pas_word(word):
        count = 0
        for i in range(len(word)):
            label_under = Label(root, text='__', font=('Arial', 20), bg=color)
            label_under.place(x=height - margin * 2 + count, y=margin * 2.5)
            count += 40
            label_word.append(label_under)
        root.update()

    def draw(lifes):
        if (lifes == 4):
            head = canvas.create_oval(width // 3 - 40, margin * 1.75,
                                      width // 3 + 40, margin * 2.5, width=2, fill='white')
        elif (lifes == 3):
            body = canvas.create_line(width // 3, margin * 2.5,
                                      width // 3, margin * 4, width=4, fill='black')
        elif (lifes == 2):
            l_hand = canvas.create_line(width // 3, margin * 2.5,
                                        width // 3 - 70, margin * 3, width=4, fill='black')
            r_hand = canvas.create_line(width // 3, margin * 2.5,
                                        width // 3 + 70, margin * 3, width=4, fill='black')
        elif (lifes == 1):
            l_foot = canvas.create_line(width // 3, margin * 4,
                                        width // 3 - 70, margin * 5, width=4, fill='black')
            r_foot = canvas.create_line(width // 3, margin * 4,
                                        width // 3 + 70, margin * 5, width=4, fill='black')
        elif (lifes == 0):
            l_eye = canvas.create_line(width // 3.05, margin * 2,
                                       width // 3.3, margin * 2.15, width=3, fill='black')
            l_eye2 = canvas.create_line(width // 3.3, margin * 2,
                                        width // 3.05, margin * 2.15, width=3, fill='black')
            p_eye = canvas.create_line(width // 2.8, margin * 2,
                                       width // 3, margin * 2.15, width=3, fill='black')
            p_eye2 = canvas.create_line(width // 3, margin * 2,
                                        width // 2.8, margin * 2.15, width=3, fill='black')
            game_over('lose')
        root.update()

    def check(event, word):
        alpha = event.widget['text']
        p = []

        for i in range(len(word)):
            if (word[i] == alpha):
                p.append(i)

        if (len(p) != 0):
            for i in p:
                label_word[i].config(text='{}'.format(word[i]))

            count_alpha = 0
            for i in label_word:
                if (i['text'].isalpha()):
                    count_alpha += 1
            if (count_alpha == len(word)):
                game_over('win')
        else:
            lifes = int(label_life.cget('text'))

            if (lifes != 0):
                label_life.config(text='{}'.format(lifes - 1))

            draw(lifes)
        root.update()

    def game_over(status):
        for btn in bth_alpha:
            btn.destroy()

        if (status == 'win'):
            canvas.create_text(canvas.winfo_width() / 2 + 100, canvas.winfo_height() / 2, font=('Arial', 26),
                               text='Ты победил!', fill='black')
        else:
            canvas.create_text(canvas.winfo_width() / 2 + 100, canvas.winfo_height() / 2, font=('Arial', 26),
                               text='Попробуй ещё раз', fill='black')
        root.update()

        butt2 = Button(root, text='Начать', width=14, height=3, command=lambda: game())
        butt2.place(x=550, y=450)

    lifes = 5

    label_text = Label(root, text='Жизни: ', font=('Arial', 20))
    label_text.place(x=800, y=10)
    root.update()
    label_life = Label(root, text='{}'.format(lifes), font=('Arial', 20))
    label_life.place(x=900, y=10)
    root.update()

    canvas = Canvas(root, width=width, height=height, bg=color2)
    canvas.place(x=0, y=40)
    root.geometry('900x850')

    vicel()
    alphabet()
    word = start_word()
    start_pas_word(word)
    print(word)

butt1 = Button(root, text='Начать', width=14, height=3, command=lambda: game())
butt1.place(x=250, y=470)
root.mainloop()
