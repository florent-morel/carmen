from backend.src.core.yaml_config_loader import DaemonConfig
from backend.src.daemon.writers.compute.compute_writer import ComputeWriter
from backend.src.schemas.virtual_machine import VirtualMachine


class LocalComputeWriter(ComputeWriter):
    def __init__(self, vms: list[VirtualMachine], config: "DaemonConfig"):
        super().__init__(config, vms)
        self.config: "DaemonConfig" = config

    def upload_compute_report(self):
        self.create_compute_CO2_report()
