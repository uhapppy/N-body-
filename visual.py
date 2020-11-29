from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys



from pathlib import Path
from scipy.stats import kde




data = Path("C:/Users/JF/source/repos/NBodyC++/NBodyC++/")
dataopen=data/"gravity.cvs"
gravity=open(dataopen)
a= np.loadtxt(gravity,delimiter=",")
n=0
n2=1000 #should be equal to nombredeplanete
nombreplanete=1000
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.setGeometry(0, 110, 1920, 1080)
w.show()
#g = gl.GLGridItem()
#w.addItem(g)

#generate random points from -10 to 10, z-axis positive
pos = a[n:n2]
sp2=gl.GLScatterPlotItem(pos=pos , size=2)
w.addItem(sp2)

def update():
    global n
    global n2
    global nombreplanete 
    n+=nombreplanete
    n2+=nombreplanete
    sp2.setData(pos=a[n:n2])
    

    
t = QtCore.QTimer()
t.timeout.connect(update)
t.start(40)




## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
