import tempfile
import os
import logging
import sst.actions as ssta
import sst.config

#logging.basicConfig(level=logging.INFO)

def here():
    return os.path.dirname(os.path.abspath(__file__))

def virtual_display_start(size=(1280, 1024)):
    ''' creates a virtual display '''
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=size)
    display.start()
    return display

class Screenshot(object):
    def __init__(self, fileName):
        ''' opens file as saves data in a buffer'''
        self.imageData = open(fileName, 'rb').read()
    def _repr_png_(self):
        return self.imageData
    def __str__(self):
        return 'Size of image %s bytes' % len(self.imageData)

def take_screenshot():
    # need to set config directory
    sst.config.results_directory = here()
    tempFile = tempfile.NamedTemporaryFile(delete=False)
    logging.info('created named file %s' % tempFile.name)
    tempFile.close()
    ssta.take_screenshot(tempFile.name)
    screenshot = Screenshot(tempFile.name)
    os.unlink(tempFile.name)
    if os.path.exists(tempFile.name):
        logging.info('unable to delete temporary file %s' % tempFile.name)
    return screenshot





