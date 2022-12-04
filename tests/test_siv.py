from immatricuation.siv import isValid


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
