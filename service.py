from time import sleep

from jnius import autoclass

PythonService = autoclass('org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)


while True:
    print("service running.....")
    sleep(5)
