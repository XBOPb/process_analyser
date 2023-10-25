import wmi

class ProcessMonitor():
    
    def __init__(self):
        self.process_property = {
            'Caption': None,
            'CreationDate': None,
            'ProcessID': None
        }
        self.filter = 'creation'
        self.process_watcher = wmi.WMI().Win32_Process.watch_for(self.filter)

    def update(self):
        process = self.process_watcher()
        self.process_property['EventType'] = process.event_type
        self.process_property['Caption'] = process.Caption
        self.process_property['CreationDate'] = process.CreationDate
        self.process_property['ProcessID'] = process.ProcessID

    def convert_datetime(self, datetime):
        year = datetime[:4]
        month = datetime[4:6]
        day = datetime[6:8]
        hour = datetime[8:10]
        minutes = datetime[10:12]
        seconds = datetime[12:14]
        return f'{day}/{month}/{year} {hour}:{minutes}:{seconds}'
    
    @property
    def event_type(self):
        return self.process_property['EventType']
    
    @property
    def caption(self):
        return self.process_property['Caption']
    
    @property
    def creation_date(self):
        date = self.process_property['CreationDate']
        return self.convert_datetime(date)
    
    @property
    def process_id(self):
        return self.process_property['ProcessID']