import numpy as np
import matplotlib as mpl
mpl.use('pgf')
def p2I(x):
	return x/72

golden_mean = (np.sqrt(5)-1.0)/2.0

fig_width = p2I(246)
fig_height = fig_width*golden_mean

params = {
    "pgf.texsystem": "pdflatex", 						#Use PdfLaTeX as system
	"text.usetex": True, 								#Render Text with Latex
	"text.latex.unicode": True,
	
	"font.family": "serif",
	
	"text.antialiased" : False,
	
	"pgf.rcfonts": False, 								#Let Document Control Fonts

	"pgf.preamble": [									#Preamble for PGF, should be the same as the document you are using
         r"\usepackage[utf8x]{inputenc}",
         r"\usepackage[T1]{fontenc}",
		 r"\usepackage[final]{microtype}",
		 r"\usepackage[USenglish]{babel}",
		 r"\usepackage{newtxtext}",
		 r"\usepackage{amsmath}",
		 r"\usepackage{newtxmath}",
         ],
		 
	"font.size": 12,									#Global Font Size
	"xtick.labelsize" : 10,								#XTick Font Size
	"ytick.labelsize" : 10,								#YTick Font Size
	
	"lines.linewidth" : 1.5,
	"axes.linewidth"  : 1,
	"axes.formatter.useoffset" : True,
	"axes.xmargin" : 0,
	"axes.ymargin" : 0,
	
	"xtick.direction" : 'in',
	"ytick.direction" : 'in',
	
	
	
	"figure.figsize": [fig_width,fig_height],
	"figure.autolayout": False,
}
mpl.rcParams.update(params)
import matplotlib.pyplot as plt



x = np.linspace(0,10,1000)
y = np.sqrt(.5+np.square(x)-np.sqrt(np.square(.5+np.square(x))-np.square(x)))
const = np.full(1000, 1/np.sqrt(2))
plt.plot(x,y,'k')
plt.plot(x, const, 'k--')

plt.ylim(0,1)
plt.xlim(0,3)
plt.xlabel(r'Fuck $q$')
plt.ylabel(r'$\omega(q)$')
plt.xticks([0,1,2,3],[r'\hspace*{-8pt}$0$',r'$\frac{\omega_\mathrm{p}}{c}$',r'$\frac{2\omega_\mathrm{p}}{c}$',r'$\frac{3\omega_\mathrm{p}}{c}$'])
plt.yticks([.25, .5, 1/np.sqrt(2),1], [r'$\frac{\omega_\mathrm{p}}{4}$',r'$\frac{\omega_\mathrm{p}}{2}$',r'$\frac{\omega_\mathrm{p}}{\sqrt{2}}$',r'$\omega_\mathrm{p}$'])

plt.savefig(r'3c-1.pgf', bbox_inches="tight")
plt.savefig('example.pdf', bbox_inches="tight")


