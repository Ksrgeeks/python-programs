import psutil 
for proc in psutil.process_iter():
    try:
        processName = proc.name()
        processId = proc.pid
        print(processName, ' ::: ', processId)
    except(psutil.NoSuchProcess, \
        psutil.AccessDenied, psutil.ZombieProcess):
        pass 