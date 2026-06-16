from pathlib import Path

path = Path("2026/june/reports/salary.txt")

path.parent.mkdir(exist_ok= True , parents= True)
path.write_text("Dinesh salary 1000000 Sruthi Salary 2000000")