import sqlite3
from datetime import date

import pytest
from holidays import country_holidays
from holidays.countries import BR
from holidays.holiday_base import HolidayBase

from delivery.storage import VeichileStorageSqlite


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


@pytest.fixture(scope="session")
def create_database():
    db_name = ":memory:"
    conn = sqlite3.connect(db_name)

    yield conn

    conn.close()


@pytest.fixture(scope="session")
def create_veichile_database(create_database):
    conn = create_database
    db = VeichileStorageSqlite(conn)
    db.create_table()

    yield db
    db.drop_table()
