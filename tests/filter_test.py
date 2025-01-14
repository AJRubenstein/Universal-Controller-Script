"""
tests > filter_test

Tests for event filters

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
from plugs import event_filters


def get_function(filter):
    @filter()
    def func(self, control, index):
        raise ValueError()
    return func


def was_filtered(func, index):
    """Return True if the index was filtered"""
    self = ...
    control = ...
    try:
        func(self, control, index)
    except ValueError:
        return False
    return True


def test_filter_to_plugin():
    func = get_function(event_filters.toPluginIndex)
    assert was_filtered(func, None)
    assert was_filtered(func, 0)
    assert not was_filtered(func, (1, ))
    assert not was_filtered(func, (1, 2))


def test_filter_to_generator():
    func = get_function(event_filters.toGeneratorIndex)
    assert was_filtered(func, None)
    assert was_filtered(func, 0)
    assert was_filtered(func, (1, 2))
    assert not was_filtered(func, (1, ))


def test_filter_to_effect():
    func = get_function(event_filters.toEffectIndex)
    assert was_filtered(func, None)
    assert was_filtered(func, 0)
    assert was_filtered(func, (1, ))
    assert not was_filtered(func, (1, 2))


def test_filter_to_window():
    func = get_function(event_filters.toWindowIndex)
    assert was_filtered(func, None)
    assert was_filtered(func, (1, ))
    assert was_filtered(func, (1, 2))
    assert not was_filtered(func, 0)


def test_filter_out_none():
    func = get_function(event_filters.toSafeIndex)
    assert was_filtered(func, None)
    assert not was_filtered(func, 0)
    assert not was_filtered(func, (1, ))
    assert not was_filtered(func, (1, 2))
