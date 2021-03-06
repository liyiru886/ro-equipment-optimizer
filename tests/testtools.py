import sys


class TestTools:
    # input 裝備資訊or人物資訊
    def verify_statsname(info):
        for i in info:
            if i not in TestTools.__statsnamelist:
                print(i)
                sys.exit()
                break

    # input 人物資訊內的裝備表
    def verify_equiplist(equiplist):
        for i in equiplist:
            if i not in TestTools.__equipnamelist:
                print(i)
                break

    __statsnamelist = [
        # 人物素質
        'HP',
        '基礎HP',
        '乘算MHP加成',
        '加算MHP加成',
        'SP',
        '基礎HP',
        '乘算MSP加成',
        '加算MSP加成',
        'BLV',
        'JLV',
        '基礎STR',
        '基礎AGI',
        '基礎VIT',
        '基礎INT',
        '基礎DEX',
        '基礎LUK',
        'STR',
        'AGI',
        'VIT',
        'INT',
        'DEX',
        'LUK',
        '技能後延遲',
        'ASPD',
        '攻速後延遲',
        'CRI',
        'DEF',
        'MDEF',
        '裝備表',
        # 裝備表
        '洞',
        # ATK 參數
        '武器ATK',
        '精煉ATK',
        '體型懲罰',
        '箭矢ATK',
        '屬性倍率',
        '前ATK',
        '素質ATK',
        '修練ATK',
        '鐵匠強悍ATK',
        '後ATK',
        '卡裝ATK',
        '物理全種族增傷',
        '物理惡魔增傷',
        '物理天使增傷',
        '物理植物增傷',
        '物理無形增傷',
        '物理人型增傷',
        '物理動物增傷',
        '物理魚貝增傷',
        '物理不死增傷',
        '物理龍族增傷',
        '物理昆蟲增傷',
        '物理全體型增傷',
        '物理大型增傷',
        '物理中型增傷',
        '物理小型增傷',
        '物理全屬性敵增傷',
        '物理無屬性敵增傷',
        '物理火屬性敵增傷',
        '物理水屬性敵增傷',
        '物理風屬性敵增傷',
        '物理地屬性敵增傷',
        '物理毒屬性敵增傷',
        '物理聖屬性敵增傷',
        '物理暗屬性敵增傷',
        '物理念屬性敵增傷',
        '物理不屬性敵死增傷',
        '物理全階級增傷',
        '物理一般階級增傷',
        '物理首領階級增傷',
        'ATK%',
        '遠傷',
        '近傷',
        '爆傷',
        '卡裝技能增傷',
        '技能技能增傷',
        # MATK 參數
        '武器MATK',
        '精煉MATK',
        '前MATK',
        '後MATK',
        '卡裝MATK',
        '魔法全種族增傷',
        '魔法惡魔增傷',
        '魔法天使增傷',
        '魔法植物增傷',
        '魔法無形增傷',
        '魔法人型增傷',
        '魔法動物增傷',
        '魔法魚貝增傷',
        '魔法不死增傷',
        '魔法龍族增傷',
        '魔法昆蟲增傷',
        '魔法全體型增傷',
        '魔法大型增傷',
        '魔法中型增傷',
        '魔法小型增傷',
        '魔法全屬性敵增傷',
        '魔法無屬性敵增傷',
        '魔法火屬性敵增傷',
        '魔法水屬性敵增傷',
        '魔法風屬性敵增傷',
        '魔法地屬性敵增傷',
        '魔法毒屬性敵增傷',
        '魔法聖屬性敵增傷',
        '魔法暗屬性敵增傷',
        '魔法念屬性敵增傷',
        '魔法不死屬性敵增傷',
        '全屬性魔法增傷',
        '無屬性魔法增傷',
        '火屬性魔法增傷',
        '水屬性魔法增傷',
        '風屬性魔法增傷',
        '地屬性魔法增傷',
        '毒屬性魔法增傷',
        '聖屬性魔法增傷',
        '暗屬性魔法增傷',
        '念屬性魔法增傷',
        '不死屬性魔法增傷',
        '魔法全階級增傷',
        '魔法一般階級增傷',
        '魔法首領階級增傷',
        'MATK%',
    ]

    __equipnamelist = [
        '頭上',
        '頭中',
        '頭下',
        '鎧甲',
        '武器',
        '盾',
        '披肩',
        '鞋子',
        '左飾品',
        '右飾品',
    ]


if __name__ == '__main__':
    print()
