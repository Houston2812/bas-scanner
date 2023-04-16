scanned_dir:
	touch .env
	echo "SCANNER_DIR='$$(pwd)'" > src/.env

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run: venv/bin/activate scanned_dir
	./venv/bin/python3 src/scanner.py -s directory_traversal_basic

test_config: scanned_dir
	echo "Check config"
	./venv/bin/python3 src/config.py
	
test_request: scanned_dir
	echo "Check request"
	./venv/bin/python3 tests/test.py


clean:
	rm -rf __pycache__
	rm -rf venv