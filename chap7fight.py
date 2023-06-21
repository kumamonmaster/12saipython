import tkinter as tk


class FightManager:
    def __init__(self) -> None:
        self.dialog = tk.Frame(width=820, height=434)
        self.dialog.place(x=10, y=10)

        # 非表示
        self.dialog.place_forget()
