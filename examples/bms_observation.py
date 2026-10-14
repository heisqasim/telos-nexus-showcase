"""Pure data model for safe read-only BMS observation.

Illustrates separation of transport freshness and equipment truth.
No network code, controllers, overrides, or commands.
"""
from dataclasses import dataclass
from enum import Enum


class LinkState(str, Enum):
    DEMO = "DEMO"
    ONLINE = "ONLINE"
    STALE = "STALE"
    OFFLINE = "OFFLINE"
    NO_LINK = "NO_LINK"


@dataclass(frozen=True)
class PointSample:
    observed_at: float
    running: bool | None
    fault_active: bool | None


@dataclass(frozen=True)
class EquipmentObservation:
    source: str
    link: LinkState
    running: bool | None
    alarm_active: bool | None
    alarm_is_current: bool


def observe_equipment(
    *,
    now: float,
    live_requested: bool,
    transport_connected: bool,
    sample: PointSample | None,
    stale_after: float = 60,
    offline_after: float = 300,
) -> EquipmentObservation:
    """Present only supported plant facts. Prior alarms remain flagged stale."""
    if not (0 < stale_after < offline_after):
        raise ValueError("invalid freshness thresholds")

    if not live_requested:
        return EquipmentObservation(
            source="DEMO", link=LinkState.DEMO,
            running=None, alarm_active=None, alarm_is_current=False
        )

    if not transport_connected:
        return EquipmentObservation(
            source="LIVE", link=LinkState.NO_LINK,
            running=None,
            alarm_active=sample.fault_active if sample else None,
            alarm_is_current=False,
        )

    if sample is None:
        return EquipmentObservation(
            source="LIVE", link=LinkState.OFFLINE,
            running=None, alarm_active=None, alarm_is_current=False
        )

    age = now - sample.observed_at
    if age < 0:
        raise ValueError("sample timestamp is in the future")

    if age >= offline_after:
        link = LinkState.OFFLINE
    elif age >= stale_after:
        link = LinkState.STALE
    else:
        link = LinkState.ONLINE

    current = link == LinkState.ONLINE
    return EquipmentObservation(
        source="LIVE", link=link,
        running=sample.running if current else None,
        alarm_active=sample.fault_active,
        alarm_is_current=current,
    )
