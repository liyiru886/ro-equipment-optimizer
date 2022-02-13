import unittest
from src.equiplist.headgear_middle import HeadgearMiddle
from tests.testtools import TestTools


class MyTestCase(unittest.TestCase):

    ########################
    #
    #   TESTCASE： 花冠
    #
    ########################
    def test_seraphim_coronet1(self):
        equip_name = "花冠"
        stats = {
            '基礎INT': 120
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝ATK'], info['洞'])
        expected = (250, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_seraphim_coronet2(self):
        equip_name = "花冠"
        stats = {
            '基礎INT': 108
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝ATK'], info['洞'])
        expected = (115, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_seraphim_coronet3(self):
        equip_name = "花冠"
        stats = {
            '基礎INT': 1
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝ATK'], info['洞'])
        expected = (0, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_seraphim_coronet4(self):
        equip_name = "花冠"
        stats = {
            '基礎INT': 82
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝ATK'], info['洞'])
        expected = (50, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 天狗面具
    #
    ########################
    def test_crow_tengu_mask1(self):
        equip_name = "天狗面具"
        stats = {
            '基礎STR': 120
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['物理全體型增傷'], info['遠傷'], info['洞'])
        expected = (4, 7, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_crow_tengu_mask2(self):
        equip_name = "天狗面具"
        stats = {
            '基礎STR': 109
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['物理全體型增傷'], info['遠傷'], info['洞'])
        expected = (2, 4, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_crow_tengu_mask3(self):
        equip_name = "天狗面具"
        stats = {
            '基礎STR': 107
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['物理全體型增傷'], info['遠傷'], info['洞'])
        expected = (1, 2, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 英雄面具
    #
    ########################
    def test_mask_of_hero(self):
        stats = None
        equip_name = "英雄面具"
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['VIT'], info['MDEF'], info['洞'])
        expected = (10, 10, 0)

        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 男爵眼罩
    #
    ########################
    def test_barons_evil_eye(self):
        stats = None
        equip_name = "男爵眼罩"
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['技能後延遲'], info['洞'])
        expected = (5, 0)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 太陽眼鏡[1]
    #
    ########################
    def test_sunglasses(self):
        stats = None
        equip_name = "太陽眼鏡[1]"
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['洞'])
        expected = 1
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 影子助推器[1]
    #
    ########################
    def test_shadow_booster(self):
        stats = None
        equip_name = "影子推助器[1]"
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['ASPD'], info['技能後延遲'], info['洞'])
        expected = (1, 1, 1)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 柯耳
    #
    ########################
    def test_kardui_ear1(self):
        equip_name = "柯耳"
        stats = {
            '基礎DEX': 120
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝MATK'], info['洞'])
        expected = (184, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_kardui_ear2(self):
        equip_name = "柯耳"
        stats = {
            '基礎DEX': 110
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝MATK'], info['洞'])
        expected = (82, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_kardui_ear3(self):
        equip_name = "柯耳"
        stats = {
            '基礎DEX': 107
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝MATK'], info['洞'])
        expected = (20, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_kardui_ear4(self):
        equip_name = "柯耳"
        stats = {
            '基礎DEX': 1
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝MATK'], info['洞'])
        expected = (0, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 帝國羽翼
    #
    ########################
    def test_imperial_feather(self):
        equip_name = "帝國羽翼"
        stats = {
            '基礎AGI': 107
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['ASPD'], info['攻速後延遲'], info['洞'])
        expected = (0, 1, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_imperial_feather2(self):
        equip_name = "帝國羽翼"
        stats = {
            '基礎AGI': 108
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['ASPD'], info['攻速後延遲'], info['洞'])
        expected = (1, 2, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 賭徒之印
    #
    ########################
    def test_gambler_seal1(self):
        equip_name = "賭徒之印"
        stats = {
            '基礎DEX': 51,
            '基礎LUK': 107,
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝ATK'], info['卡裝MATK'], info['CRI'], info['爆傷'], info['洞'])
        expected = (20, 20, 13, -7, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_gambler_seal2(self):
        equip_name = "賭徒之印"
        stats = {
            '基礎DEX': 101,
            '基礎LUK': 108,
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝ATK'], info['卡裝MATK'], info['CRI'], info['爆傷'], info['洞'])
        expected = (20, 20, 18, -7, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_gambler_seal3(self):
        equip_name = "賭徒之印"
        stats = {
            '基礎DEX': 102,
            '基礎LUK': 120,
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['卡裝ATK'], info['卡裝MATK'], info['CRI'], info['爆傷'], info['洞'])
        expected = (24, 24, 30, 10, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 愛情紅暈
    #
    ########################
    def test_costume_love_cheeks1(self):
        equip_name = "愛情紅暈"
        stats = {
            '基礎STR': 120,
            '基礎LUK': 120,
            '基礎INT': 120,
            '基礎DEX': 120,
            '基礎AGI': 120,
            '基礎VIT': 120,
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['物理全階級增傷'], info['CRI'], info['爆傷'], info['卡裝MATK'], info['攻速後延遲'], info['乘算MHP加成'], info['洞'])
        expected = (2, 10, 4, 30, 4, 4, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_costume_love_cheeks2(self):
        equip_name = "愛情紅暈"
        stats = {
            '基礎STR': 61,
            '基礎LUK': 62,
            '基礎INT': 63,
            '基礎DEX': 64,
            '基礎AGI': 65,
            '基礎VIT': 66,
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['物理全階級增傷'], info['CRI'], info['爆傷'], info['卡裝MATK'], info['攻速後延遲'], info['乘算MHP加成'], info['洞'])
        expected = (1, 5, 2, 15, 2, 2, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    ########################
    #
    #   TESTCASE： 魔力之星
    #
    ########################
    def test_magic_star(self):
        equip_name = "魔力之星"
        stats = {
            '基礎STR': 61,
            '基礎LUK': 62,
            '基礎INT': 63,
            '基礎DEX': 64,
            '基礎AGI': 65,
            '基礎VIT': 66,
        }
        test = HeadgearMiddle()
        info = test.equip_info(equip_name, stats)
        result = (info['無屬性魔法增傷'], info['風屬性魔法增傷'], info['水屬性魔法增傷'],
                  info['火屬性魔法增傷'], info['地屬性魔法增傷'], info['聖屬性魔法增傷'], info['洞'])
        expected = (10, 10, 10, 10, 10, 10, 0)
        TestTools.verify_statsname(stats)
        TestTools.verify_statsname(info.keys())
        self.assertEqual(expected, result)

    def test_list_magic_equip(self):
        test = HeadgearMiddle()
        result = test.list_magic_equip
        expected = ['柯耳', '魔力之星', '英雄面具', '男爵眼罩', '太陽眼鏡[1]', '影子推助器[1]', '愛情紅暈']
        self.assertEqual(expected, result)

    def test_list_phy_equip(self):
        test = HeadgearMiddle()
        result = test.list_phy_equip
        expected = ['花冠', '天狗面具', '帝國羽翼', '賭徒之印', '英雄面具', '男爵眼罩', '太陽眼鏡[1]', '影子推助器[1]', '愛情紅暈']
        self.assertEqual(expected, result)

    def test_list_all(self):
        test = HeadgearMiddle()
        result = test.list_all
        expected = ['花冠', '天狗面具', '帝國羽翼', '賭徒之印', '柯耳', '魔力之星', '英雄面具', '男爵眼罩', '太陽眼鏡[1]', '影子推助器[1]', '愛情紅暈']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
