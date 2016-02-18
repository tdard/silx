# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016 European Synchrotron Radiation Facility
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
"""Tests from interaction state machines"""

__authors__ = ["T. Vincent"]
__license__ = "MIT"
__date__ = "18/02/2016"


import unittest

from silx.gui.plot import Interaction


class TestInteraction(unittest.TestCase):
    def testClickOrDrag(self):
        """Minimalistic test for click or drag state machine."""
        events = []

        class TestClickOrDrag(Interaction.ClickOrDrag):
            def click(self, x, y, btn):
                events.append(('click', x, y, btn))

            def beginDrag(self, x, y):
                events.append(('beginDrag', x, y))

            def drag(self, x, y):
                events.append(('drag', x, y))

            def endDrag(self, x, y):
                events.append(('endDrag', x, y))

        clickOrDrag = TestClickOrDrag()

        # click
        clickOrDrag.handleEvent('press', 10, 10, Interaction.LEFT_BTN)
        self.assertTrue(len(events) == 0)

        clickOrDrag.handleEvent('release', 10, 10, Interaction.LEFT_BTN)
        self.assertTrue(len(events) == 1)
        self.assertEqual(events[0] == ('click', 10, 10, Interaction.LEFT_BTN))

        # drag
        events = []
        clickOrDrag.handleEvent('press', 10, 10, Interaction.LEFT_BTN)
        self.assertTrue(len(events) == 0)
        clickOrDrag.handleEvent('move', 15, 10, Interaction.LEFT_BTN)
        self.assertTrue(len(events) == 1)
        self.assertEqual(events[-1] == ('beginDrag', 15, 10))
        clickOrDrag.handleEvent('move', 20, 10, Interaction.LEFT_BTN)
        self.assertTrue(len(events) == 2)
        self.assertEqual(events[-1] == ('drag', 20, 10))
        clickOrDrag.handleEvent('release', 20, 10, Interaction.LEFT_BTN)
        self.assertTrue(len(events) == 3)
        self.assertEqual(events[-1] == ('endDrag', 20, 10))


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestInteraction))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
