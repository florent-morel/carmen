from abc import ABC, abstractmethod
import logging
import time
import csv
import os
from datetime import datetime, timedelta
from backend.src.common.known_exception import KnownException
from backend.src.common.errors import ErrorCode
from backend.src.core.settings import settings
from backend.src.core.yaml_config_loader import DaemonConfig
from backend.src.schemas.virtual_machine import VirtualMachine

logger = logging.getLogger(__name__)


class ComputeWriter(ABC):
    def __init__(self, config: "DaemonConfig", vms: list[VirtualMachine]):
        self.vms: list[VirtualMachine] = vms
        self.date: str = ComputeWriter.get_execution_date()
        self.config: "DaemonConfig" = config
        self.out_file: str = os.path.join(
            str(self.config.upload_path), f"CO2_{self.date}.csv"
        )

    @abstractmethod
    def upload_compute_report(self):
        pass

    @staticmethod
    def get_execution_date():
        execution_date_str = os.getenv("EXECUTION_DATE")
        if not execution_date_str:
            execution_date_str = (datetime.now() - timedelta(days=2)).strftime(
                "%Y-%m-%d"
            )
        try:
            execution_date = datetime.strptime(execution_date_str, "%Y-%m-%d")
        except ValueError as err:
            logger.error(
                "Invalid date format for EXECUTION_DATE: '%s'", execution_date_str
            )
            raise KnownException(
                ErrorCode.VALIDATION_INVALID_DATE_FORMAT,
                details="Failed to parse execution date",
            ) from err
        logger.info(
            "Carbon daemon starting execution for date: %s",
            execution_date.strftime("%Y-%m-%d"),
        )
        return execution_date_str

    def create_compute_CO2_report(
        self,
    ):
        """
        Creates a CSV report containing all resource types.
        Handles VMs, Storage, and future resource categories in one file.
        """
        vms = self.vms or []

        logger.info(
            "Creating CSV report with %d VMs",
            len(vms),
        )
        start = time.time()

        with open(self.out_file, mode="w", newline="", encoding="utf-8") as report:
            writer = csv.writer(report)
            writer.writerows(settings.FINOPS.REPORT_HEADERS)

            vm_carbon = 0
            vm_energy = 0

            # Add VMs
            for vm in vms:
                vm.total_carbon_emitted = (
                    vm.total_carbon_operational + vm.total_carbon_embodied
                )
                vm_carbon += vm.total_carbon_emitted
                vm_energy += vm.total_energy_consumed

                row = [
                    # Common columns
                    self.date,
                    "VM",
                    vm.id,
                    vm.name,
                    vm.region,
                    vm.subscription,
                    vm.total_energy_consumed,
                    vm.total_carbon_operational,
                    vm.total_carbon_embodied,
                    vm.total_carbon_emitted,
                    vm.carbon_intensity,
                    # VM columns
                    vm.vm_size,
                    vm.service,
                    vm.instance,
                    vm.environment,
                    vm.partition,
                    vm.component,
                ]
                writer.writerow(row)
        elapsed_time = time.time() - start
        logging.info("Total carbon emitted: %.2f kg CO2", vm_carbon)
        logging.info("Total energy consumed: %.2f kWh", vm_energy)
        logger.info("CSV report created in %.2f seconds", elapsed_time)
        logger.info(
            "  Resources: %d VMs",
            len(vms),
        )
        logger.info("Report saved to: %s", self.out_file)
