from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 2)
    with pytest.raises(TypeError):
        encrypt_message("FalleN", "10")

    assert encrypt_message("FalleN", 2) == "Nell_aF"
    assert encrypt_message("FalleN", 2) != "Ne_llaF"
    assert encrypt_message("FalleN", 10) == "".join("NellaF")
