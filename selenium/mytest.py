from pyvirtualdisplay import Display
print '\nstarting virtual display...'
display = Display(visible=0, size=(1280, 1024))
display.start()

from sst.actions import *

go_to('http://www.ubuntu.com/')
assert_title_contains('Ubuntu homepage')
