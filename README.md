This is a wrapper for the papertrail logging system.
This package do not adds functions to logging package or standard python language,
it simply provides basic methods to send logs to the papertrail system.

Logs have the same log level as logging logs.
Some infos are automatically added to message: 
date and time, Computer name and process that generated the log.

Actually this package has been tested only on Windows 10, in the future I'll test on other OSes