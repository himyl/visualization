from pyecharts.charts import Bar
from pyecharts import options as opts

x_data = [f"November {str(i)}" for i in range(1, 12)]
y_total = [0, 900, 1245, 1530, 1376, 1376, 1511, 1689, 1856, 1495, 1292]
y_in = [900, 345, 393, "-", "-", 135, 178, 286, "-", "-", "-"]
y_out = ["-", "-", "-", 108, 154, "-", "-", "-", 119, 361, 203]


bar = (
    Bar()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_total,
        stack="total",
        itemstyle_opts=opts.ItemStyleOpts(color="rgba(0,0,0,0)"),
    )
    .add_yaxis(series_name="income", y_axis=y_in, stack="total")
    .add_yaxis(series_name="expenditure", y_axis=y_out, stack="total")
    .set_global_opts(yaxis_opts=opts.AxisOpts(type_="value"))
    .render("bar_waterfall_plot.html")
)
