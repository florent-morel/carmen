"""
This module defines the IocRegistrationModel class for holding IoC (inversion of control) registration details,
as well as a function for resolving concrete types based on abstract types and IoC keys.
"""

from __future__ import annotations


class IocRegistrationModel:
    """
    IoC Registration Model

    This class represents an IoC registration item, holding details such as IoC key,
    abstract type, and concrete type.
    """

    def __init__(self, ioc_key: str, abstract_type: type, concrete_type: type) -> None:
        """
        Initialize IoC Registration Model

        Args:
            ioc_key (str): The IoC key associated with the registration item.
            abstract_type (type): The abstract type associated with the registration item.
            concrete_type (type): The concrete type associated with the registration item.
        """
        self.ioc_key = ioc_key
        self.abstract_type = abstract_type
        self.concrete_type = concrete_type


def resolve(abstract_type: type, ioc_key: str, duration: int) -> object | None:
    """
    This function resolves the concrete type based on the provided abstract type and IoC key,
    used for carbon computation model selection (IF | CCF).

    Args:
        abstract_type (type): The abstract type to resolve.
        ioc_key (str): The IoC key associated with the concrete type.
        duration (int): Time interval in which power is consumed
    """
    for ioc_registered_item in ioc_registered_models:
        abstract_type_name = ioc_registered_item.abstract_type.__name__

        if (ioc_registered_item.ioc_key == ioc_key) & (
            abstract_type_name == abstract_type.__name__
        ):
            return ioc_registered_item.concrete_type(duration)
    return None


ioc_registered_models: list[IocRegistrationModel] | None = []
