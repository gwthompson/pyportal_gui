from tg_gui import gui, system_handler
window = system_handler.request_window()
page0 = gui.page()
widget0 = gui.rect(page0.width//2-5,page0.height//2-5,page0.width+10,30,0,page0,gui.color(0,255,0))
widget1 = gui.text(page0.width//2,page0.height//2,page0.width,20,page0,'Testing Testing 125',size = 1,color = gui.color(255,255,0))