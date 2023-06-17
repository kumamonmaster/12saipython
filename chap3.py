import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("リリーにしつもん")
root.minsize(640, 480)

# 画像表示
canvas = tk.Canvas(bg="black", width=640, height=480)
canvas.place(x=0, y=0)
img = tk.PhotoImage(file="img3/chap3-back.png")
canvas.create_image(320, 240, image=img)

# メインループ
root.mainloop()
