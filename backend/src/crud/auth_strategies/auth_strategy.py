"""
This module defines the base class for authentication strategies.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class AuthStrategy(ABC):
    """
    Abstract base class for authentication strategies.
    """

    @abstractmethod
    def get_headers(self) -> dict[str, str]:
        """
        Get the headers for the request, including any necessary authentication tokens.
        """
