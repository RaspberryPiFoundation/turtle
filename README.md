## Turtle

An implementation of Python's native turtle module that works with Pyodide.

Instead of rendering to a tkinter window, this package outputs a Python dict
that represents an SVG which can then be added to the DOM. This allows the
package to be used either natively on the web page or within a web worker where
the JavaScript document is not available.

## Demo

Run `./bin/server` then visit http://localhost:8000/demo-pyodide.html to see a
demo of the turtle package. Notice that the output at the bottom is an SVG.

## Limitations

This turtle package does not support user interaction, such as hover or click
events. Search `__init__.py` for 'not implemented' and `svg.py` for
'NotImplemented' to see which methods are not implemented.

## License

This package was adapted from
[Basthon's turtle](https://framagit.org/basthon/basthon-kernel/-/tree/master/packages/kernel-python3/src/modules/turtle?ref_type=heads)
package. It therefore has the same GPLv3 license.

See the banner at the top of `__init__.py`.
