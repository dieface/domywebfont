#!/usr/bin/python
#
# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Routines for character coverage of fonts."""

__author__ = "roozbeh@google.com (Roozbeh Pournader)"

import sys
import json
from fontTools import ttLib


def character_set(font):
    """Returns the character coverage of a font.

    Args:
      font: The input font's file name, or a TTFont.

    Returns:
      A frozenset listing the characters supported in the font.
    """
    if type(font) is str:
        font = ttLib.TTFont(font)
    cmap_table = font["cmap"]


    cmaps = {}
    for table in cmap_table.tables:
        if (table.format, table.platformID, table.platEncID) in [
            (4, 3, 1), (12, 3, 10)]:
            cmaps[table.format] = table.cmap
    if 12 in cmaps:
        cmap = cmaps[12]
    elif 4 in cmaps:
        cmap = cmaps[4]
    else:
        cmap = {}
    # names = {}        
    # for code, name in cmap.items():
        # names[name] = code
        # print "names[%s] = %s" % (name, code)
    f = open('/Users/brucelee/Documents/workspace/doing_custom_fonts/input/NotoSansCJKsc_SimplifiedChinese/cmap','wb')
    # f.write(json.dumps(sorted(frozenset(cmap.keys())))) # python will convert \n to os.linesep
    f.write(json.dumps(cmap)) # python will convert \n to os.linesep
    f.close() # you can omi

    return frozenset(cmap.keys())


def convert_set_to_ranges(charset):
    """Converts a set of characters to a list of ranges."""
    working_set = set(charset)
    output_list = []
    while working_set:
        start = min(working_set)
        end = start + 1
        while end in working_set:
            end += 1
        output_list.append((start, end - 1))
        working_set.difference_update(range(start, end))
    return output_list


def main(argv):
    """Outputs the character coverage of fonts given on the command line."""
    import unicode_data
    # f = open('/Users/brucelee/Documents/workspace/noto_source/noto-c21755e239ef/nototools/noto_chars','wb')
    print argv[1:]
    for font in argv[1:]:
        # print "%s:" % font
        for char in sorted(character_set(font)):
            try:
                name = unicode_data.name(char)
            except ValueError:
                name = "<Unassigned>"
            line = "U+%04X %s\n" % (char, name)
            # f.write(line)
            # print "U+%04X %s" % (char, name)
    # f.close()


if __name__ == "__main__":
    main(sys.argv)
