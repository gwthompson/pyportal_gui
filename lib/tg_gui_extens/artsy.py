# The MIT License (MIT)
#
# Copyright (c) 2019 Jonah Yolles-Murphy
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
from tg_gui.gui import widget, round_rect, default_color, white, good_gap_size

class canvas(widget):

    def __init__(self, *args, border = good_gap_size, border_color = default_color, color = white):
        super().__init__(*args)
        #print(*args)
        self._border = border
        self._border_color = border_color
        self._color = color

    def place(self):
        super().place()
        #print(self.width)
        round_rect( self.physical_x,
                    self.physical_y,
                    self.width, self.height, 0,
                    self._border_color)
        self.clear()


    def draw_pixel(self, x, y, color):
        if 0<x<self.width-self._border*2 and 0<y<self.height-self._border*2:
            round_rect( self.physical_x + self._border + x,
                        self.physical_y + self.height -self._border -y,
                        1, 1, 0, color)

    def clear(self):
        round_rect( self.physical_x + self._border,
                    self.physical_y + self._border,
                    self.width - self._border*2,
                    self.height - self._border*2,
                    0, self._color)