import tkinter as tk


class FightManager:
    def __init__(self) -> None:
        self.dialog = tk.Frame(width=820, height=434)
        self.dialog.place(x=10, y=10)

        canvas = tk.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="black")

        # ボタン作成
        btn_win = tk.Button(self.dialog, text="勝った")
        btn_win.place(x=180, y=340)
        btn_lose = tk.Button(self.dialog, text="負けた")
        btn_lose.place(x=320, y=340)

        # 非表示
        self.dialog.place_forget()

    def fight_start(self, map_data, x, y):
        """戦闘開始"""
        self.dialog.place(x=10, y=10)
