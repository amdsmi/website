import threading
import config as cfg

from server import Server

_TIMEOUT = 1 / 1000


class Service:
    def __init__(self):
        self._is_running = False
        self._main_thread = None

    @property
    def is_running(self):
        if self._is_running:
            return True

        if self._main_thread is not None and self._main_thread.is_alive():
            return True

        return False

    def run(self):
        if self._is_running:
            raise Exception('The object already is running.')

        if self._main_thread is not None and self._main_thread.is_alive():
            raise Exception('The previous running has not finished.')

        self._main_thread = threading.Thread(target=self._main, args=(), daemon=True)

        self._main_thread.start()

    def cancel(self):
        if self._is_running:
            self._is_running = False

    def join(self):
        if self._main_thread is not None and self._main_thread.is_alive():
            self._main_thread.join()

    def stop(self):
        self.cancel()
        self.join()

    def _main(self):
        try:
            self._is_running = True

            server = Server(name=__name__)
            server.run()

        finally:
            self._is_running = False
