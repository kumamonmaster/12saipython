import tkinter as tk

def decode_line(event):
    """1行分のデータをデコードしてメッセージエリアに表示する"""
    global current_line, bgimg, lcharimg, ccharimg, rcharimg
    if current_line >= len(scanario):
        return

    line = scanario[current_line]
    current_line += 1
    line = line.replace("\\n", "\n").strip()
    params = line.split(" ")

    if line[0] != "#":
        message["text"] = line
        return
    elif params[0] == "#back":
        canvas.delete("all")
        bgimg = tk.PhotoImage(file=params[1])
        canvas.create_image(450, 230, image=bgimg)
    elif params[0] == "#putChar":
        if params[2] == "L":
            canvas.delete("left")
            lcharimg = tk.PhotoImage(file=params[1])
            canvas.create_image(200, 160, image=lcharimg, tag="left")
        elif params[2] == "R":
            canvas.delete("right")
            rcharimg = tk.PhotoImage(file=params[1])
            canvas.create_image(700, 160, image=rcharimg, tag="right")
        else:
            canvas.delete("center")
            ccharimg = tk.PhotoImage(file=params[1])
            canvas.create_image(450, 160, image=ccharimg, tag="center")

    decode_line(None)

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
message["text"] = "クリックしてスタート"

# ファイル読み込み
scanario = []
file = open("img8/scenario.txt", "r", encoding="utf_8")
while True:
    line = file.readline()
    scanario.append(line)
    if not line:
        file.close()
        break

current_line = 0
message.bind("<Button-1>", decode_line)

# 画像
bgimg = None
lcharimg = None
ccharimg = None
rcharimg = None

root.mainloop()
