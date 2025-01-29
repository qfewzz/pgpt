"""private-gpt."""

import logging
import os

# Set to 'DEBUG' to have extensive logging turned on, even for libraries
ROOT_LOG_LEVEL = "INFO"

PRETTY_LOG_FORMAT = (
    "%(asctime)s.%(msecs)03d [%(levelname)-8s] %(name)+25s - %(message)s"
)
logging.basicConfig(level=ROOT_LOG_LEVEL, format=PRETTY_LOG_FORMAT, datefmt="%H:%M:%S")
logging.captureWarnings(True)

# Disable gradio analytics
# This is done this way because gradio does not solely rely on what values are
# passed to gr.Blocks(enable_analytics=...) but also on the environment
# variable GRADIO_ANALYTICS_ENABLED. `gradio.strings` actually reads this env
# directly, so to fully disable gradio analytics we need to set this env var.
os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"

# Disable chromaDB telemetry
# It is already disabled, see PR#1144
# os.environ["ANONYMIZED_TELEMETRY"] = "False"

# adding tiktoken cache path within repo to be able to run in offline environment.
os.environ["TIKTOKEN_CACHE_DIR"] = "tiktoken_cache"


import time
import threading
import importlib
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import live_config
class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == os.path.abspath("path/to/your/file.py"):
            print(f'{event.src_path} has been modified!')
            importlib.reload(live_config)

def start_observer():
    path = "path/to/your/"
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    observer_thread = threading.Thread(target=start_observer)
    observer_thread.daemon = True
    observer_thread.start()

    # Main thread can perform other tasks
    while True:
        print("Background thread is running...")
        time.sleep(5)
        # You can access the global variables from your_module here
        # e.g. print(your_module.global_variable)
