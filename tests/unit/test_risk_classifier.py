from src.governance.risk_classifier import classify_action


def test_classify_action_r0() -> None:
    assert classify_action(False, False) == "R0"


def test_classify_action_r2() -> None:
    assert classify_action(True, False) == "R2"


def test_classify_action_r3() -> None:
    assert classify_action(False, True) == "R3"