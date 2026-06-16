from pathlib import Path

path = Path("reports/salary.txt")

path.parent.mkdir(exist_ok= True)
path.write_text("Dinesh salary 1000000 Sruthi Salary 2000000")