"""Simple test to see code paths for mojibake fix."""

import ftfy

def test_simple():
    c = b'\xed\xa0\xbd\xed\xb8\x81'
    v = c * 4
    expected ='😁😁😁😁'
    
    assert expected == ftfy.fixes.fix_encoding(v.decode('latin1'))
