from immatricuation.siv import isValid, computeValue


def test_isValid():
    assert not isValid("lhsdljfs")
    assert isValid("aa-111-aa")
    assert isValid("AA-111-AA")
    assert not isValid("11-AAA-11")
    assert not isValid("ww-111-aa")
    assert not isValid("aa-111-ss")
    assert not isValid("ss-111-aa")
    assert not isValid("ia-111-aa")
    assert not isValid("aa-111-ua")
    assert not isValid("aa-111-oa")


def test_computeValue():
    assert computeValue("aa-001-aa") == 1
    assert computeValue("aa-999-aa") == 999

    assert computeValue("aa-001-ab") == 1000
    assert computeValue("aa-999-ab") == 1998
    assert computeValue("aa-001-ba") == 999 * 23 + 1
    assert computeValue("aa-001-ca") == 999 * 23 * 2 + 1
    assert computeValue("aa-999-zz") == 999 * (23 * 23 - 1)

    assert computeValue("ab-001-aa") == 999 * (23 * 23 - 1) + 1
    assert computeValue("ac-001-aa") == 999 * (23 * 23 - 1) * 2 + 1
    assert computeValue("ba-001-aa") == 999 * (23 * 23 - 1) * 23 + 1
    assert computeValue("ca-001-aa") == 999 * (23 * 23 - 1) * 23 * 2 + 1

    assert computeValue("zz-999-zz") == (23 * 23 - 2) * 999 * (23 * 23 - 1)
