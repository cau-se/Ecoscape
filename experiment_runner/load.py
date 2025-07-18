import subprocess
from time import sleep

from k8s_client import K8sClient


class Load:
    def __init__(self, start_command, stop_command, load_generator_delay):
        self.k8s_client = K8sClient()
        self.start_command = start_command
        self.stop_command = stop_command,
        self.load_generator_delay = load_generator_delay

    def start(self):
        print(f"Wait {self.load_generator_delay} seconds until load starts")
        sleep(self.load_generator_delay)
        self.k8s_client.apply_directory(self.start_command)

    def stop(self):
        self.k8s_client.apply_directory(self.stop_command)
