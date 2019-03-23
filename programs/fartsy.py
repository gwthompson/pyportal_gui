from tg_gui import gui, system_handler
from tg_gui_extens.artsy import canvas

window = system_handler.request_window()
page0 = gui.page()

print(page0.width-10)
my_canvas = canvas(5,5,page0.width-10,page0.width-50,page0)

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
    my_canvas.clear()
    x = 0
    y = 0
    for i in range(300):
        smap(7)

def reload(source):
    import supervisor
    supervisor.reload()

gui.button(5, page0.width -40, 50, 40, 0, page0, "pixel", smoop)

bubble = gui.popup(9/11, 9/11)

gui.button(60, page0.width -40, 50, 40, 0, page0, "pop!", bubble.place)
gui.button(115, page0.width -40, 50, 40, 0, page0, "reload!", reload)
#print(page0._contents)