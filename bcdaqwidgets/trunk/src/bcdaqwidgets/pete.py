#!/usr/bin/env python

import epics

TIME_PV = 'S:SRtimeCP'
CURRENT_PV = 'S:SRcurrentCP'


###################################################################################

import sys
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import pylab

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide import QtCore, QtGui

from MatplotlibWidget import MatplotlibWidget


def getData():
    xpv = epics.PV(TIME_PV)
    ypv = epics.PV(CURRENT_PV)
    if xpv.connected and ypv.connected:
        x, y = xpv.value, ypv.value
    else:
        with open('aps_data.txt', 'r') as fp:
            buf = [map(float,xypair.split()) for xypair in fp.read().splitlines()[3:]]
        x, y = zip(*buf)
    return x, y


class MplWidget(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        
        widget = MatplotlibWidget()
        layout.addWidget(widget)
        
        time_data, current_data = getData()
        p1, = widget.axes.plot(time_data, current_data, 'r-', label='history')
        # TODO: learn how to plot two or more data on one graph
        # TODO: learn how to add a data set later
        #widget.axes.plot(time_data, current_data, [-5, -2], [1,20])
        #p2, = widget.axes.plot([-5, -2], [1,20], 'bo-', label='2 points')
        #widget.axes.legend([p1, p2], ['history', '2 points'])
        widget.axes.set_title('APS Storage Ring 24-hour History')
        widget.axes.set_xlabel('t, hr')
        widget.axes.set_ylabel('current, mA')
        widget.axes.grid(True)
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
        print 'on_figure_enter: %s' % str(event.canvas.figure)
        self.default_color['figure'] = event.canvas.figure.get_facecolor()
        event.canvas.figure.set_facecolor('bisque')
        event.canvas.draw()
        
    def on_figure_leave(self, event):
        print 'on_figure_leave: %s' % str(event.canvas.figure)
        if self.default_color['figure'] is not None:
            event.canvas.figure.set_facecolor(self.default_color['figure'])
        event.canvas.draw()
        
    def on_axes_enter(self, event):
        print 'on_axes_enter: %s, x=%d, y=%d, xdata=%f, ydata=%f' % (
                str(event.inaxes), event.x, event.y, event.xdata, event.ydata)
        self.default_color['axes'] = event.inaxes.patch.get_facecolor()
        event.inaxes.patch.set_facecolor('mintcream')
        event.canvas.draw()
        
    def on_axes_leave(self, event):
        print 'on_axes_leave: %s, x=%d, y=%d, xdata=%f, ydata=%f' % (
                str(event.inaxes), event.x, event.y, event.xdata, event.ydata)
        if self.default_color['axes'] is not None:
            event.inaxes.patch.set_facecolor(self.default_color['axes'])
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
        x, y = getData()
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
