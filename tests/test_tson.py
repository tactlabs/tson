"""Tests for `tson` package."""

import pytest
import core


def test_simple():
    """Test the Base."""

    json_ = {
        "one" : "two"
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    assert ("two" in tson_values)

def test_two_entries():
    """Test the Base."""

    json_ = {
        "one" : "two",
        "three" : "four"
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    assert ("two" in tson_values)
    assert ("four" in tson_values)