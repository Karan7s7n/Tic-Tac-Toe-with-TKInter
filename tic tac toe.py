import tkinter as tk

def set(row,column):
    global curr
    if(go):
        return

    if board[row][column]["text"] !="":
        return
    board[row][column]["text"]=curr
    if curr==plo:
        curr=plx
    else:
        curr=plo
    l["text"]=curr+"'s turn"
    cw()

def cw():
    global turns,go
    turns+=1

    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] 
           and board[row][0]["text"] !=""):
            l.config(text=board[row][0]["text"]+"is the WINNER!",foreground=y)
            for column in range(3):
                board[row][column].config(foreground=y,background=lg)
            go=True
            return
    
    for column in range(3):
        if(board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"]
           and board[0][column]["text"]!=""):
            l.config(text=board[0][column]["text"]+"is the WINNER!",foreground=y)
            for row in range(3):
                board[row][column].config(foreground=y,background=lg)
            go=True
            return
    
    if (board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"] and 
        board[0][0]["text"]!=""):
        l.config(text=board[0][0]["text"]+"is the WINNER!",foreground=y)
        for i in range(3):
            board[i][i].config(foreground=y,background=lg)
        go=True
        return
    
    if (board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"] and 
        board[0][2]["text"]!=""):
        l.config(text=board[0][2]["text"]+"is the WINNER!",foreground=y)
        board[0][2].config(foreground=y,background=lg)
        board[1][1].config(foreground=y,background=lg)
        board[2][0].config(foreground=y,background=lg)
        go=True
        return
    if (turns==9):
        go=True
        l.config(text="TIE!",foreground=y)
            

def new():
    global turns,go
    turns=0
    go=False
    l.config(text=curr+"'s turn",foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",foreground=b,background=g)


plx ="X"
plo= "O"
curr=plx
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]
b="#4584b6"
y="#ffde57"
lg="#343434"
g="#646464"
turns=0
go=False
w=tk.Tk()
w.title("TIC TAC TOE")
w.resizable(False, False)
f=tk.Frame(w)
l=tk.Label(f,text=curr+"'s Turn",font=("Consolas",20),background=g,foreground="white")

l.grid(row=0,column=0,columnspan=3,sticky="we")
for row in range(3):
    for column in range(3):
        board[row][column]=tk.Button(f,text="",font=("Consolas",50,"bold"),background=g,
                                     foreground=b,width=4,height=1,
                                     command=lambda row=row,column=column: set(row,column))
        board[row][column].grid(row=row+1,column=column)
r=tk.Button(f,text="RESTART",background=g,foreground="white",command=new)
r.grid(row=4,column=0,columnspan=3,sticky="we")
f.pack()
w.update()
wdh=w.winfo_width()
hei=w.winfo_height()
swdh=w.winfo_screenwidth()
shei=w.winfo_screenheight()
wx=int((swdh/2)-(wdh/2))
wy=int((shei/2)-(hei/2))
w.geometry(f"{wdh}x{hei}+{wx}+{wy}")
w.mainloop()