# -*- coding: utf-8 -*-
import os
import random


class _Faker:
    clothes = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    drinks = ["可乐", "雪碧", "橙汁", "绿茶", "奶茶", "百威", "青岛"]
    phones = ["小米", "三星", "华为", "苹果", "魅族", "VIVO", "OPPO"]
    fruits = ["草莓", "芒果", "葡萄", "雪梨", "西瓜", "柠檬", "车厘子"]
    animal = ["河马", "蟒蛇", "老虎", "大象", "兔子", "熊猫", "狮子"]
    cars = ["宝马", "法拉利", "奔驰", "奥迪", "大众", "丰田", "特斯拉"]
    dogs = ["哈士奇", "萨摩耶", "泰迪", "金毛", "牧羊犬", "吉娃娃", "柯基"]
    week = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    week_en = "Saturday Friday Thursday Wednesday Tuesday Monday Sunday".split()
    clock = ("12a 1a 2a 3a 4a 5a 6a 7a 8a 9a 10a 11a 12p "
             "1p 2p 3p 4p 5p 6p 7p 8p 9p 10p 11p".split())
    visual_color = ["#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#ffffbf", "#fee090", "#fdae61", "#f46d43",
                    "#d73027", "#a50026", ]
    months = ["{}月".format(i) for i in range(1, 13)]
    provinces = ["北京", "天津", "上海", "重庆"]
    beijing_districts = ["东城区", "西城区", "石景山区", "丰台区", "海淀区", "朝阳区", "通州区", "平谷区", "顺义区", "大兴区", "昌平区", "门头沟区", "房山区",
                         "延庆区", "怀柔区", "密云区"]
    tianjin_districts = ["和平区", "南开区", "河西区", "河东区", "河北区", "红桥区", "东丽区", "西青区", "津南区", "北辰区", "武清区", "宝坻区", "滨海新区",
                         "宁河区", "静海区", "蓟州区"]
    shanghai_districts = ["黄浦区", "徐汇区", "长宁区", "静安区", "普陀区", "虹口区", "杨浦区", "闵行区", "宝山区", "嘉定区", "浦东新区", "金山区", "松江区",
                          "青浦区", "奉贤区", "崇明区"]
    chongqing_districts = ["万州区", "涪陵区", "渝中区", "大渡口区", "江北区", "沙坪坝区", "九龙坡区", "南岸区", "北碚区", "綦江区", "大足区", "渝北区", "巴南区",
                           "黔江区", "长寿区", "江津区", "合川区", "永川区", "南川区", "璧山区", "铜梁区", "潼南区", "荣昌区", "开州区", "梁平区", "武隆区",
                           "城口县", "丰都县", "垫江县", "忠县", "云阳县", "奉节县", "巫山县", "巫溪县", "石柱土家族自治县", "秀山土家族苗族自治县",
                           "酉阳土家族苗族自治县", "彭水苗族土家族自治县"]
    days_attrs = ["{}天".format(i) for i in range(30)]
    days_values = [random.randint(1, 30) for _ in range(30)]

    def choose(self) -> list:
        return random.choice([self.clothes, self.drinks, self.phones, self.fruits, self.animal, self.dogs, self.week, ])

    @staticmethod
    def values(start: int = 20, end: int = 150) -> list:
        return [random.randint(start, end) for _ in range(7)]

    @staticmethod
    def rand_color():
        return random.choice(
            ["#c23531", "#2f4554", "#61a0a8", "#d48265", "#749f83", "#ca8622", "#bda29a", "#6e7074", "#546570",
             "#c4ccd3", "#f05b72", "#444693", "#726930", "#b2d235", "#6d8346", "#ac6767", "#1d953f", "#6950a1", ])

    @staticmethod
    def img_path(path: str, prefix: str = "images") -> str:
        return os.path.join(prefix, path)


Faker = _Faker()


class Collector:
    charts = []

    @staticmethod
    def funcs(fn):
        Collector.charts.append((fn, fn.__name__))


