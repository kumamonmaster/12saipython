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

# メインループ
root.mainloop()
