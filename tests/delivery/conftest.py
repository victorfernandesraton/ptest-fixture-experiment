from datetime import date

import pytest
from holidays import country_holidays
from holidays.countries import BR
from holidays.holiday_base import HolidayBase


class CustonNordesteCalendar(BR):
    def _populate(self, year):
        super()._populate(year)
        self[date(year, 6, 24)] = "Véspera de São João"
        self[date(year, 6, 25)] = "São João"


@pytest.fixture(scope="module")
def default_holidays():
    calendar = country_holidays("BR")
    return calendar


@pytest.fixture(scope="module")
def custon_holidays(default_holidays):
    return default_holidays + CustonNordesteCalendar()
