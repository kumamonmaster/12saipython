import random
import time
import tkinter as tk

from character import Monster1, Monster2

class FightManager:
    def __init__(self) -> None:
        self.dialog = tk.Frame(width=820, height=434)
        self.dialog.place(x=10, y=10)

        self.canvas = tk.Canvas(self.dialog, width=820, height=434)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, 620, 434, fill="black")

        # 「攻撃」ボタン
        self.fbutton = tk.Button(self.dialog, text="攻撃")
        self.fbutton.place(x=180, y=340)
        self.fbutton["command"] = self.click_fight

        # 「力をためる」ボタン
        self.rbutton = tk.Button(self.dialog, text="力をためる")
        self.rbutton.place(x=320, y=340)
        self.rbutton["command"] = self.click_reserve

        # 画像の読み込み
        self.images = [
            tk.PhotoImage(file="img6/chap7-monster1.png"),
            tk.PhotoImage(file="img6/chap7-monster2.png")
        ]
        self.canvas.create_image(180, 160, image=self.images[0])

        # ラベルを配置
        self.label = tk.Label(self.dialog, text="ラベル", fg="white", bg="black", justify="left")
        self.label.place(x=360, y=10)

        # 非表示
        self.dialog.place_forget()

    def fight_start(self, map_data, x, y, brave):
        """戦闘開始"""
        self.dialog.place(x=10, y=10)
        self.map_data = map_data
        self.brave_x = x
        self.brave_y = y
        self.brave = brave

        # モンスターの画像を表示
        p = self.map_data[y][x]
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 620, 434, fill="black")
        self.canvas.create_image(180, 160, image=self.images[p - 5])
        self.label["text"] = ""

        # モンスターのオブジェクトを作成
        if p == 5:
            self.monster = Monster1()
        elif p == 6:
            self.monster = Monster2()

        self.label["text"] = f"{self.monster.name}が現れた！"

    def click_fight(self):
        """攻撃ボタンクリック"""
        self.fbutton["state"] = "disabled"
        self.rbutton["state"] = "disabled"
        self.do_turn(self.brave.get_atk())

    def click_reserve(self):
        """力をためるボタンクリック"""
        self.fbutton["state"] = "disabled"
        self.rbutton["state"] = "disabled"
        self.brave.reserve()
        self.do_turn(-1)

    def do_turn(self, brave_atk):
        """戦闘処理"""
        # 主人公のターン
        monster_dfs = self.monster.get_dfs()
        if brave_atk < 0:
            label_text = f"{self.brave.name}は力をためた"
        else:
            label_text = f"{self.brave.name}は攻撃した"
            self.label["text"] = label_text
            self.dialog.update()

            time.sleep(0.5)

            dmg = brave_atk - monster_dfs
            self.monster.culc_hp(brave_atk, monster_dfs)
            if dmg <= 0:
                label_text += "\n防がれた"
            else:
                label_text += f"\n{dmg}のダメージを与えた"

        # ラベル更新、残り体力表示
        self.label["text"] = label_text
        self.dialog.update()

        time.sleep(0.5)

        label_text += f"\nモンスターの残り体力は{self.monster.hp}"
        self.label["text"] = label_text
        self.dialog.update()

        if self.monster.hp < 1:
            time.sleep(0.5)
            self.fbutton["state"] = "normal"
            self.rbutton["state"] = "normal"
            self.fight_win()
            return

        # モンスターのターン
        time.sleep(0.5)
        brave_dfs = self.brave.get_dfs()
        if random.random() < 0.2:
            label_text += "\n\nモンスターは力をためた"
            self.monster.reserve()
        else:
            label_text += "\n\nモンスターの攻撃"
            self.label["text"] = label_text
            self.dialog.update()

            time.sleep(0.5)

            monster_atk = self.monster.get_atk()
            dmg = monster_atk - brave_dfs
            self.brave.culc_hp(monster_atk, brave_dfs)
            if dmg <= 0:
                label_text += "\n防いだ"
            else:
                label_text += f"\n{dmg}のダメージを受けた"

        # ラベル更新、残り体力表示
        self.label["text"] = label_text
        self.dialog.update()

        time.sleep(0.5)

        label_text += f"\n勇者の残り体力は{self.brave.hp}"
        self.label["text"] = label_text
        self.dialog.update()

        if self.brave.hp < 1:
            time.sleep(0.5)
            self.fight_lose()
        else:
            self.fbutton["state"] = "normal"
            self.rbutton["state"] = "normal"

    def fight_win(self):
        """戦闘勝利"""
        self.map_data[self.brave_y][self.brave_x] = 0
        self.dialog.place_forget()

    def fight_lose(self):
        """戦闘敗北"""
        canvas = tk.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="red")
        canvas.create_text(300, 200, fill="white", font=("MS ゴシック", 15), text="""勇者は負けてしまった。
最初からやり直してくれたまえ。""")
