import pandas as pd
import matplotlib.pyplot as plt

empdata = {"empid": [1001, 1002, 1003, 1004, 1005], "ename": [
    "ganesh rao", "amrutha", "rekha", "srinivas", "tarun"], "sal": [10000, 30000, 60000, 90000, 95000]}

df = pd.DataFrame(empdata)
x = df['empid']
y = df['sal']


plt.bar(x, y, color='black')
plt.xlabel("employee id no's")
#Text(0.5,0,"employee id numbers")
plt.ylabel("employee salaries")
plt.title("talent accurate company")
plt.legend()
plt.show()
