"""
This module defines the Azure Active Directory authentication strategy.
"""

from __future__ import annotations

from msal import ConfidentialClientApplication

from backend.src.core.yaml_config_loader import ApiConfig
from backend.src.crud.auth_strategies.auth_strategy import AuthStrategy


class AAD(AuthStrategy):
    """
    AAD Authentication Strategy for Thanos queries.
    """

    def __init__(self, config: ApiConfig) -> None:
        """
        Initialize the AAD auth_strategies strategy.
        """
        assert config.credentials is not None
        self.app: ConfidentialClientApplication = ConfidentialClientApplication(
            client_id=str(config.credentials.client_id),
            client_credential=str(config.credentials.client_secret),
            authority=f"https://login.microsoftonline.com/{str(config.credentials.tenant_id)}",
        )
        self.scope: str = str(config.scope)

    def get_headers(self) -> dict[str, str]:
        """
        Get the headers for the request, including the AAD token.

        Returns:
            dict: The headers for the request.
        """
        result = self.app.acquire_token_for_client([self.scope])
        if result and "access_token" in result:
            token: str = str(result["access_token"])
            return {"Authorization": f"Bearer {token}"}
        raise ValueError(result)
