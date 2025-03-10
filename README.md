# TreeWatcher
This script provides hot reload functionality by monitoring a directory for file changes and automatically executing a specified command upon detection. 

Ideal for development environments, it streamlines workflows by automatically refreshing or rebuilding applications whenever code is updated, enabling a more responsive and iterative development process. This approach eliminates the need for manual restarts, saving time and improving productivity.

Usage Example:
```python
from TreeWatcher import *

def file_changed(filename, change_type):
    print(f"File {filename} {change_type}!")
    return False


handler = TreeWatcher(file_changed)
handler.start()
```

To set the interval after each check (1 second by default), just initialize the Watcher with a different interval (in seconds):
```python
handler = TreeWatcher(file_changed, interval=0.5)
```
