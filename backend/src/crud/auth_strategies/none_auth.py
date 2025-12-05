"""
This module defines a no-authentication strategy for Thanos queries.
"""

from __future__ import annotations

from backend.src.crud.auth_strategies.auth_strategy import AuthStrategy


class NoAuth(AuthStrategy):
    """
    This class implements a no-authentication strategy for Thanos queries.
    It is used when no authentication is required to access the Thanos API.
    """

    def get_headers(self) -> dict[str, str]:
        """
        Returns an empty dictionary as no authentication headers are needed.

        Returns:
            dict: An empty dictionary.
        """
        return {}
