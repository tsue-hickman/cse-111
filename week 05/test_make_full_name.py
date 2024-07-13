from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('John', 'Smith') == 'Smith; John'
    assert make_full_name('Jane', 'Smith-Doe') == 'Smith-Doe; Jane'
    assert make_full_name('Issac', 'Newton') == 'Newton; Issac'

def test_extract_family_name():
    assert extract_family_name('Smith; John') == 'Smith'
    assert extract_family_name('Smith-Doe; Jane') == 'Smith-Doe'
    assert extract_family_name('Newton; Issac') == 'Newton'

def test_extract_given_name():
    assert extract_given_name('Smith; John') == 'John'
    assert extract_given_name('Smith-Doe; Jane') == 'Jane'
    assert extract_given_name('Newton; Issac') == 'Issac'
