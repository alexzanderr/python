
"""
    core/__json.py

    upgraded version of json.py
    useful in work with jsons

    author: @alexzander
"""


# python
import os
import json
from pathlib import Path


def read_json_from_file(__path: str):
    """ reads .json from @path"""

    if isinstance(__path, str):
        with open(__path, "r+", encoding="utf-8") as _json:
            return json.loads(_json.read())

    elif isinstance(__path, Path):
        return json.loads(__path.read_text())

    else:
        raise TypeError(
            f"{__path} is not type str; type({__path})=={type(__path)}")



def write_json_to_file(
    __collection: dict,
    destination: str,
    __indent=4
):

    if isinstance(destination, str):
        with open(destination, "w+", encoding="utf-8") as _json:
            _json.truncate(0)
            if isinstance(__collection, dict) or isinstance(__collection, list):
                _json.write(json.dumps(__collection, indent=__indent))
            else:
                _json.write(json.dumps(
                    __collection,
                    indent=__indent,
                    default=lambda custom_object: custom_object.__dict__
                ))

    elif isinstance(destination, Path):
        if isinstance(__collection, dict) or isinstance(__collection, list):
            destination.write_text(json.dumps(
                __collection,
                indent=4
            ))
        else:
            destination.write_text(json.dumps(
                __collection,
                indent=4,
                default=lambda custom_object: custom_object.__dict__
            ))


def prettify(__collection, __indent=4):
    if isinstance(__collection, dict) or isinstance(__collection, list):
        return json.dumps(__collection, indent=__indent)

    # this default is useful when you want
    # to make your class JSON Serializable
    return json.dumps(
        __collection,
        indent=__indent,
        default=lambda custom_object: custom_object.__dict__
    )


def pretty_print(__collection, __indent=4):
    print(prettify(__collection, __indent=__indent))


# TESTING
if __name__ == '__main__':
    pass
