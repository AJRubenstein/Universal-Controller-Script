"""
plugs > tick_filters > index

Contains filters for filtering by plugin and window indexes

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
from common.plug_indexes import UnsafeIndex
from .decorator import do_filter


@do_filter
def toPluginIndex(index: UnsafeIndex):
    """
    Filter out events when the index is not a plugin
    """
    return isinstance(index, tuple)


@do_filter
def toGeneratorIndex(index: UnsafeIndex):
    """
    Filter out events when the index is not a generator plugin
    """
    return isinstance(index, tuple) and len(index) == 1


@do_filter
def toEffectIndex(index: UnsafeIndex):
    """
    Filter out events when the index is not an effect plugin
    """
    return isinstance(index, tuple) and len(index) == 2


@do_filter
def toWindowIndex(index: UnsafeIndex):
    """
    Filter out events when the index is not a window
    """
    return isinstance(index, int)


@do_filter
def toSafeIndex(index: UnsafeIndex):
    """
    Filter out events when the index is None
    """
    return index is not None