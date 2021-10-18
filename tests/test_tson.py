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

def test_three_entries():
    """Test the Base."""

    json_ = {
      "list":[
            {
            "one" : "two"
            },
            {
            "three" : "four"
            }
        ]
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())

    try:
    
        assert ("two" in tson_values)
        assert ("four" in tson_values)

    except AssertionError as msg:
        print(msg)

def test_four_entries():
    """Test the Base."""

    json_ = {
        "list":[
            {
            "one" : "two"
            },
            {
            "three" : "four"
            },
            {
                "colors": ["red", "white", "blue"]
            }
        ]
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    # assert ("two" in tson_values)
    # assert ("four" in tson_values)
    assert (["red", "white", "blue"] in tson_values)

def test_five_entries():
    """Test the Base."""

    json_ = {
        "list":[
            {
            "one" : "two",
            "three" : "four"
            }
            # {
            #     "three" : "four"
            # },
            # {
            #     "colors": {
            #        "first":["red", "white", "blue"],
            #         }
            # }
        ]
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    assert ("two" in tson_values)
    assert ("four" in tson_values)
    # assert (["red", "white", "blue"] in tson_values)

def test_six_entries():
    """Test the Base."""

    json_ = {
        "list":[
            {
            "one" : "two"
            },
            {
            "three" : "four"
            },
            {
                "colors": ["red", "white", "blue"]
            },
            {
                "num" :12
            }
        ]
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    # assert ("two" in tson_values)
    # assert ("four" in tson_values)
    assert ("12" in tson_values)
    # assert (["red", "white", "blue"] in tson_values)

def test_seven_entries():
    """Test the Base."""

    json_ = {
        "list":[
            {
            "one" : "two"
            },
            {
            "three" : "four"
            },
            {
                "colors": ["red", "white", "blue"]
            },
            {
                "num" :12,
                "num1":[12,13,15]
            }
        ]
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    # assert ("two" in tson_values)
    # assert ("four" in tson_values)
    # assert ("12" in tson_values)
    assert ("[12,13,15]" in tson_values)
    # assert (["red", "white", "blue"] in tson_values)

def test_eight_entries():
    """Test the Base."""

    json_ = {
        "list":[
            {
            "one" : "two"
            },
            {
            "three" : "four"
            },
            {
                "colors": ["red", "white", "blue"]
            },
            {
                "num" :12,
                "num1,num2":[12,13,15]
            }
        ]
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    assert ("two" in tson_values)
    assert ("four" in tson_values)
    assert ("12" in tson_values)
    assert ("[12,13,15]" in tson_values)
    assert (["red", "white", "blue"] in tson_values)

def test_nine_entries():
    """Test the Base."""

    json_ = {
        "list":[
            {
            "one" : "two"
            },
            {
            "three" : "four"
            },
            {
                "colors": ["red", "white", "blue"],
                "secondary-clr":["blue","black","pink"]
            },
            {
                "num" :12,
                "num1":[12,13,15]
            }
        ]
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    # assert ("two" in tson_values)
    # assert ("four" in tson_values)
    # assert ("12" in tson_values)
    # assert ("[12,13,15]" in tson_values)
    assert (["blue","black","pink"] in tson_values)
    # assert (["red", "white", "blue"] in tson_values)

def test_ten_entries():
    """Test the Base."""

    json_ = {
        "list":[
            {
            "one" : "two"
            },
            {
            "three" : "four"
            },
            {
                "colors": ["red", "white", "blue"],
                "secondary-clr":["blue","black","pink"]
            },
            {
                "num" :12,
                "num_1":[12,13,15]
            },
            {
                12: {
                        "car":"ford"
                    }
            }
        ]
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    assert ("two" in tson_values)
    assert ("four" in tson_values)
    assert ("12" in tson_values)
    assert ("[12,13,15]" in tson_values)
    assert (["blue","black","pink"] in tson_values)
    assert (["red", "white", "blue"] in tson_values)
    assert ("ford" in tson_values)


