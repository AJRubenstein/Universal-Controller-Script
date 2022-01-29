"""
plugins > mappingstrategies > mappingstrategy

Definition for a mapping strategy, which can be used to map a controls
with little effort on the part of the plugin developer
"""

from devices import DeviceShadow


class IMappingStrategy:
    """
    Creates a quick and simple way to map controls to plugin parameters used by
    many plugins, for example pedal events
    """
    def __init__(self) -> None:
        pass
    
    def apply(self, shadow: DeviceShadow) -> None:
        raise NotImplementedError("This function should be implemented by child"
                                  " classes")