

test: test/src test/engine
	@ echo "all done"

test/src:
	cd src && \
	python3 -m unittest

test/engine:
	cd src/engine && \
	python3 -m unittest
