import time
import os
import traceback
from pathlib import Path


class TreeWatcher:
    def __init__(self, callback, interval=1):
        self.callback = callback
        self.i = interval
        #
        self.file_modified_times = {}
        self.script_location = Path(__file__).absolute().parent
        self.initialize_file_times()

    def initialize_file_times(self):

        for root, _, files in os.walk(self.script_location):
            for filename in files:
                filepath = Path(root) / filename
                if filepath.is_file():
                    self.file_modified_times[str(
                        filepath)] = os.path.getmtime(filepath)

    def start(self):
        try:
            while True:
                time.sleep(self.i)
                for root, _, files in os.walk(self.script_location):
                    for filename in files:
                        filepath = Path(root) / filename
                        filepath_str = str(filepath)
                        if filepath.is_file():
                            modified = os.path.getmtime(filepath)
                            if filepath_str not in self.file_modified_times:

                                self.file_modified_times[filepath_str] = modified
                                if self.callback(filename, 'created'):
                                    return

                            elif modified != self.file_modified_times[filepath_str]:
                                self.file_modified_times[filepath_str] = modified
                                if self.callback(filename, 'modified'):
                                    return

        except Exception as e:
            print(traceback.format_exc())