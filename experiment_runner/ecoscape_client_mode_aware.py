from time import sleep

from ecoscape_client import EcoscapeClient
from mode.mode import Mode

class EcoscapeClientModeAware():

    def __init__(
        self,
        mode: Mode,
        load_generation_delay: int,
        infra_delay: int,
        ecoscape_client: EcoscapeClient
    ):
        self.mode = mode
        self.ecoscape_client = ecoscape_client
        self.load_generation_delay = load_generation_delay
        self.infra_delay = infra_delay

    def deploy_sut(self):
        if self.mode.is_deploy_system():
            self.ecoscape_client.apply_sut()

    def remove_sut(self):
        if self.mode.is_deploy_system():
            print("Deleting SUT")
            self.ecoscape_client.delete_sut()

    def start_load(self):
        if self.mode.is_start_load():
            print("start load")
            self.ecoscape_client.apply_load()

    def stop_load(self):
        if self.mode.is_start_load():
            print("Stopping load")
            self.ecoscape_client.stop_load()

    def apply_infrastructure_constraints(self):
        if self.mode.is_apply_infrastructure_constraints():
            self._sleep_with_message(self.infra_delay, "apply infrastructure constraints")
            self.ecoscape_client.apply_infra()

    def delete_infrastructure_constraints(self):
        if self.mode.is_apply_infrastructure_constraints():
            print("Deleting infrastructure constraints")
            self.ecoscape_client.delete_infra()

    def apply_chaos(self):
        if self.mode.is_apply_chaos():
            print("Applying Chaos")
            self.ecoscape_client.apply_chaos()

    def delete_chaos(self):
        if self.mode.is_apply_chaos():
            print("Deleting Chaos")
            self.ecoscape_client.delete_chaos()

    def _sleep_with_message(self, sleep_duration, message):
        print(f"Wait {sleep_duration}s to {message}")
        sleep(sleep_duration)