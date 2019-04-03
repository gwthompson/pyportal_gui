from tg_gui import gui, system_handler
from tg_gui_extens.artsy import canvas

def scale_position(value,maximum):
    return int(value*20/maximum)

window = system_handler.request_window()
page0 = gui.page()
graph_canvas = canvas(0,0,page0.width,page0.height*0.8,page0)
graph_function = 'x**2'
#wait until canvas is done being made
for x in range(-10,11,1):
    print(eval(graph_function))
    graph_canvas.draw_pixel(scale_position(x,page0.width),scale_position(eval(graph_function),page0.height),gui.red)