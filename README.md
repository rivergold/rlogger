# rlogger

A convenient encapsulation of Python logging

## Install

```shell
pip install rlogger
```

## Use

```python
from rlogger import RLogger
# Set log file path
RLogger.init('file.log', enable_screen=True, log_level='INFO', max_bytes=1e8, backup_count=1)
RLogger.log('your message', RLogger.INFO)
RLogger.log('your message', RLogger.DEBUG)
RLogger.log('your message', RLogger.WARNING)
RLogger.log('your message', RLogger.ERROR)
# Close log when you not need
RLogger.close()
RLogger.log('your message', RLogger.ERROR) # Will not print
```
