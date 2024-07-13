import pytest
from personality import (
    initialize_personality_scores,
    get_personality_type,
    get_type_attributes,
    get_type_mapping
)

def test_initialize_personality_scores():
    scores = initialize_personality_scores()
    assert isinstance(scores, dict)
    assert len(scores) == 8
    assert all(trait in scores for trait in [
        "extrovert", "introvert", "sensing", "intuition",
        "thinking", "feeling", "judging", "perceiving"
    ])
    assert all(score == 0 for score in scores.values())

def test_get_personality_type():
    scores1 = {
        "extrovert": 5, "introvert": 3,
        "sensing": 2, "intuition": 4,
        "thinking": 6, "feeling": 2,
        "judging": 3, "perceiving": 5
    }
    assert get_personality_type(scores1) == "ENTP"

    scores2 = {
        "extrovert": 2, "introvert": 6,
        "sensing": 5, "intuition": 3,
        "thinking": 4, "feeling": 4,
        "judging": 7, "perceiving": 1
    }
    assert get_personality_type(scores2) == "ISTJ"

def test_get_type_attributes():
    type_mapping = get_type_mapping()
    
    istj_attributes = get_type_attributes("ISTJ", type_mapping)
    assert istj_attributes == {"house": "Hufflepuff", "element": "Earth", "animal": "Beaver"}
    
    entp_attributes = get_type_attributes("ENTP", type_mapping)
    assert entp_attributes == {"house": "Ravenclaw", "element": "Air", "animal": "Monkey"}
    
    unknown_attributes = get_type_attributes("UNKNOWN", type_mapping)
    assert unknown_attributes == {"house": "Unknown", "element": "Unknown", "animal": "Unknown"}