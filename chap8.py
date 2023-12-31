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
    elif params[0] == "#branch":
        message.unbind("<Button-1>")
        btn = tk.Button(text=params[2], width=20)
        branch.append(btn)
        btn["command"] = lambda : jump_to_line(int(params[1])-1)
        btn.place(x=300, y=60+int(params[1])*60)
        jumplabel.append(params[3])
        if params[4] == "n":
            return
    elif params[0] == "#jump":
        label = params[1].strip()
        # ジャンプ先を探す
        for l in range(len(scanario)):
            if scanario[l].strip() == "## " + label:
                current_line = l
                decode_line(None)
                return
    elif params[0].strip() == "#end":
        message["text"] = "終わり"
        message.unbind("<Button-1>")
        current_line = 999999999

    decode_line(None)

def jump_to_line(branchID):
    global current_line

    # ボタンを消す
    for btn in branch:
        btn.place_forget()
        btn.destroy()

    branch.clear()
    label = jumplabel[branchID]
    jumplabel.clear()
    message.bind("<Button-1>", decode_line)

    # ラベルにジャンプ
    for l in range(len(scanario)):
        if scanario[l].strip() == "## " + label:
            current_line = l
            decode_line(None)
            return

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

# 選択肢
branch = []
jumplabel = []

root.mainloop()
