#!/home/sxl1036/python/installing/python355/bin/python3

from bokeh.plotting import figure, output_file, show,save
output_file("test.html")
p = figure(plot_width=500,plot_height=300)
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

save(p)

