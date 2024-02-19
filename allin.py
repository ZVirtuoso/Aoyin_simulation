"""
敖隐模拟
主、副剑指为最新使用两个技能的对应元素
使用技能对应元素，若已有相同元素的剑指，则获得相同的两个剑指
使用技能获得被动印记，拥有被动印记普攻获得主剑元素和印记数量相关的对应效果
1技能可以获得两个印记
使用大招时印记不会消失，不可以普攻
"""

ELE_EFFECT = {
    "fire": "伤害",
    "water": "恢复",
    "wind": "击退",
}
ELE_NAME = {
    "fire": "【火】",
    "water": "【水】",
    "wind": "【风】",
}
ELE_OF_ORDER = {
    "1": "fire",
    "2": "water",
    "3": "wind",
}


class Allin:
    def __init__(self):
        self.pri_ele = "fire"
        self.sec_ele = "fire"
        self.mark_num = 0
        self.fly = False

    def check(self):
        if self.mark_num > 3:
            self.mark_num = 3
        print(
            "当前主剑指为%s，副剑指为%s，龙魂印记数量为%s"
            % (ELE_NAME[self.pri_ele], ELE_NAME[self.sec_ele], self.mark_num)
        )
        if self.pri_ele == "wind" or self.sec_ele == "wind":
            if self.pri_ele == self.sec_ele:
                print("你正在享受2.5倍移速加成！")
                return None
            print("你正在享受加速效果！")

    def attack(self):
        if not self.fly:
            # if self.mark_num > 0:
            #     # print("强化普攻")
            #     print("强化普攻产生了大量的%s" % (ELE_EFFECT[self.pri_ele]), end=",")
            #     self.mark_num = 0
            #     if self.pri_ele == self.sec_ele:
            #         print("并造成了2.5效果", end="")
            # elif self.pri_ele == self.sec_ele:
            #     print("普攻并产生了2.5倍的%s" % (ELE_EFFECT[self.pri_ele]), end=",")
            # else:
            #     print(
            #         "普攻造成了%s效果，并造成了少量%s效果"
            #         % (ELE_EFFECT[self.pri_ele], ELE_EFFECT[self.sec_ele]),
            #         end=",",
            #     )
            # print()

            if self.mark_num > 0:
                print(
                    "普攻造成了额外%s和副剑的%s效果"
                    % (ELE_EFFECT[self.pri_ele], ELE_EFFECT[self.sec_ele]),
                    end=",",
                )
                # print("强化普攻")
                print("此次为强化普攻,附加了%s层龙魂的增幅" % (self.mark_num), end=",")
                self.mark_num = 0
            if self.pri_ele == self.sec_ele:
                print("由于同剑指产生了2.5倍的%s" % (ELE_EFFECT[self.pri_ele]), end=",")
            print()
            self.check()
        else:
            print("腾空期间无法普攻")

    def skill(self, order=""):
        if order != "1":
            if not self.fly:
                self.mark_num += 1
                print("使用了" + order + "技能,增加了一层龙魂")
        else:
            if not self.fly:
                self.mark_num += 2
                print("使用了" + order + "技能,增加了两层龙魂")
        if (self.pri_ele == ELE_OF_ORDER[order]) or (
            self.sec_ele == ELE_OF_ORDER[order]
        ):
            self.pri_ele = ELE_OF_ORDER[order]
            self.sec_ele = ELE_OF_ORDER[order]
        else:
            self.sec_ele = self.pri_ele
            self.pri_ele = ELE_OF_ORDER[order]
        self.check()

    def skill02(self):
        pass

    def skill03(self):
        pass

    def skill04(self):
        if self.fly:
            print("大招落地！")
            self.fly = False
        else:
            print("大招起飞！")
            self.fly = True


cyy = Allin()
while True:
    get_order_seq = list(input("请输入指令"))
    for i in range(len(get_order_seq)):
        if get_order_seq[i] in ("1", "2", "3"):
            cyy.skill(get_order_seq[i])
        if get_order_seq[i] == "4":
            cyy.skill04()
        if get_order_seq[i] == "a":
            cyy.attack()
