"""
This module defines custom Enum classes.
"""

from __future__ import annotations

from enum import Enum


class LogLevel(Enum):
    """
    Enum for defining logging levels.

    Attributes:
        DEBUG (str): Debug logging level.
        INFO (str): Informational logging level.
        WARNING (str): Warning logging level.
        ERROR (str): Error logging level.
        CRITICAL (str): Critical logging level.
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Label(Enum):
    """
    Enum for defining various thanos labels.

    Attributes:
        SERVICE (str): Label for service.
        PAAS (str): Label for cluster.
        NAMESPACE (str): Label for namespace.
        POD (str): Label for pod.
        UID (str): The unique identifier label for pod.
    """

    SERVICE = "label_app_kubernetes_io_part_of"
    PAAS = "stack"
    NAMESPACE = "namespace"
    POD = "pod"
    UID = "uid"


class HardwareConsumptionType(Enum):
    """
    Enum for defining hardware consumption types.

    Attributes:
        REQUESTED_CORES (str): Label for cpu requested cores.
        CPU_UTIL (str): Label for cpu utilization: used cores / requested cores.
        REQUESTED_BYTES (str): Label for memory requested bytes.
        STORAGE_CAPACITY_BYTES (str): Label for storage capacity bytes.
    """

    REQUESTED_CORES = "cpu requested"
    CPU_UTIL = "cpu utilization"
    REQUESTED_BYTES = "memory requested"
    STORAGE_CAPACITY_BYTES = "storage capacity"


class SamplingRate(str, Enum):
    """
    Enumeration representing different sampling rates.

    Each sampling rate is defined as a string representing a duration.
    """

    FIFTEEN_SECONDS = "15s"
    THIRTY_SECONDS = "30s"
    ONE_MINUTE = "1m"
    FIVE_MINUTES = "5m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    SIX_HOURS = "6h"
    ONE_DAY = "1d"
