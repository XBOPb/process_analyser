import wmi

notify_filter = 'creation'
process_watcher = wmi.WMI().Win32_Process.watch_for(notify_filter)
while True:
    new_process = process_watcher()
    print(new_process.Caption)
    print(new_process.CreationDate)