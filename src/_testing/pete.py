#!/usr/bin/env python


import sys
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PyQt4'
import pylab

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt4 import QtCore, QtGui

from MatplotlibWidget import MatplotlibWidget
import epics
import datetime
import time


TIME_PV = 'S:SRtimeCP'
CURRENT_PV = 'S:SRcurrentCP'


def _readAsciiData():
    ''''read test data from text file'''
    with open('aps_data.txt', 'r') as fp:
        buf = fp.read()
    x, y = [], []
    for line in buf.splitlines():
        line = line.strip()
        if len(line) > 0 and not line.startswith('#'):  # skip any comment lines
            try:
                fx, fy = map(float, line.split())
                x.append(fx)
                y.append(fy)
            except:
                pass
    timestamp = '2013-07-09 15:00:00'       # approximate
    epoch = time.mktime(time.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))
    return epoch, x, y


def _readXmlData():
    ''''read test data from XML file'''
    import xml.etree.cElementTree as ElementTree
    root = ElementTree.parse('aps_data.xml').getroot()
    timestamp = root.attrib['datetime']
    epoch = time.mktime(time.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))
    x = map(float, root.find('time').text.strip().split())
    y = map(float, root.find('current').text.strip().split())
    return epoch, x, y


def getTestData():
    '''get some test data, either from EPICS or a local data file'''
    xpv = epics.PV(TIME_PV)
    ypv = epics.PV(CURRENT_PV)
    if xpv.connected and ypv.connected:
        x, y = xpv.value, ypv.value
        epoch = time.mktime(time.gmtime())
    else:
        #epoch, x, y = _readAsciiData()
        epoch, x, y = _readXmlData()
    return epoch, x, y


class MplWidget(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        
        widget = MatplotlibWidget(title='APS Storage Ring 24-hour History',
                                  xlabel='time before now, ht',
                                  ylabel='',
                                  hold=True,
                                  showgrid=True,
                                  #xticks=[-24,-18,-6,0],
                                  yticks=[0,25,50,75,100],
                                  )
        layout.addWidget(widget)
        
        epoch, time_data, current_data = getTestData()
        widget.addPlot(time_data, current_data, 'r-',  label='history')
        widget.addPlot([-5, -2],  [1,20],       'bo-', label='2 points')
        widget.axes.legend()
        '''
        MatPlotLib mouse events
        
        http://matplotlib.org/users/event_handling.html
        
        example handling:
        
        >>> print event
        MPL MouseEvent: xy=(492,105) xydata=(-4.23387096774,25.71875) button=1 dblclick=False inaxes=Axes(0.125,0.1;0.775x0.363636)
        '''
        self.default_color = dict(figure=None, axes=None)
        widget.mpl_connect('button_press_event', self.on_button_press)
        widget.mpl_connect('button_release_event', self.on_button_release)
        widget.mpl_connect('figure_enter_event', self.on_figure_enter)
        widget.mpl_connect('figure_leave_event', self.on_figure_leave)
        widget.mpl_connect('axes_enter_event', self.on_axes_enter)
        widget.mpl_connect('axes_leave_event', self.on_axes_leave)
        
    # changing colors and print text to demo the handlers
    # TODO: replace demo code with real functions such as a proper zoom stack
    def on_button_press(self, event):
        print 'on_button_press: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % (
                event.button, event.x, event.y, event.xdata, event.ydata)
        
    def on_button_release(self, event):
        print 'on_button_release: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % (
                event.button, event.x, event.y, event.xdata, event.ydata)
        
    def on_figure_enter(self, event):
        fig = event.canvas.figure
        print 'on_figure_enter: %s' % str(fig)
        if self.default_color['figure'] is None:
            self.default_color['figure'] = fig.get_facecolor()
        fig.set_facecolor('bisque')
        event.canvas.draw()
        
    def on_figure_leave(self, event):
        fig = event.canvas.figure
        print 'on_figure_leave: %s' % str(fig)
        if self.default_color['figure'] is not None:
            fig.set_facecolor(self.default_color['figure'])
        event.canvas.draw()
        
    def on_axes_enter(self, event):
        axes = event.inaxes
        print 'on_axes_enter: %s, x=%d, y=%d, xdata=%f, ydata=%f' % (
                str(axes), event.x, event.y, event.xdata, event.ydata)
        if self.default_color['axes'] is None:
            self.default_color['axes'] = axes.patch.get_facecolor()
        axes.patch.set_facecolor('#ccccff')
        event.canvas.draw()
        
    def on_axes_leave(self, event):
        axes = event.inaxes
        print 'on_axes_leave: %s, x=%d, y=%d, xdata=%f, ydata=%f' % (
                str(axes), event.x, event.y, event.xdata, event.ydata)
        if self.default_color['axes'] is not None:
            axes.patch.set_facecolor(self.default_color['axes'])
        event.canvas.draw()



class PlotMyWay(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        
        fig = Figure()
        fig.suptitle('matplotlib testing')
        xpv = epics.PV(TIME_PV)
        ypv = epics.PV(CURRENT_PV)
        epoch, x, y = getTestData()
        ax = fig.add_subplot(111)
        ax.set_xlabel('time since now, hours')
        ax.set_ylabel('APS storage ring current, mA')
        ax.set_title('APS Storage Ring 24-hour History')
        ax.grid(True)
        ax.plot(x, y, 'r-')
        layout.addWidget( FigureCanvas(fig) )
        fig.canvas.mpl_connect('button_release_event', self.on_button_release)
        
    def on_button_release(self, event):
        '''MatPlotLib mouse event
        
        http://matplotlib.org/users/event_handling.html
        
        MPL MouseEvent: xy=(492,105) xydata=(-4.23387096774,25.71875) button=1 dblclick=False inaxes=Axes(0.125,0.1;0.775x0.363636)
        '''
        print event


def makeFigure():
    # generate the plot
    fig = Figure(figsize=(600,600), dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
    ax = fig.add_subplot(111)
    ax.plot([0,1])
    return fig


def main():
    app = QtGui.QApplication(sys.argv)
    canvas = FigureCanvas(makeFigure())    # generate the canvas to display the plot
    win = QtGui.QMainWindow()
    win.setCentralWidget(canvas)           # add the plot canvas to a window
    win.show()
    sys.exit(app.exec_())


def myway():
    app = QtGui.QApplication(sys.argv)
    view = PlotMyWay()
    view.show()
    sys.exit(app.exec_())


def mplw():
    app = QtGui.QApplication(sys.argv)
    view = MplWidget()
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    #main()
    #myway()
    mplw()
