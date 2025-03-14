import pytest
from countnclear.counter import CountFlushTerm

def test_count_flush_term():
    # Bu test faqat funksiyani chaqirib, xato chiqmasligini tekshiradi
    result = CountFlushTerm(3)
    assert result == "" or result is None