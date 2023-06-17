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

# ラベル配置
serifu_text = tk.Label(text="王様「魔王を倒したら褒美をやるぞ！」")
serifu_text.place(x=160, y=10)

sys_text = tk.Label(text="褒美はいくらあげますか？", fg="red")
sys_text.place(x=180, y=380)

# 入力ボックス配置
entry = tk.Entry(width=12)
entry.place(x=180, y=420)
bold_text = tk.Label(text="ゴールド")
bold_text.place(x=330, y=420)

# ボタン配置
button = tk.Button(text="決定")
button.place(x=420, y=420)

# ボタンクリックイベント
def click_btn():
    gold = float(entry.get())
    if gold >= 100000:
        canvas.delete("illust")
        canvas.create_image(320, 220, image=img3, tag="illust")
        serifu_text["text"] = "勇者「そんな大金、よっぽど危険なんだ・・・。\n関わらないでおこう。」"
    elif gold >= 5000:
        canvas.delete("illust")
        canvas.create_image(320, 220, image=img2, tag="illust")
        serifu_text["text"] = "勇者「よーし、私に任せなさい！」"
    else:
        serifu_text["text"] = "志願者は誰も来ませんでした。"

    sys_text.destroy()
    button["state"] = "disabled"
    entry["state"] = "disabled"

button["command"] = click_btn

# メインループ
root.mainloop()
