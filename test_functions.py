#!/usr/bin/env python3
from functions import print_message

def test_message():
    message = "test"
    assert isinstance(print_message(message),str)
