.PHONY: help setup trends analytics query stats clean all

# Color output
RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[1;33m
BLUE=\033[0;34m
NC=\033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)CISA KEV Analytics - Available Commands$(NC)"
	@echo "=========================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-15s$(NC) %s\n", $$1, $$2}'

setup: ## Setup Python environment and install dependencies
	@echo "$(YELLOW)Setting up environment...$(NC)"
	@chmod +x setup.sh
	@./setup.sh
	@echo "$(GREEN)✓ Setup complete!$(NC)"

analytics: ## Generate comprehensive analytics dashboard (all visualizations)
	@echo "$(YELLOW)Generating comprehensive analytics...$(NC)"
	@. venv/bin/activate && python scripts/kev_analytics.py
	@echo "$(GREEN)✓ Analytics complete! Check outputs/graphs/$(NC)"

stats: ## Show KEV database statistics
	@echo "$(YELLOW)Fetching statistics...$(NC)"
	@. venv/bin/activate && python scripts/kev_query.py --stats

update-readme-stats: ## Update statistics in README.md
	@echo "$(YELLOW)Generating updated statistics...$(NC)"
	@. venv/bin/activate && python scripts/generate_stats.py > /tmp/kev_stats.md
	@echo "$(GREEN)✓ Stats generated! Manually update README.md with content from /tmp/kev_stats.md$(NC)"

query-vendor: ## Query by vendor (usage: make query-vendor VENDOR="Microsoft")
	@. venv/bin/activate && python scripts/kev_query.py --vendor "$(VENDOR)" --details

query-product: ## Query by product (usage: make query-product PRODUCT="Windows")
	@. venv/bin/activate && python scripts/kev_query.py --product "$(PRODUCT)" --details

query-cve: ## Query specific CVE (usage: make query-cve CVE="CVE-2024-1234")
	@. venv/bin/activate && python scripts/kev_query.py --cve "$(CVE)"

recent: ## Show CVEs added in last 7 days (usage: make recent DAYS=7)
	@. venv/bin/activate && python scripts/kev_query.py --recent ${DAYS:-7}

ransomware: ## Show ransomware-associated CVEs
	@echo "$(RED)🦠 Ransomware-associated CVEs:$(NC)"
	@. venv/bin/activate && python scripts/kev_query.py --ransomware --details

scannable: ## Show only scannable CVEs
	@echo "$(GREEN)✅ Scannable CVEs:$(NC)"
	@. venv/bin/activate && python scripts/kev_query.py --scannable

unscannable: ## Show only unscannable CVEs
	@echo "$(RED)❌ Unscannable CVEs:$(NC)"
	@. venv/bin/activate && python scripts/kev_query.py --unscannable

all: analytics ## Generate all visualizations
	@echo "$(GREEN)✓ All visualizations generated!$(NC)"

clean: ## Clean up generated files
	@echo "$(YELLOW)Cleaning up generated files...$(NC)"
	@rm -rf outputs/graphs/*.png
	@echo "$(GREEN)✓ Cleaned!$(NC)"

clean-all: clean ## Clean everything including virtual environment
	@echo "$(YELLOW)Removing virtual environment...$(NC)"
	@rm -rf venv
	@echo "$(GREEN)✓ Everything cleaned!$(NC)"

show-outputs: ## List all generated output files
	@echo "$(BLUE)Generated Files:$(NC)"
	@ls -lh outputs/graphs/ 2>/dev/null || echo "No outputs yet. Run 'make all' to generate."

show-stats: ## Display comprehensive statistics
	@. venv/bin/activate && python scripts/generate_stats.py

quick-start: setup all ## Quick start: setup + generate all visualizations
	@echo "$(GREEN)✓ Quick start complete!$(NC)"
	@echo "Check out the generated PNG files!"

# Examples
examples: ## Show usage examples
	@echo "$(BLUE)Usage Examples:$(NC)"
	@echo "  make setup                              # First-time setup"
	@echo "  make analytics                          # Generate all analytics"
	@echo "  make stats                              # Show statistics"
	@echo "  make query-vendor VENDOR=\"Microsoft\"    # Search by vendor"
	@echo "  make query-product PRODUCT=\"Chrome\"     # Search by product"
	@echo "  make query-cve CVE=\"CVE-2024-1234\"      # Lookup specific CVE"
	@echo "  make recent DAYS=30                     # CVEs from last 30 days"
	@echo "  make ransomware                         # Ransomware CVEs"
	@echo "  make all                                # Generate everything"
	@echo "  make clean                              # Remove generated files"
