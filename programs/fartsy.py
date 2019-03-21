from tg_gui import gui, system_handler
from tg_gui_extens.artsy import canvas

window = system_handler.request_window()
page0 = gui.page()

print(page0.width-10)
my_canvas = canvas(5,5,page0.width-10,page0.width-10,page0)

x = 1
y = 1
def smap(source):
    global x,y
    my_canvas.draw(x,y,gui.red)
    x +=1
    y+=1

def smoop(source):
    for i in range(300):
        smap(7)

but = gui.button(5, page0.width, 50, 20, 0, page0, "pixel", smoop)

#smoop(5)