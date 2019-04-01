from tg_gui import gui, system_handler
from tg_gui_extens.artsy import canvas

window = system_handler.request_window()
#print('fartsy window', window)

page0 = gui.page()
page1 = gui.page()


###----page0----
#print(page0.width-10)
my_canvas = canvas(5,5,page0.width-10,page0.width-50,page0)

x = 0
y = 0
color = gui.red
def smoop(source):
    global x,y, color
    my_canvas.clear()
    x = 0
    y = 0
    for i in range(300):
        my_canvas.draw_pixel(x,y,color)
        my_canvas.draw_pixel(x,y+1,color)
        x+=1
        y+=2
    if color == gui.red:
        color = gui.blue
    else:
        color = gui.red

def reload(source):
    import supervisor
    supervisor.reload()

gui.button(5, page0.width -40, 50, 40, 0, page0, "pixel", smoop)

bubble = gui.popup(9/11, 9/11, enable_shoo_zone = True)
#print('fartsy bubble',bubble)
#gui.button(5, 5, 50, 50, 3, bubble, "shoo away", bubble.shoo)
gui.button(5, 5, 50, 50, 3, bubble, "shoo away", bubble.shoo)

#print('fartsy page0', page0)
#print('fartsy window_contents', window._contents)
#print('fartsy page0 id',id(page0))

def summon_pop(*args):
    #global page0
    #page0.place()
    #print('skap page0', page0)
    #print('skap index 0', window.current)
    #print('skap bubble',bubble)
    #print('skap window', window)
    #bubble.intrude(window.current)
    bubble.intrude(page0)
    #bubble.place()


#skap()

gui.button(60, page0.width -40, 50, 40, 0, page0, "pop!", summon_pop)
#print('page0 post button makey', page0)
gui.button(115, page0.width -40, 50, 40, 0, page0, "reload!", reload)
#print('page0 post button makey2', page0)

###----page1----

plate = gui.sized_popup(50,50,115,50)


def summon_plate(*args):
    plate.intrude(page1)

def summon_kbrd(source):
    system_handler.prompt_keyboard(source.stored_data)

gui.button(50, 50, 50, 50, 5, page1, 'ooh?', summon_plate)
kbrd_but = gui.button(105, 105, 50, 50, 5, page1, 'kbrd?', summon_kbrd)
gui.rect(18,18,124,24,0,page1,gui.white)
text_box = gui.text(20,20,120,20, page1, '')
kbrd_but.stored_data = text_box


