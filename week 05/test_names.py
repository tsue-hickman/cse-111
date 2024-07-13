from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    full_name = make_full_name("Sally", "Brown")
    assert full_name == "Brown; Sally"

def test_extract_family_name():
    family_name = extract_family_name("Brown; Sally")
    assert family_name == "Brown"

def test_extract_given_name():
    given_name = extract_given_name("Brown; Sally")
    assert given_name == "Sally"



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file


# ############ using string operations ###########
# def test_make_full_name():
#     assert make_full_name("John", "Doe") == "Doe; John"
#     assert make_full_name("Jane", "Smith-Doe") == "Smith-Doe; Jane"
#     assert make_full_name("Michael", "") == "; Michael"
#     assert make_full_name("", "Williams") == "Williams; "

# def test_extract_family_name():
#     assert extract_family_name("Doe; John") == "Doe"
#     assert extract_family_name("Smith-Doe; Jane") == "Smith-Doe"
#     assert extract_family_name("; Michael") == ""
#     assert extract_family_name("Williams; ") == "Williams"

# def test_extract_given_name():
#     assert extract_given_name("Doe; John") == "John"
#     assert extract_given_name("Smith-Doe; Jane") == "Jane"
#     assert extract_given_name("; Michael") == "Michael"
#     assert extract_given_name("Williams; ") == ""


############# using test cases #############
# def test_make_full_name():
#     test_cases = [
#         ("John", "Doe", "Doe; John"),
#         ("Jane", "Smith-Doe", "Smith-Doe; Jane"),
#         ("Michael", "", "; Michael"),
#         ("", "Williams", "Williams; ")
#     ]
#     for given_name, family_name, expected_output in test_cases:
#         assert make_full_name(given_name, family_name) == expected_output

# def test_extract_family_name():
#     test_cases = [
#         ("Doe; John", "Doe"),
#         ("Smith-Doe; Jane", "Smith-Doe"),
#         ("; Michael", ""),
#         ("Williams; ", "Williams")
#     ]
#     for full_name, expected_output in test_cases:
#         assert extract_family_name(full_name) == expected_output

# def test_extract_given_name():
#     test_cases = [
#         ("Doe; John", "John"),
#         ("Smith-Doe; Jane", "Jane"),
#         ("; Michael", "Michael"),
#         ("Williams; ", "")
#     ]
#     for full_name, expected_output in test_cases:
#         assert extract_given_name(full_name) == expected_output



############# using parametrized tests #############

# import pytest

# @pytest.mark.parametrize("given_name, family_name, expected_output", [
#     ("John", "Doe", "Doe; John"),
#     ("Jane", "Smith-Doe", "Smith-Doe; Jane"),
#     ("Michael", "", "; Michael"),
#     ("", "Williams", "Williams; ")
# ])
# def test_make_full_name(given_name, family_name, expected_output):
#     assert make_full_name(given_name, family_name) == expected_output

# @pytest.mark.parametrize("full_name, expected_output", [
#     ("Doe; John", "Doe"),
#     ("Smith-Doe; Jane", "Smith-Doe"),
#     ("; Michael", ""),
#     ("Williams; ", "Williams")
# ])
# def test_extract_family_name(full_name, expected_output):
#     assert extract_family_name(full_name) == expected_output

# @pytest.mark.parametrize("full_name, expected_output", [
#     ("Doe; John", "John"),
#     ("Smith-Doe; Jane", "Jane"),
#     ("; Michael", "Michael"),
#     ("Williams; ", "")
# ])
# def test_extract_given_name(full_name, expected_output):
#     assert extract_given_name(full_name) == expected_output