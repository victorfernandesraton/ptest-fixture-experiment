from datetime import date
from unittest.case import TestCase

import pytest

from delivery import EstimativeDeliveryService

_test = TestCase()


@pytest.mark.delivery
def test_calculate_delivery_in_ordinary_day_with_default_calendar(default_holidays):
    service = EstimativeDeliveryService(default_holidays)
    result = service.estimate_delivery(date(2024, 5, 10), 5, 8)
    _expcted_result = [
        date(2024, 5, 16),
        date(2024, 5, 17),
        date(2024, 5, 20),
        date(2024, 5, 21),
    ]
    _test.assertEqual(len(result), len(_expcted_result))
    for item in result:
        _test.assertIn(item, _expcted_result)


@pytest.mark.delivery
def test_calculate_delivery_in_ordinary_day_with_custon_calendar(custon_holidays):
    service = EstimativeDeliveryService(custon_holidays)
    result = service.estimate_delivery(date(2024, 5, 10), 5, 8)
    _expcted_result = [
        date(2024, 5, 16),
        date(2024, 5, 17),
        date(2024, 5, 20),
        date(2024, 5, 21),
    ]
    _test.assertEqual(len(result), len(_expcted_result))
    for item in result:
        _test.assertIn(item, _expcted_result)


@pytest.mark.delivery
def test_calculate_delivery_in_special_holidays_with_default_calendar(
    default_holidays,
):
    service = EstimativeDeliveryService(default_holidays)
    result = service.estimate_delivery(date(2024, 6, 20), 5, 8)
    _expcted_result = [
        date(2024, 6, 26),
        date(2024, 6, 27),
        date(2024, 6, 28),
        date(2024, 7, 1),
    ]
    _test.assertEqual(len(result), len(_expcted_result))
    for item in result:
        _test.assertIn(item, _expcted_result)


@pytest.mark.delivery
def test_calculate_delivery_in_special_holidays_with_custon_calendar(custon_holidays):
    service = EstimativeDeliveryService(custon_holidays)
    result = service.estimate_delivery(date(2024, 6, 20), 5, 8)
    _expcted_result = [
        date(2024, 6, 28),
        date(2024, 7, 1),
        date(2024, 7, 2),
        date(2024, 7, 3),
    ]
    _test.assertEqual(len(result), len(_expcted_result))
    for item in result:
        _test.assertIn(item, _expcted_result)
