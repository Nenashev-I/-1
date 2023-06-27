from tkinter import *

# Словарь вопросов
question = {
    "Кто вы?": ['студент-ботаник', 'двоечник', 'везунчик', 'халявщик'],
    "Где вы живете?": ['На квартире', 'У родителей', 'В общежитие'],
    "Как вы провели выходные?": ['Усиленно готовился', 'Отдыхал и не парился', 'Прочитал пару билетов', 'Тусовался все выходные'],
    "Попросите ли вы помощи у одногрупников?": ['Да', 'Нет'],
    "Во сколько вы ляжете спать?": ['В 23:00', 'В 1 ночи', 'В 3 утра', 'Сон не для меня'],
    "Ваш будильник звонит, стоит ли его отложить": ['Да','Нет'],
    "Стоит ли подучить материал в автобусе?": ['Да','Нет'],
    "Сдавать экзамен первым?": ['Да','Нет'],
}
# Список правильных ответов
ans = ['студент-ботаник', 'В общежитие', 'Усиленно готовился', 'Да', 'В 23:00', 'Нет','Да','Да']

current_question = 0


def start_quiz():
    start_button.forget()
    next_button.pack()
    next_question()


def next_question():
    global current_question
    if current_question < len(question):
        # Ключ
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        # Очищение рамки и обновление
        clear_frame()
        # Вопрос выводится
        Label(f1, text=f"Вопрос : {c_question}", padx=15,
              font="calibre 12 normal").pack(anchor=NW)
        # Вырианты ответов
        for option in question[c_question]:
            Radiobutton(f1, text=option, variable=user_ans,
                        value=option, padx=28).pack(anchor=NW)
        current_question += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        output = f"Вы сдали экзамен на:{user_score.get()} из 100"
        Label(f1, text=output, font="calibre 25 bold").pack()
        Label(f1, text="Конец",
              font="calibre 18 bold").pack()


def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question-1]:
        user_score.set(user_score.get()+10)




def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()


if __name__ == "__main__":
    root = Tk()

    root.title("Имитационное моделирование жизни студента.")
    root.geometry("850x520")
    root.minsize(800, 400)

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    Label(root, text="Имитационное моделирование жизни студента.",
          font="calibre 20 bold",
          relief=SUNKEN,
          padx=10, pady=9).pack()
    Label(root, text="", font="calibre 10 bold").pack()
    start_button = Button(root,
                          text="Начать",
                          command=start_quiz,
                          font="calibre 17 bold")
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Далее",
                         command=next_question,
                         font="calibre 17 bold")

    root.mainloop()
