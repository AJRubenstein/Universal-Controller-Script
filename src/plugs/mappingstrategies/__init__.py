"""
plugins > mapping strategies

Contains strategies to create event mappings for commonly used things, such
as pedals
"""

__all__ = [
    'IMappingStrategy',
    'PedalStrategy',
    'WheelStrategy',
    'NoteStrategy',
    'DirectionStrategy',
    'SimpleFaders',
]

from .mappingstrategy import IMappingStrategy

from .pedalstrategy import PedalStrategy
from .wheelstrategy import WheelStrategy
from .notestrategy import NoteStrategy
from .directionstrategy import DirectionStrategy
from .simplefaders import SimpleFaders
