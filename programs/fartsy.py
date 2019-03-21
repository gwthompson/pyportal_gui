from tg_gui import gui, system_handler
from tg_gui_extens.artsy import canvas

window = system_handler.request_window()
page0 = gui.page()

print(page0.width-10)
my_canvas = canvas(5,5,page0.width-10,page0.width-10,page0)

x = 0
y = 0
def smap(source):
    global x,y
    my_canvas.draw_pixel(x,y,gui.red)
    my_canvas.draw_pixel(x,y+1,gui.red)
    x +=1
    y+=2

def smoop(source):
    global x,y
    x = 0
    y = 0
    for i in range(300):
        smap(7)

but = gui.button(5, page0.width, 50, 20, 0, page0, "pixel", smoop)

#smoop(5)