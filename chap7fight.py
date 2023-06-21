import random
import time
import tkinter as tk


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
        pass

    def click_reserve(self):
        """力をためるボタンクリック"""
        pass

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


class Character:
    """キャラクタークラス"""
    def __new__(cls) -> None:
        obj = super().__new__(cls)
        obj.rsv = 1

        return obj

    def reserve(self):
        """力をためる"""
        self.rsv += 1

    def get_atk(self):
        """攻撃力を返す"""
        r = self.rsv
        self.rsv = 1
        return random.randint(1, self.atk * r)

    def get_dfs(self):
        """防御力を返す"""
        return random.randint(0, self.dfs)

    def culc_hp(self, atk, dfs):
        dmg = atk - dfs

        if dmg < 1:
            return self.hp

        self.hp -= dmg

        if self.hp < 1:
            self.hp = 0

        return self.hp


class Brave(Character):
    """勇者クラス"""
    def __init__(self) -> None:
        self.name = "勇者ハル"
        self.hp = 30
        self.atk = 15
        self.dfs = 10


class Monster1(Character):
    """モンスター1クラス"""
    def __init__(self) -> None:
        self.name = "マコデビル"
        self.hp = 20
        self.atk = 15
        self.dfs = 5


class Monster2(Character):
    """モンスター2クラス"""
    def __init__(self) -> None:
        self.name = "リリースネーク"
        self.hp = 10
        self.atk = 8
        self.dfs = 5
