# imports to turn the screen on
from tg_modules.tg_rgb import rgb, ili9341
from tg_modules.make_ios import dio
import busio, board, pulseio, time

from displayio import release_displays
release_displays()

#setup disp
disp = ili9341.ILI9341(busio.SPI(board.SCK, board.MOSI, board.MISO), dio(board.TFT_WR, 0), dio(board.TFT_CS, 0), dio(board.TFT_RESET, 0))
time.sleep(.01)
backlight = pulseio.PWMOut(board.TFT_BACKLIGHT)
backlight.duty_cycle = 2**16 -1

del release_displays

# rest of imports
from tg_gui import gui, system, system_handler, _resources
import random, gc, supervisor, digitalio, adafruit_touchscreen
gc.enable()

#touchscreen setup
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(320, 240))

##gui setup:
gui.round_rect = disp.round_rect
gui.place_text = disp.text

gui.good_text_size = 1
gui.good_gap_size  = 5
gui.good_widget_size  = 50
gui.aprox_char_size = (6,8)
gui.good_radius_size = 0

gui.color = rgb.colorili
gui.color_max = 255

#give suystem needed parameters
def query_commmands():
    return input('cmd:').split()

system.x = 0
system.y = 0
system.width = disp.width
system.height = disp.height

system.enable_touch_navigation_bar = True
system.enable_system_status_bar = True

system.program_paths.append("programs")
system.program_paths.append("lib.tg_gui.programs.examples")
#system.home_program = 'lib.tg_gui.programs.examples.EXP_1'


system.debug = False
system.debug_level = 3

#system.home_program = 'programs.Therm_Cam'

system.init()
system.cycle()

#system.gui._touch.add(system.gui.pointable_widget(0,0,240,320, system.gui._working_window.current, system.gui._do_nothing))
#print(system.gui._working_window.current.width, system.gui._working_window.current.height)
#system.gui._working_window.current.place(10,0,50,300)

#system_handler.push_event('mv','mv.prs','chgpg.go.1','mv.n','mv.prs','mv')# 'mv.prs')
#system_handler.push_event('mv', 'mv.n','mv.prs')

gc.collect()

was_touched = False
enable_serial = False
enable_touch = True
while True:
    #touch sterf
    if enable_touch:
        try:
            point = ts.touch_point[0:2]
            print(point)
            system_handler.push_event('ptr.go.'+str(point[1])+','+str(320-point[0]),'ptr.d')
            was_touched = True
        except:
            if was_touched:
                system_handler.push_event('ptr.prs')
                was_touched = False
            else:
                system_handler.push_event('ptr.u')


    #if connected over serial
    if supervisor.runtime.serial_connected and enable_serial:
        system.repl_query()
        system_handler.push_event('mv')


    if '!break' in system_handler._event_que:
        break
    if '!kbrd_off' in system_handler._event_que:
        enable_serial = False

    #the system.cycle runs a cycle then returns any errors and outputs
    ret = system.cycle()
    if len(ret):
        print(ret)
    gc.collect()
    #print(system._touch._obj_list)
    #time.sleep(.5)

print('done')