import math


class HeadgearMiddle:
    # TODO: 套裝效果皆未實作
    def __init__(self):
        self.__switch_phy = {
            "花冠": self.__seraphim_coronet,
            "天狗面具": self.__crow_tengu_mask,
            "帝國羽翼": self.__imperial_feather,
            "賭徒之印": self.__gambler_seal,

        }
        self.__switch_magic = {
            "柯耳": self.__kardui_ear,
            "魔力之星": self.__magic_star,

        }
        self.__switch_common = {
            "英雄面具": self.__mask_of_hero,
            "男爵眼罩": self.__barons_evil_eye,
            "太陽眼鏡[1]": self.__sunglasses,
            "影子推助器[1]": self.__shadow_booster,
            "愛情紅暈": self.__costume_love_cheeks,

        }

        self.__switch_all = {}
        self.__switch_all.update(self.__switch_phy)
        self.__switch_all.update(self.__switch_magic)
        self.__switch_all.update(self.__switch_common)

        self.__phy_list = list(self.__switch_phy.keys()) + list(self.__switch_common.keys())  # 物理裝備清單
        self.__magic_list = list(self.__switch_magic.keys()) + list(self.__switch_common.keys())  # 魔法裝備清單
        self.__all_list = list(self.__switch_all.keys())

    def __magic_star(self, stats):
        m_neutral_property_multiplier = math.floor(stats['基礎STR'] / 12) * 2
        m_wind_property_multiplier = math.floor(stats['基礎AGI'] / 12) * 2
        m_water_property_multiplier = math.floor(stats['基礎VIT'] / 12) * 2
        m_fire_property_multiplier = math.floor(stats['基礎INT'] / 12) * 2
        m_earth_property_multiplier = math.floor(stats['基礎DEX'] / 12) * 2
        m_holy_property_multiplier = math.floor(stats['基礎LUK'] / 12) * 2
        output = {'無屬性魔法增傷': m_neutral_property_multiplier,
                  '風屬性魔法增傷': m_wind_property_multiplier,
                  '水屬性魔法增傷': m_water_property_multiplier,
                  '火屬性魔法增傷': m_fire_property_multiplier,
                  '地屬性魔法增傷': m_earth_property_multiplier,
                  '聖屬性魔法增傷': m_holy_property_multiplier,
                  '洞': 0,
                  }
        return output

    def __costume_love_cheeks(self, stats):
        sl = math.floor((stats['基礎STR'] + stats['基礎LUK']) / 120)
        inde = math.floor((stats['基礎INT'] + stats['基礎DEX']) / 120)
        av = math.floor((stats['基礎AGI'] + stats['基礎VIT']) / 120)
        p_class_multiplier = sl
        cri = sl * 5
        critical_multiplier = sl * 2
        matk = inde * 15
        aspd_p = av * 2
        mhp_p = av * 2
        output = {'物理全階級增傷': p_class_multiplier,
                  'CRI': cri,
                  '爆傷': critical_multiplier,
                  '卡裝MATK': matk,
                  '攻速後延遲': aspd_p,
                  '乘算MHP加成': mhp_p,
                  '洞': 0,
                  }
        return output

    def __gambler_seal(self, stats):
        CRI = 3 + math.floor(stats['基礎LUK'] / 10)
        critical_multiplier = 3 - math.floor(stats['基礎DEX'] / 10) * 2
        atk = math.floor(stats['基礎LUK'] / 10) * 2
        matk = math.floor(stats['基礎LUK'] / 10) * 2
        if stats['基礎LUK'] >= 108:
            CRI = CRI + 5
            critical_multiplier = critical_multiplier + 10
        if stats['基礎LUK'] >= 120:
            CRI = CRI + 10
            critical_multiplier = critical_multiplier + 17
        output = {'卡裝ATK': atk,
                  '卡裝MATK': matk,
                  'CRI': CRI,
                  '爆傷': critical_multiplier,
                  '洞': 0,
                  }
        return output

    def __imperial_feather(self, stats):
        ASPD_n = 0
        ASPD_p = 1
        if stats['基礎AGI'] >= 108:
            ASPD_n = 1
            ASPD_p = ASPD_p + 1
        output = {'ASPD': ASPD_n,
                  '攻速後延遲': ASPD_p,
                  '洞': 0,
                  }
        return output

    def __kardui_ear(self, stats):
        matk = math.floor(stats['基礎DEX'] / 10) * 2
        if stats['基礎DEX'] >= 108:
            matk = matk + 60
        if stats['基礎DEX'] >= 120:
            matk = matk + 100
        output = {'卡裝MATK': matk,
                  '洞': 0,
                  }
        return output

    def __shadow_booster(self, stats):
        output = {'ASPD': 1,
                  '技能後延遲': 1,
                  '洞': 1,
                  }
        return output

    def __sunglasses(self, stats):
        output = {'洞': 1,
                  }
        return output

    def __barons_evil_eye(self, stats):
        output = {'技能後延遲': 5,
                  '洞': 0,
                  }
        return output

    def __mask_of_hero(self, stats):
        output = {'VIT': 10,
                  'MDEF': 10,
                  '洞': 0,
                  }
        return output

    def __crow_tengu_mask(self, stats):
        p_size_multiplier = 1
        long_ranged_multiplier = 2
        if stats['基礎STR'] >= 108:
            p_size_multiplier = p_size_multiplier + 1
            long_ranged_multiplier = long_ranged_multiplier + 2
        if stats['基礎STR'] >= 120:
            p_size_multiplier = p_size_multiplier + 2
            long_ranged_multiplier = long_ranged_multiplier + 3
        output = {'物理全體型增傷': p_size_multiplier,
                  '遠傷': long_ranged_multiplier,
                  '洞': 0,
                  }
        return output

    def __seraphim_coronet(self, stats):
        d = {'STR': 2
             }
        atk = math.floor(stats['基礎INT'] / 8) * 5
        if stats['基礎INT'] >= 108:
            atk = atk + 50
        if stats['基礎INT'] >= 120:
            atk = atk + 125
        output = {'卡裝ATK': atk,
                  '洞': 0,
                  }
        return output

    def equip_info(self, equip_name, stats):
        return self.__switch_all.get(equip_name)(stats)

    @property
    def list_magic_equip(self):
        return self.__magic_list

    @property
    def list_phy_equip(self):
        return self.__phy_list

    @property
    def list_all(self):
        return self.__all_list


if __name__ == '__main__':
    print()
    test = HeadgearMiddle()
    print(test.list_phy_equip)
    print(test.list_magic_equip)
    print(test.list_all)
