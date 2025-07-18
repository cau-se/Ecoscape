from config.directory_config import ExperimentDirectoryConfig
from k8s_client import K8sClient

class EcoscapeClient:

    def __init__(
        self,
        base_dir,
        directory_config: ExperimentDirectoryConfig
    ):
        self.k8s_client:K8sClient = K8sClient()
        self.base_dir = base_dir
        self.load_dir = directory_config.load_dir
        self.sut_dir = directory_config.sut_dir
        self.infra_dir = directory_config.infra_dir
        self.monitor_dir = directory_config.monitor_dir
        self.chaos_dir = directory_config.chaos_dir

    def apply_load(self):
        self.k8s_client.create_directory(self.base_dir + "/" + self.load_dir)

    def stop_load(self):
        self.k8s_client.delete_directory(self.base_dir + "/" + self.load_dir)

    def apply_sut(self):
        self.k8s_client.create_directory(self.base_dir + "/" + self.sut_dir)

    def delete_sut(self):
        self.k8s_client.delete_directory(self.base_dir + "/" + self.sut_dir)

    def apply_infra(self):
        self.k8s_client.create_directory(self.base_dir + "/" + self.infra_dir)
        self.k8s_client.create_directory(self.base_dir + "/" + self.monitor_dir)
        self.k8s_client.create_directory(self.base_dir + "/" + self.monitor_dir + "/podmonitor")

    def delete_infra(self):
        self.k8s_client.delete_directory(self.base_dir + "/" + self.infra_dir)
        self.k8s_client.delete_directory(self.base_dir + "/" + self.monitor_dir)

    def apply_chaos(self):
        self.k8s_client.create_directory(self.base_dir + "/" + self.chaos_dir)

    def delete_chaos(self):
        self.k8s_client.delete_directory(self.base_dir + "/" + self.chaos_dir)
