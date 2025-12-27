from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class BugReport:
    """
    Canonical schema for all incoming bug reports.

    Both free-text user reports and structured developer
    reports are normalized into this format.
    """

    content: str
    inferred_severity: Optional[str] = None
    source: str = "unknown"  # user | developer | system
    created_at: datetime = datetime.utcnow()
