import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("よろしくアドベンチャー")
root.minsize(900, 460)
root.option_add("*font", ["メイリオ", 14])

# キャンバス作成
canvas = tk.Canvas(width=900, height=460)
canvas.place(x=0, y=0)

# メッセージエリア
message = tk.Label(width=70, height=5, wraplength=840, bg="white", justify="left", anchor="nw")
message.place(x=20, y=284)
message["text"] = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよわをんあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよわをん"

root.mainloop()
