import tkinter as tk

from character import Brave
import fight


# マップの描画
def draw_map():
    for y in range(MAX_HEIGHT):
        for x in range(MAX_WIDTH):
            p = map_data[y][x]
            if p >= 5:
                p = 5
            canvas.create_image(x * 62 + 31, y * 62 + 31, image=images[p])

    # 主人公表示
    canvas.create_image(brave_x * 62 + 31, brave_y * 62 + 31, image=images[4], tag="brave")

# 移動先のチェック
def check_move(x, y):
    global brave_x, brave_y, key_flag
    if x >= 0 and x < MAX_WIDTH and y >= 0 and y < MAX_HEIGHT:
        p = map_data[y][x]
        if p == 1:
            return
        elif p == 3:
            key_flag = True
            map_data[y][x] = 0
            canvas.delete("all")
            draw_map()
        elif p == 2:
            if key_flag == True:
                ending()
                return
            else:
                return
        elif p >= 5:
            fightmanager.fight_start(map_data, x, y, brave)

        brave_x = x
        brave_y = y
        draw_map()
        # canvas.coords("brave", brave_x * 62 + 31, brave_y * 62 + 31)

# 上ボタンクリック
def click_btn_up():
    check_move(brave_x, brave_y - 1)

# 下ボタンクリック
def click_btn_down():
    check_move(brave_x, brave_y + 1)

# 左ボタンクリック
def click_btn_left():
    check_move(brave_x - 1, brave_y)

# 右ボタンクリック
def click_btn_right():
    check_move(brave_x + 1, brave_y)

# エンディング表示
def ending():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 620, 434, fill="black")
    canvas.create_text(300, 200,
        fill="white", font=("MS ゴシック", 15),
        text="""ゴールおめでとう。

だが、君の戦いはまだ始まったばかりだ。

                                ・・・つづく？""")
    # ボタンを無効化
    btn_up["state"] = "disabled"
    btn_down["state"] = "disabled"
    btn_left["state"] = "disabled"
    btn_right["state"] = "disabled"


if __name__ == "__main__":
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
    btn_up["command"] = click_btn_up

    btn_down = tk.Button(text="↓")
    btn_down.place(x=720, y=210)
    btn_down["command"] = click_btn_down

    btn_left = tk.Button(text="←")
    btn_left.place(x=660, y=180)
    btn_left["command"] = click_btn_left

    btn_right = tk.Button(text="→")
    btn_right.place(x=780, y=180)
    btn_right["command"] = click_btn_right

    # キーボードの操作設定
    root.bind("<Up>", lambda event: click_btn_up())
    root.bind("<Down>", lambda event: click_btn_down())
    root.bind("<Left>", lambda event: click_btn_left())
    root.bind("<Right>", lambda event: click_btn_right())
    root.bind("f", lambda event: fightmanager.click_fight())
    root.bind("r", lambda event: fightmanager.click_reserve())

    # 画像読み込み
    images = [
        tk.PhotoImage(file="img6/chap6-mapfield.png"),
        tk.PhotoImage(file="img6/chap6-mapwall.png"),
        tk.PhotoImage(file="img6/chap6-mapgoal.png"),
        tk.PhotoImage(file="img6/chap6-mapkey.png"),
        tk.PhotoImage(file="img6/chap6-mapman.png"),
        tk.PhotoImage(file="img6/chap7-mapmonster.png")
    ]

    # マップデータ
    MAX_WIDTH = 10
    MAX_HEIGHT = 7
    map_data = [
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 2, 0, 6, 1, 3, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 5, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 6, 1],
        [1, 0, 6, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # 主人公の位置
    brave_x = 1
    brave_y = 0
    brave = Brave()
    print(brave.get_atk())

    # 鍵取得フラグ
    key_flag = False

    # 先頭画面の準備
    fightmanager = fight.FightManager()

    draw_map()
    root.mainloop()
