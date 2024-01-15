# Modified version of Brython's SVG module
# Author: Romain Casati
# License: GPL v3 or higher

_svg_ns = "http://www.w3.org/2000/svg"
_xlink_ns = "http://www.w3.org/1999/xlink"

_svg_tags = ['a',
             'altGlyph',
             'altGlyphDef',
             'altGlyphItem',
             'animate',
             'animateColor',
             'animateMotion',
             'animateTransform',
             'circle',
             'clipPath',
             'color_profile',  # instead of color-profile
             'cursor',
             'defs',
             'desc',
             'ellipse',
             'feBlend',
             'foreignObject',  # patch to enable foreign objects
             'g',
             'image',
             'line',
             'linearGradient',
             'marker',
             'mask',
             'path',
             'pattern',
             'polygon',
             'polyline',
             'radialGradient',
             'rect',
             'set',
             'stop',
             'svg',
             'text',
             'tref',
             'tspan',
             'use']


def _tag_func(tag):
    def func(*args, **kwargs):
        node = { "tag": tag, "props": {}, "children": [] }
        # this is mandatory to display svg properly
        if tag == 'svg':
            node["props"]["xmlns"] = _svg_ns
            node["props"]["xmlns:xlink"] = _xlink_ns
        for arg in args:
            if isinstance(arg, (str, int, float)):
                arg = { "text": str(arg) }
            node["children"].append(arg)
        for key, value in kwargs.items():
            key = key.lower()
            if key[0:2] == "on":
                raise NotImplementedError
            elif key == "style":
                node["props"]["style"] = ';'.join(f"{k}: {v}" for k, v in value.items())
            elif "href" in key:
                node["props"]["href"] = value
            elif value is not False:
                # option.selected=false sets it to true :-)
                node["props"][key.replace('_', '-')] = value
        return node
    return func


for tag in _svg_tags:
    vars()[tag] = _tag_func(tag)
