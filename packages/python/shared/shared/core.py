"""Domain-neutral data structures shared across services."""

from dataclasses import dataclass


@dataclass(slots=True)
class ServiceInfo:
    """Basic metadata describing a platform service."""

    name: str
    version: str
    description: str = ""
