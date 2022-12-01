# Lists available recipes
@menu:
    just --list --unsorted

# Creates a template for today's problem
@setup:
    python3 problem_setup.py
    echo Today setup. Good luck!

# Creates a template for a given day and year's problem
@setup-day day year:
    python3 problem_setup.py --day {{day}} --year {{year}}
    echo Day {{day}} and {{year}} setup. Good luck!