# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/
"""This script shows the features of a colormap dialog.
"""

__authors__ = ["V. Valls"]
__license__ = "MIT"
__date__ = "04/01/2018"

import functools

from silx.gui import qt

from silx.gui.plot.ColormapDialog import ColormapDialog
from silx.gui.plot.Colormap import Colormap
from silx.gui.plot.ColorBar import ColorBarWidget


class ColormapDialogExample(qt.QMainWindow):
    """PlotWidget with an ad hoc toolbar and a colorbar"""

    def __init__(self, parent=None):
        super(ColormapDialogExample, self).__init__(parent)
        self.setWindowTitle("Colormap dialog example")

        self.colormap1 = Colormap("viridis")
        self.colormap2 = Colormap("gray")

        self.colorBar = ColorBarWidget(self)

        self.colorDialogs = []

        options = qt.QWidget(self)
        options.setLayout(qt.QVBoxLayout())
        self.createOptions(options.layout())

        mainWidget = qt.QWidget(self)
        mainWidget.setLayout(qt.QHBoxLayout())
        mainWidget.layout().addWidget(options)
        mainWidget.layout().addWidget(self.colorBar)
        self.mainWidget = mainWidget

        self.setCentralWidget(mainWidget)
        self.createColorDialog()

    def createOptions(self, layout):
        button = qt.QPushButton("Create a new dialog")
        button.clicked.connect(self.createColorDialog)
        layout.addWidget(button)

        layout.addSpacing(10)

        button = qt.QPushButton("Set colormap 1")
        button.clicked.connect(self.setColormap1)
        layout.addWidget(button)
        button = qt.QPushButton("Set colormap 2")
        button.clicked.connect(self.setColormap2)
        layout.addWidget(button)
        button = qt.QPushButton("Create new colormap")
        button.clicked.connect(self.setNewColormap)
        layout.addWidget(button)

        layout.addSpacing(10)

        button = qt.QPushButton("Set no histogram")
        button.clicked.connect(self.setNoHistogram)
        layout.addWidget(button)
        button = qt.QPushButton("Set positive histogram")
        button.clicked.connect(self.setPositiveHistogram)
        layout.addWidget(button)
        button = qt.QPushButton("Set neg-pos histogram")
        button.clicked.connect(self.setNegPosHistogram)
        layout.addWidget(button)
        button = qt.QPushButton("Set negative histogram")
        button.clicked.connect(self.setNegativeHistogram)
        layout.addWidget(button)

        layout.addSpacing(10)

        button = qt.QPushButton("Set no range")
        button.clicked.connect(self.setNoRange)
        layout.addWidget(button)
        button = qt.QPushButton("Set positive range")
        button.clicked.connect(self.setPositiveRange)
        layout.addWidget(button)
        button = qt.QPushButton("Set neg-pos range")
        button.clicked.connect(self.setNegPosRange)
        layout.addWidget(button)
        button = qt.QPushButton("Set negative range")
        button.clicked.connect(self.setNegativeRange)
        layout.addWidget(button)

        layout.addStretch()

    def createColorDialog(self):
        newDialog = ColormapDialog(self)
        newDialog.finished.connect(functools.partial(self.removeColorDialog, newDialog))
        self.colorDialogs.append(newDialog)
        self.mainWidget.layout().addWidget(newDialog)

    def removeColorDialog(self, dialog):
        self.colorDialogs.remove(dialog)

    def setColormap1(self):
        self.colorBar.setColormap(self.colormap1)
        for dialog in self.colorDialogs:
            dialog.setColormap(self.colormap1)

    def setColormap2(self):
        self.colorBar.setColormap(self.colormap2)
        for dialog in self.colorDialogs:
            dialog.setColormap(self.colormap2)

    def setNewColormap(self):
        self.colormap = Colormap("inferno")
        self.colorBar.setColormap(self.colormap)
        for dialog in self.colorDialogs:
            dialog.setColormap(self.colormap)

    def setNoHistogram(self):
        for dialog in self.colorDialogs:
            dialog.setHistogram()

    def setPositiveHistogram(self):
        histo = [5, 10, 50, 10, 5]
        pos = 1
        edges = list(range(pos, pos + len(histo)))
        for dialog in self.colorDialogs:
            dialog.setHistogram(histo, edges)

    def setNegPosHistogram(self):
        histo = [5, 10, 50, 10, 5]
        pos = -2
        edges = list(range(pos, pos + len(histo)))
        for dialog in self.colorDialogs:
            dialog.setHistogram(histo, edges)

    def setNegativeHistogram(self):
        histo = [5, 10, 50, 10, 5]
        pos = -30
        edges = list(range(pos, pos + len(histo)))
        for dialog in self.colorDialogs:
            dialog.setHistogram(histo, edges)

    def setNoRange(self):
        for dialog in self.colorDialogs:
            dialog.setDataRange()

    def setPositiveRange(self):
        for dialog in self.colorDialogs:
            dialog.setDataRange(1, 1, 10)

    def setNegPosRange(self):
        for dialog in self.colorDialogs:
            dialog.setDataRange(-10, 1, 10)

    def setNegativeRange(self):
        for dialog in self.colorDialogs:
            dialog.setDataRange(-10, float("nan"), -1)


def main():
    app = qt.QApplication([])

    # Create the ad hoc plot widget and change its default colormap
    example = ColormapDialogExample()
    example.show()

    app.exec_()


if __name__ == '__main__':
    main()
