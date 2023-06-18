import tkinter as tk
import time

# ウィンドウの作成
root = tk.Tk()
root.title("棒グラフをソートして表示する")

# キャンバスの作成
canvas = tk.Canvas(root, width=640, height=480)
canvas.create_rectangle(40, 40, 600, 440, fill="gray78")
canvas.pack()

# グラフ用変数
start_x = 60
start_y = 60
width_px = 5
height_px = 32
distance_px = 4

# データの作成
data = [70, 15, 66, 21, 19, 97, 33, 44, 30, 2]
len_data = len(data)

# グラフの描画
def draw_graph():
    x = start_x
    y = start_y
    root.update()
    canvas.delete("graph")
    time.sleep(0.1)

    for i in data:
        canvas.create_rectangle(x, y, x + i * width_px, y + height_px, fill="blue", outline="blue", tags="graph")
        y = y + height_px + distance_px

for k in range(len_data - 1, 0, -1):
    for j in range(0, k):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
        draw_graph()

root.mainloop()
