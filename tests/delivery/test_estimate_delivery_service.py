from datetime import date
from unittest.case import TestCase

import pytest

from delivery import EstimativeDeliveryService

_test = TestCase()


@pytest.mark.delivery
def test_calculate_delivery_in_ordinary_day(holidays_base):
    service = EstimativeDeliveryService(holidays_base)
    result = service.estimate_delivery(date(2024, 5, 10), 5, 8)
    _expected_size = 3
    _expcted_result = [
        date(2024, 5, 16),
        date(2024, 5, 17),
        date(2024, 5, 20),
        date(2024, 5, 21),
    ]
    _test.assertEqual(len(result), 4)
    for item in result:
        _test.assertIn(item, _expcted_result)
