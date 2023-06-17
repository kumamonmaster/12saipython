import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("勇者求む！")
root.minsize(640, 480)
root.option_add("*font", ["メイリオ", 14])

# 画像読み込み
img1 = tk.PhotoImage(file="img4/chap4-1-1.png")
img2 = tk.PhotoImage(file="img4/chap4-1-2.png")
img3 = tk.PhotoImage(file="img4/chap4-1-3.png")

# キャンバス作成
canvas = tk.Canvas(root, width=640, height=480)
canvas.place(x=0, y=0)
canvas.create_image(320, 220, image=img1, tag="illust")

# メインループ
root.mainloop()
