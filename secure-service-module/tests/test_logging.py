import logging


def test_registeration_succeeds(service, caplog):
    caplog.set_level(logging.INFO)
    service.create_user("aline", "Secret123!")
    assert "aline" in caplog.text
    assert "Secret123!" not in caplog.text
