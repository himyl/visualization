## pyecharts 代码 / 效果

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("Company A", Faker.values())
    .add_yaxis("Company B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-basic-sample", subtitle="subtitle"))
    .render("bar_base.html")
)

```
<iframe width="100%" height="800px" src="Bar/bar_base.html"></iframe>
