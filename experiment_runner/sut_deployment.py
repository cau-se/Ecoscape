import subprocess

from k8s_client import K8sClient


class SutDeployment:

    def __init__(self, deploy_command, remove_command, remove_phase2_command):
        self.k8s_client = K8sClient()
        self.deploy_command = deploy_command
        self.remove_command = remove_command
        self.remove_phase2_command = remove_phase2_command

    def deploy(self):
        self.k8s_client.apply_directory(self.deploy_command)

    def remove(self):
        subprocess.run(self.remove_command, shell=True)

    def remove_phase2(self):
        subprocess.run(self.remove_phase2_command, shell=True)
