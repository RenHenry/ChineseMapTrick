# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map
from Faker import Faker


def map_beijing() -> Map:
    c = (Map().add("随机数字", [list(z) for z in zip(Faker.beijing_districts, Faker.values())], "北京").set_global_opts(
        title_opts=opts.TitleOpts(title="Map-北京地图"), visualmap_opts=opts.VisualMapOpts(), ))
    return c

def map_tianjin() -> Map:
    c = (Map().add("随机数字", [list(z) for z in zip(Faker.tianjin_districts, Faker.values())], "天津").set_global_opts(
        title_opts=opts.TitleOpts(title="Map-天津地图"), visualmap_opts=opts.VisualMapOpts(), ))
    return c


if __name__ == "__main__":
    map_beijing().render("beijing.html")
    map_tianjin().render("tianjin.html")
