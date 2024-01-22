import random
import tkinter ### 窗口


f=open('食谱.txt', encoding='utf-8')
txt=[]
for line in f:
    txt.append(line.strip())
# print(txt)

foods=txt

def new_text():
    global  button_control
    n_foods = len(foods)
    choose_food = random.randint(0, n_foods - 1)  ###random.randint(a, b) 生成的随机数n: a <= n <= b,
    # print("等下去吃%s叭！"%foods[choose_food])
    food = foods[choose_food]
    text_new = tkinter.Label(Window, text=food, bg='gray', fg='white', font=('华文楷体', 28))
    text_new.pack()

Window=tkinter.Tk()
Window.title('等下吃什么')
Window.geometry('400x300')
text=tkinter.Label(Window,text='等下吃什么捏？',bg='gray',fg='white',font=('华文楷体',28))
text.pack()
button=tkinter.Button(Window,text='点击随机',width=15,height=2,command=new_text)
button.pack()
Window.mainloop()