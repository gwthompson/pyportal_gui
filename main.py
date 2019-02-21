from tg_gui import gui, system, system_handler
from tg_modules.tg_rgb import rgb, ili9341
from tg_modules.make_ios import dio
import time, random, gc, supervisor, busio, board, digitalio, pulseio, adafruit_touchscreen
gc.enable()

from displayio import release_displays
release_displays()

#setup disp
disp = ili9341.ILI9341(busio.SPI(board.SCK, board.MOSI, board.MISO), dio(board.TFT_DC, 0), dio(board.TFT_CS, 0), dio(board.TFT_RESET, 0))
backlight = pulseio.PWMOut(board.TFT_BACKLIGHT)
backlight.duty_cycle = 2**16 -1

#touchscreen setup
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(320, 240))

##gui setup:
gui.round_rect = disp.round_rect
gui.place_text = disp.text

gui.good_text_size = 2
gui.good_gap_size  = 5
gui.good_widget_size  = 60
gui.aprox_char_size = (6,8)

gui.color = rgb.colorili
gui.color_max = 255

#give suystem needed parameters
def query_commmands():
    return input('cmd:').split()

system.x = 0
system.y = 0
system.width = disp.width
system.height = disp.height

system.enable_touch_navigation_bar = False
system.enable_system_status_bar = True

#system.standard_path = 'programs'

system.debug = False
system.debug_level = 1000

#system.home_program = 'programs.Therm_Cam'

system.init()
system.cycle()

was_touched = False
while True:
    #touch sterf
    try:
        point = ts.touch_point[0:2]
        system_handler.push_event('ptr.go.'+str(),'ptr.d')
        was_touched = True
    except:
        if was_touched:
            system_handler.push_event('ptr.prs')
            was_touched = False
        else:
            system_handler.push_event('ptr.u')


    #if connected over serial
    '''if supervisor.runtime.serial_connected:
        system.repl_query()
    else:
        system_handler.push_event('mv')'''

    if '!break' in system_handler._event_que:
        break

    #the system.cycle runs a cycle then returns any errors and outputs
    ret = system.cycle()
    if len(ret):
        print(ret)
    gc.collect()

print('done')