from datetime import datetime

date1 = datetime(2021, 1, 1, 12, 0, 0)
date2 = datetime(2022, 1, 2, 12, 0, 0)

difference_seconds = (date2 - date1).total_seconds()

print("Difference in seconds:", difference_seconds)
