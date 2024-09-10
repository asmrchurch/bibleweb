#!/usr/bin/env python3

import sys

section=sys.argv[1]

lines = []

filename = f"public/static/html/norm/{section}.htm"
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()

        if '<div style="display:block;margin-left:32px;text-indent:0px;">' in line:
            line = line.replace(
                '<div style="display:block;margin-left:32px;text-indent:0px;">',
                '<div style="display:block;margin-left:32px;text-indent:0px;" id="verse">'
            )

        if("</em>" in line):
            em, text = line.split("</em>" )
            text = f"<span id='verse'>{text}</span>"
            lines.append(f"{em}</em>{text}")
        else:
            lines.append(line)

linestr = "\n".join(lines)
with open(filename, 'w') as file:
    file.write(linestr)
