import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("仲間を選ぶ")
root.minsize(640, 480)
root.option_add("*font", ["メイリオ", 14])

# 画像読み込み
king_img = tk.PhotoImage(file="img4/chap4-2-1.png")
monsterA_img = tk.PhotoImage(file="img4/chap4-2-2.png")
monsterB_img = tk.PhotoImage(file="img4/chap4-2-3.png")

# キャンバス作成
canvas = tk.Canvas(root, width=640, height=480)
canvas.place(x=0, y=0)
canvas.create_image(110, 220, image=king_img, tag="illust")
canvas.create_image(320, 220, image=monsterA_img, tag="illust")
canvas.create_image(530, 220, image=monsterB_img, tag="illust")

# ラベル配置
sys_text = tk.Label(text="だれを仲間にしますか？（1:王様、2:魔物A、3:魔物B）")
sys_text.place(x=100, y=20)

# 入力ボックス配置
entry = tk.Entry(width=12)
entry.place(x=200, y=350)

# ボタン配置
button = tk.Button(text="決定")
button.place(x=380, y=350)

# 仲間を選択したときの処理
def choice_friend(friend: str, img: tk.PhotoImage):
    sys_text.destroy()
    res_text = tk.Label(text=f"{friend}が仲間になりました。")
    res_text.place(x=200, y=60)
    canvas.delete("illust")
    canvas.create_image(320, 220, image=img, tag="illust")

# ボタンクリックイベント
def click_btn():
    val = float(entry.get())
    if val == 1:
        choice_friend("王様", king_img)
    elif val == 2:
        choice_friend("魔物A", monsterA_img)
    elif val == 3:
        choice_friend("魔物B", monsterB_img)
    else:
        res_text = tk.Label(text="だれも仲間になりませんでした。")
        res_text.place(x=160, y=60)
        canvas.delete("illust")

    button["state"] = "disabled"
    entry["state"] = "disabled"

button["command"] = click_btn

root.mainloop()
