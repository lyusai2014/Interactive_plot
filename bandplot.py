#!/home/sxl1036/python/installing/python355/bin/python3

from bokeh.plotting import figure, output_file, show,save
output_file("structure.html")

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉") # subscript
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


p = figure(title='BeGeN2'.translate(SUB),plot_width=500,plot_height=300, y_axis_label='Energy (eV)')

import numpy as np

data =np.genfromtxt('BNDS.DAT', delimiter='\t')

nband=len(data[0,:])
#print (nband)
for i in range(nband-1):
   p.line(data[:,0],data[:,i+1],line_width=1.5,color='red')

p.line([0,0],[-19,16])
p.line([1,1],[-19,16])
p.line([2.2202,2.2202],[-19,16])
p.line([3.2202,3.2202],[-19,16])
p.line([4.3673,4.3673],[-19,16])
p.line([5.5875,5.5875],[-19,16])
p.line([6.5875,6.5875],[-19,16])
p.line([7.7345,7.7345],[-19,16])
p.line([0,7.7345],[0,0])

p.line([0,7.7345],[-19,-19])
p.line([0,7.7345],[16,16])

GG=str(u'\u0393') #unicode of \Gamma
#print (GG)
p.xaxis.ticker = [ 0,1,2.2202,3.2202,4.3673,5.5875,6.5875,7.7345]
p.xaxis.major_label_overrides = {0:'X',1:GG,2.2202:'Z',3.2202:'U',4.3673:'R',5.5875:'S',6.5875:'Y',7.7345:GG}

save(p)

