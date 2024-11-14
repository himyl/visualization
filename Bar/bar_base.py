from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("company A", Faker.values())
    .add_yaxis("company B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-basic-sample", subtitle="subtitle"))
    .render("bar_base.html")
)
