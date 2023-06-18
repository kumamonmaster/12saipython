import tkinter as tk

# マップの描画
def draw_map():
    for y in range(MAX_HEIGHT):
        for x in range(MAX_WIDTH):
            canvas.create_image(x * 62 + 31, y * 62 + 31, image=images[map_data[y][x]])

    # 主人公表示
    canvas.create_image(brave_x * 62 + 31, brave_y * 62 + 31, image=images[4], tag="brave")

# ウィンドウの作成
root = tk.Tk()
root.title("ダンジョン＆パイソン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])

# キャンバス作成
canvas = tk.Canvas(width=620, height=434)
canvas.place(x=10, y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray", tag="drawField")

# ボタン配置
btn_up = tk.Button(text="↑")
btn_up.place(x=720, y=150)

btn_down = tk.Button(text="↓")
btn_down.place(x=720, y=210)

btn_left = tk.Button(text="←")
btn_left.place(x=660, y=180)

btn_right = tk.Button(text="→")
btn_right.place(x=780, y=180)

# 画像読み込み
images = [
    tk.PhotoImage(file="img6/chap6-mapfield.png"),
    tk.PhotoImage(file="img6/chap6-mapwall.png"),
    tk.PhotoImage(file="img6/chap6-mapgoal.png"),
    tk.PhotoImage(file="img6/chap6-mapkey.png"),
    tk.PhotoImage(file="img6/chap6-mapman.png")
]

# マップデータ
MAX_WIDTH = 10
MAX_HEIGHT = 7
map_data = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 2, 0, 0, 1, 3, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 主人公の位置
brave_x = 1
brave_y = 0

draw_map()
root.mainloop()
