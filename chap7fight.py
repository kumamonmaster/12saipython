import random
import tkinter as tk


class FightManager:
    def __init__(self) -> None:
        self.dialog = tk.Frame(width=820, height=434)
        self.dialog.place(x=10, y=10)

        canvas = tk.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="black")

        # 「勝った」ボタン
        btn_win = tk.Button(self.dialog, text="勝った")
        btn_win.place(x=180, y=340)
        btn_win["command"] = self.fight_win

        # 「負けた」ボタン
        btn_lose = tk.Button(self.dialog, text="負けた")
        btn_lose.place(x=320, y=340)
        btn_lose["command"] = self.fight_lose

        # 非表示
        self.dialog.place_forget()

    def fight_start(self, map_data, x, y):
        """戦闘開始"""
        self.dialog.place(x=10, y=10)
        self.map_data = map_data
        self.brave_x = x
        self.brave_y = y

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
    def get_atk(self):
        """攻撃力を返す"""
        return random.randint(1, self.atk)

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
