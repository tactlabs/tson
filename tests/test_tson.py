"""Tests for `tson` package."""

import pytest
import core


def test_command_line_interface():
    """Test the CLI."""

    a = 2
    b = 3

    c = a + b

    json_ = {
        "one" : "two"
    }

    tson_ = core.convert_json_to_tson(json_)
    # print(tson_)

    tson_values = list(tson_['result'].values())
    
    assert ("two" in tson_values)