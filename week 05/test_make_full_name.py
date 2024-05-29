def test_make_full_name():
    assert make_full_name('John', 'Smith') == 'John Smith'
    assert make_full_name('Jane', 'Smith-Doe') == 'Jane Smith-Doe'
    assert make_full_name('Issac' , 'Newton') == 'Issac Newton'