.PHONY: manager
manager:
	@echo "Building coin-operated light show manager"
	cd manager && hatch -e py3.9.2-1.0  build

.PHONY: vessel
manager:
	@echo "Building coin-operated light show vessel"
	cd vessel && hatch -e py3.9.2-1.0  build

.PHONY: witch
manager:
	@echo "Building coin-operated light show witch"
	cd witch && hatch -e py3.9.2-1.0 build