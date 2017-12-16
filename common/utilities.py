import os
import sys

# List module info
class LM:

    def __init__(self):
        self.cwd = os.getcwd()
        self.modules = sys.modules.keys()

    def __repr__(self):
        return '<Repr for Debug: \n' \
               + 'cwd:{}\n'.format(self.cwd) \
               + 'modules:{!r}'.format(self.modules)


class CD:
    def __init__(self, new_path):
        self._new_path = os.path.expanduser(new_path)

    def __enter__(self):
        self._cur_path = os.getcwd()
        os.chdir(self._new_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self._cur_path)
