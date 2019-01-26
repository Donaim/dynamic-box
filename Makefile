

test: test/src
	@ echo "all done"

test/src:
	cd src && \
	python3 -m unittest

