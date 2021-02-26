import logging
import sys
import threading
import config


class KeyMonitor(threading.Thread):

    def __init__(self, args=(), kwargs=None):
        super().__init__()
        self.q = args
        self.args = args
        logging.debug('Ready for keyboard input:')

    def run(self):
        while True:
            if not config.run:
                self.stop()
            input_str = input()
            self.q.put(input_str)

    def stop(self):
        logging.debug("Closing keyboard thread...")
        sys.exit(1)
