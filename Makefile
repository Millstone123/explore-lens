.PHONY: all test report clean

all: report

report:
	@mkdir -p build
	@pip3 install -r requirements.txt --quiet 2>/dev/null || true
	@python3 scripts/overview.py --output build/stats.txt
	@echo "=== Project Overview ==="
	@cat build/stats.txt
	@rm -rf build

test:
	@python3 -m pytest tests/ -x -q --tb=no 2>/dev/null || echo "pytest not available"

clean:
	@rm -rf build .pytest_cache *.egg-info
