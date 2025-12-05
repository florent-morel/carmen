"""
This module defines the Metadata model which is used to handle parameters-metadata for IF models.
"""

from dataclasses import dataclass


@dataclass
class Metadata:
    """
    Metadata class to define parameters-metadata for IF models.
    """

    aggregation_parameter: str
    unit: str
    description: str
    aggregation_method_time: str
    aggregation_method_component: str
