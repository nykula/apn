all:
	find . -type f -name '*.txt' -exec python3 iterator.py "{}" \;
