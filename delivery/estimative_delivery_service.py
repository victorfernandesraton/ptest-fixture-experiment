from datetime import date, timedelta

from holidays import HolidayBase


class EstimativeDeliveryService:
    def __init__(self, holidays: HolidayBase):
        self.holidays = holidays

    def estimate_delivery(self, start_date: date, min: int, max: int) -> list[date]:
        result = list()
        count = max
        day = start_date
        while count > 0:

            if day.weekday() < 5 and day not in self.holidays:
                count -= 1
                if count <= max - min:
                    result.append(day)

            day = day + timedelta(days=1)
        return result
