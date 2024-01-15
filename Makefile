build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf *.egg-info/ build/ dist/

.PHONY: build clean
