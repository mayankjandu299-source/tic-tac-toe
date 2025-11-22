import tkinter as tk
from tkinter import messagebox

def check_winner():
    """Highlight winning line, declare winner or draw, and disable board."""
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    # check wins
    for a, b, c in win_combos:
        t1, t2, t3 = buttons[a]["text"], buttons[b]["text"], buttons[c]["text"]
        if t1 != "" and t1 == t2 == t3:
            for i in (a, b, c):
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {t1} wins")
            disable_all()
            return True
    # check draw
    if all(btn["text"] != "" for btn in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        disable_all()
        return True
    return False

def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

def on_click(index):
    global current_player
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        finished = check_winner()
        if not finished:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

# create 9 buttons; don't shadow names
buttons = [
    tk.Button(
        root, text="", font=("normal", 25), width=6, height=2,
        command=lambda i=i: on_click(i)
    )
    for i in range(9)
]

for i, btn in enumerate(buttons):
    btn.grid(row=i // 3, column=i % 3)

current_player = "X"
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()

