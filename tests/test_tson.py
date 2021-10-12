"""Tests for `tson` package."""

import pytest



def test_command_line_interface():
    """Test the CLI."""

    a = 2
    b = 3

    c = a + b
    
    assert c == 5