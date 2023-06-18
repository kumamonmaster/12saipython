import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("ダンジョン＆パイソン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])

# キャンバス作成
canvas = tk.Canvas(width=620, height=434)
canvas.place(x=10, y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray", tag="drawField")

# 画像読み込み
images = [
    tk.PhotoImage(file="img6/chap6-mapfield.png"),
    tk.PhotoImage(file="img6/chap6-mapwall.png"),
    tk.PhotoImage(file="img6/chap6-mapgoal.png"),
    tk.PhotoImage(file="img6/chap6-mapkey.png"),
    tk.PhotoImage(file="img6/chap6-mapman.png")
]

root.mainloop()
