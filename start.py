from threading import Thread
from tracker import ProcessMonitor
import wmi
import pythoncom

class Monitor(Thread):
    
    def __init__(self, action):
        self.action = action
        Thread.__init__(self)
    
    def run(self):
        pythoncom.CoInitialize()
        proc_mon = ProcessMonitor(self.action)
        while True:
            proc_mon.update()
            print(
                proc_mon.creation_date,
                proc_mon.event_type,
                proc_mon.caption,
                proc_mon.process_id
            )
        pythoncom.CoUninitialize()

if __name__ == '__main__':
    mon_creation = Monitor('creation')
    mon_creation.start()
    mon_deletion = Monitor('deletion')
    mon_deletion.start()