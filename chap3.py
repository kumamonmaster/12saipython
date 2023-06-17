import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("リリーにしつもん")
root.minsize(640, 480)
root.option_add("*font", ["MS Pゴシック", 22])

# 画像表示
canvas = tk.Canvas(bg="black", width=640, height=480)
canvas.place(x=0, y=0)
img = tk.PhotoImage(file="img3/chap3-back.png")
canvas.create_image(320, 240, image=img)

# テキスト表示
question = tk.Label(text="知りたいのは何分かな？", bg="white")
question.place(x=100, y=40)

# テキストボックス表示
entry = tk.Entry(width=12, bd=4)
entry.place(x=50, y=133)

# 質問ボタン表示
ask_button = tk.Button(text="聞く")
ask_button.place(x=260, y=125)

# 答え表示
answer = tk.Label(text="・・・・・・・・・", bg="white")
answer.place(x=115, y=235)

# メインループ
root.mainloop()
