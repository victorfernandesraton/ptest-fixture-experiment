from unittest.case import TestCase

from delivery.domain.models import VeichileModel, VeichileStatus

_test = TestCase()


def test_insert_one_veichile(create_veichile_database):
    database = create_veichile_database
    search_veichile = database.get_veichile_by_id(1)
    _test.assertIsNone(search_veichile)
    veichile = VeichileModel(
        id=1,
        plate="CNC-1212",
        status=VeichileStatus.AVAILABLE,
    )
    created_veichile = database.create_veichile(veichile)
    _test.assertEqual(created_veichile.id, 1)


def test_update_veichile_status(create_veichile_database):
    database = create_veichile_database
    search_veichile = database.get_veichile_by_id(1)
    _test.assertEqual(search_veichile.status, VeichileStatus.AVAILABLE)
    updated_veichile = database.update_veichile_status(
        search_veichile.id, VeichileStatus.UNAVAILABLE
    )

    get_updated_veichile = database.get_veichile_by_id(1)

    _test.assertEqual(updated_veichile.id, search_veichile.id)
    _test.assertNotEqual(updated_veichile.status, search_veichile.status)
    _test.assertEqual(updated_veichile.status, VeichileStatus.UNAVAILABLE)
    _test.assertEqual(get_updated_veichile.status, VeichileStatus.UNAVAILABLE)
