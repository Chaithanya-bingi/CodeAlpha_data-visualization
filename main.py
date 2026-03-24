import subprocess

scripts = [
    "scripts/test_dataset.py",
    "scripts/data_cleaning.py",
    "scripts/data_analysis.py",
    "scripts/visualization.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(["python", script])