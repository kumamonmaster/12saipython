class CharaTest:
    def __init__(self, name):
        self.name = name

    def fight(self):
        print(f"{self.name}は戦うぞ！")

chara1 = CharaTest("戦士")
print(chara1.name)
chara1.fight()
