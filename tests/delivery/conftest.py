from datetime import date

import pytest
from holidays.countries import BR


class CustonNordesteCalendar(BR):
    def _populate(self, year):
        super()._populate(year)
        self[date(year, 6, 24)] = "Véspera de São João"
        self[date(year, 6, 25)] = "São João"


@pytest.fixture(scope="module")
def holidays_base():
    return CustonNordesteCalendar()
