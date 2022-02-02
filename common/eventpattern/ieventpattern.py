"""
common > eventpattern

Contains code for pattern matching with MIDI events, including EventPattern,
a standard way to match events, and IEventPattern, from which custom pattern
matchers can be derived.

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]
"""

# from __future__ import annotations

from typing import TYPE_CHECKING
from abc import abstractmethod

if TYPE_CHECKING:
    from .. import eventData

class IEventPattern:
    """
    Abstract definition for an EventPattern, used to match MIDI events with
    ControlSurfaces.

    This class can be extended if a developer wishes to create their own event
    pattern for a case where the standard EventPattern class doesn't suffice.
    """
    
    @abstractmethod
    def matchEvent(self, event: 'eventData') -> bool:
        """
        Return whether the given event matches the pattern

        This is an abstract method which should be implemented by child classes.

        ### Args:
        * `event` (`eventData`): Event to match against

        ### Returns:
        * `bool`: whether the event matches
        """
        raise NotImplementedError("This method should be implemented by "
                                  "child classes")