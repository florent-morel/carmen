"""
Utility functions for Azure operations including authentication and blob storage.
"""

import logging
import os
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
from azure.identity._credentials.client_secret import ClientSecretCredential
from azure.storage.blob import BlobServiceClient, ContainerClient
from backend.src.core.yaml_config_loader import DaemonConfig
from backend.src.common.known_exception import KnownException

logger = logging.getLogger(__name__)


def initialize_azure_client(config: "DaemonConfig") -> ClientSecretCredential:
    """
    Initialize Azure credentials.

    Raises:
        ClientAuthenticationError: If Azure authentication fails.
    """
    try:
        # Config validation ensures these are not None, so we can safely access them
        credential: ClientSecretCredential = ClientSecretCredential(
            tenant_id=str(config.credentials.tenant_id),
            client_id=str(config.credentials.client_id),
            client_secret=str(config.credentials.client_secret),
        )
        logger.debug("azure credentials initialized successfully")
        return credential
    except Exception as e:
        logger.error("failed to initialize azure credentials %s", str(e))
        raise ClientAuthenticationError("azure authentication failed") from e


def create_blob_service_client(
    storage_account_url: str, credential: ClientSecretCredential
) -> BlobServiceClient:
    """
    Create and return a blob service client.

    Returns:
        Configured BlobServiceClient instance.
    """
    return BlobServiceClient(
        account_url=storage_account_url,
        credential=credential,
    )


def upload_blob_to_container(
    storage_account_url: str,
    credential: ClientSecretCredential,
    container_name: str,
    file_path: str,
    blob_name: str,
) -> None:
    """
    Upload a file to Azure Blob Storage container.

    Args:
        storage_account_url: Azure storage account URL
        credential: Azure client secret credential
        container_name: Name of the container to upload to
        file_path: Local path to the file to upload
        blob_name: Name/path for the blob in storage

    Raises:
        FileNotFoundError: If the local file doesn't exist
        Exception: If upload fails
    """
    try:
        container_client = ContainerClient(
            account_url=storage_account_url,
            container_name=container_name,
            credential=credential,
        )

        with open(file_path, "rb") as data:
            _ = container_client.upload_blob(name=blob_name, data=data, overwrite=True)
            logger.info(
                "file %s successfully uploaded to datalake container %s",
                blob_name,
                container_name,
            )

    except FileNotFoundError as ex:
        logger.error(
            "file %s not found at path %s",
            os.path.basename(file_path),
            os.path.dirname(file_path),
        )
        raise KnownException(f"file not found {file_path}") from ex
    except ValueError as ex:
        logger.error(
            "invalid parameter for upload file_path %s blob_name %s",
            file_path,
            blob_name,
        )
        raise KnownException(f"invalid parameter for upload {str(ex)}") from ex
    except HttpResponseError as ex:
        status_code = getattr(ex, "status_code", "unknown")
        logger.error(
            "azure http error status %s while uploading file %s",
            status_code,
            blob_name,
        )
        raise KnownException(
            f"azure service error {status_code} while uploading {blob_name}"
        ) from ex
    except Exception as ex:
        logger.error("unexpected error while uploading file %s %s", blob_name, str(ex))
        raise KnownException(f"upload failed for {blob_name} {str(ex)}") from ex
