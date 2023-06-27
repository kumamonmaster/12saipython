import random


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
