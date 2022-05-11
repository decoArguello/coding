import win32api
import win32gui
from  WindowMgr import WindowMgr

close = False

class Punto:
  def __init__(self, posX, posY, color):
    self.posX = posX
    self.posY = posY
    self.color = color
  def __str__(self):
    return "x: "+str(self.posX)+" y: "+  str(self.posY) + " color: "+str(self.color) 

def IntToRGBTuple(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return (red, green, blue)

def window_enumeration_handler(hwnd, top_windows):
  #"""Add window title and ID to array."""
  top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def lindo():
  w = WindowMgr()
  w.find_window_wildcard("Lindo")
  w.set_foreground()

def capture_click():
  lindo()
  clicked = False
  state_left = win32api.GetKeyState(0x01)
  while not clicked:
    a = win32api.GetKeyState(0x01)
    if a != state_left:
      state_left = a
      print(a)
      if a >= 0:
        x,y = win32api.GetCursorPos()
        color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x , y)
        c = IntToRGBTuple(color)
        p = Punto(x,y,c)
        print(p)
        clicked = True 
  print("captured click")

def winEnumHandler( hwnd, ctx ):
  if win32gui.IsWindowVisible( hwnd ):
    ctx.append((hwnd,win32gui.GetWindowText( hwnd )))

while not close:
  print('1. Capture Click')
  print('2. Lindo to front')
  print('3. Close')
  opcion = str(input())
  if opcion == '3':
    close = True
  elif opcion == '1':
    capture_click()
  elif opcion == '2':
    top_windows = []
    win32gui.EnumWindows( winEnumHandler, top_windows )
    for window in top_windows:
      if 'lindo' in window[1].lower(): 
        win32gui.ShowWindow(window[0], 9)
  else:
    print("invalid option")

print("Exiting")