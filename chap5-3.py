import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("棒グラフをソートして表示する")

# キャンバスの作成
canvas = tk.Canvas(root, width=640, height=480)
canvas.create_rectangle(40, 40, 600, 440, fill="gray78")
canvas.pack()

# データの作成
data = [70, 15, 66, 21, 19, 97, 33, 44, 30, 2]
disp = ""
len_data = len(data)

for k in range(len_data - 1, 0, -1):
    print(f"{len_data - k}度目")
    for j in range(0, k):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
        for i in data:
            disp = disp + str(i) + " "
        print(disp)
        disp = ""

root.mainloop()
