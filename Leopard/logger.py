from time import strftime, gmtime # time library for files
import global_vars

#### Appends an event to the log.txt
# @param event = The event to be added to the log.txt
def log_event(event):
    #open log file for appending
    log_txt = open(global_vars.log_txt,"a+")
    msg = strftime("%a %b %d %I:%M:%S %p",gmtime())
    log_txt.write(msg + " >>> " + event)
    log_txt.close()
# end def log_event
