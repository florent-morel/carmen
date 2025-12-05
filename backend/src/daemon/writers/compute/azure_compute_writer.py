"""
Azure writer strategy for uploading compute reports to Azure Blob Storage.
"""

import logging

from azure.identity import ClientSecretCredential

from backend.src.core.yaml_config_loader import DaemonConfig
from backend.src.daemon.writers.compute.compute_writer import ComputeWriter
from backend.src.schemas.virtual_machine import VirtualMachine
from backend.src.utils.azure_utils import (
    initialize_azure_client,
    upload_blob_to_container,
)

logger = logging.getLogger(__name__)


class AzureComputeWriter(ComputeWriter):
    """
    Azure Blob Storage writer for uploading compute CO2 reports.

    This class handles uploading generated compute reports to Azure Blob Storage
    using the configured storage account and container.
    """

    def __init__(self, vms: list[VirtualMachine], config: DaemonConfig) -> None:
        """
        Initialize the Azure compute writer.

        Args:
            vms: List of virtual machines to generate report for
            config: Daemon configuration containing Azure settings

        Raises:
            ValueError: If required Azure configuration is missing
        """
        super().__init__(config, vms)
        self.config: DaemonConfig = config

        self.storage_account_url: str = str(
            self.config.source.azure.storage_account_url
        )
        self.container_name_upload: str = str(
            self.config.upload.azure.container_name_upload
        )

        self.blob_name: str = str(self.config.upload.azure.blob_name)

        self.credential: ClientSecretCredential = initialize_azure_client(config)

        logger.debug(
            "azure compute writer initialized with container %s",
            self.container_name_upload,
        )

    def upload_compute_report(self) -> None:
        """
        Create and upload the compute CO2 report to Azure Blob Storage.
        """
        logger.info("creating compute co2 report for upload")
        self.create_compute_CO2_report()
        self.upload_file_to_datalake()
        logger.info("compute co2 report created successfully")

    def upload_file_to_datalake(self) -> None:
        """
        Upload a file to the Azure Blob Storage datalake.

        Raises:
            KnownException: If upload fails for any reason
        """
        logger.info("uploading file to datalake blob_name %s", self.blob_name)

        try:
            upload_blob_to_container(
                storage_account_url=self.storage_account_url,
                credential=self.credential,
                container_name=self.container_name_upload,
                file_path=self.out_file,
                blob_name=self.blob_name,
            )
            logger.info("file upload completed successfully for %s", self.blob_name)

        except Exception as e:
            logger.error("failed to upload file %s %s", self.blob_name, str(e))
            raise
