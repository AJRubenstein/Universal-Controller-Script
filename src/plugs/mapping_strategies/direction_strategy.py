"""
plugs > mapping_strategies > direction_strategy

Mapping strategy to handle direction buttons

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
import ui
from . import IMappingStrategy
from devices import DeviceShadow
from plugs.event_filters import filterButtonLift
from common.types import Color

from control_surfaces import (
    IControlShadow,
    DirectionNext,
    DirectionPrevious,
    DirectionLeft,
    DirectionRight,
    DirectionUp,
    DirectionDown,
    DirectionSelect,
)

BOUND_COLOR = Color.fromInteger(0x888888)


class DirectionStrategy(IMappingStrategy):
    """
    Mapping strategy to handle direction buttons.

    This maps controls to next or previous commands.
    """
    def __init__(self) -> None:
        self._controls: list[IControlShadow] = []

    def apply(self, shadow: DeviceShadow):
        # TODO: Find nicer way to bind colors like this
        shadow.bindMatch(
            DirectionNext,
            self.next,
        ).colorize(BOUND_COLOR)

        shadow.bindMatch(
            DirectionPrevious,
            self.previous,
        ).colorize(BOUND_COLOR)

        shadow.bindMatch(
            DirectionRight,
            self.next,
        ).colorize(BOUND_COLOR)

        shadow.bindMatch(
            DirectionLeft,
            self.previous,
        ).colorize(BOUND_COLOR)

        shadow.bindMatch(
            DirectionDown,
            self.next,
        ).colorize(BOUND_COLOR)

        shadow.bindMatch(
            DirectionUp,
            self.previous,
        ).colorize(BOUND_COLOR)

        shadow.bindMatch(
            DirectionSelect,
            self.select,
        ).colorize(BOUND_COLOR)

    @filterButtonLift()
    def next(self, control, index, *args, **kwargs):
        ui.next()
        return True

    @filterButtonLift()
    def previous(self, control, index, *args, **kwargs):
        ui.previous()
        return True

    @filterButtonLift()
    def select(self, control, index, *args, **kwargs):
        # BUG: Will just echo enter - improve this
        ui.enter()
        return True
