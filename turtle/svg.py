# Modified version of Brython's SVG module
# Author: Romain Casati
# License: GPL v3 or higher

from js import document


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
        node = document.createElementNS(_svg_ns, tag)
        # this is mandatory to display svg properly
        if tag == 'svg':
            node.setAttribute('xmlns', _svg_ns)
        for arg in args:
            if isinstance(arg, (str, int, float)):
                arg = document.createTextNode(str(arg))
            node.appendChild(arg)
        for key, value in kwargs.items():
            key = key.lower()
            if key[0:2] == "on":
                # Event binding passed as argument "onclick", "onfocus"...
                # Better use method bind of DOMNode objects
                node.addEventListener(key[2:], value)
            elif key == "style":
                node.setAttribute("style", ';'.join(f"{k}: {v}"
                                                    for k, v in value.items()))
            elif "href" in key:
                node.setAttributeNS(_xlink_ns, "href", value)
            elif value is not False:
                # option.selected=false sets it to true :-)
                node.setAttributeNS(None, key.replace('_', '-'), value)
        return node
    return func


for tag in _svg_tags:
    vars()[tag] = _tag_func(tag)
