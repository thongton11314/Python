#py -3 -m venv .venv
#.venv\scripts\activate
#Windows (may require elevation)
#python -m pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Make fake dataset
data = {"United State": 100, "England": 75, "Vietnam": 50, "Lao": 25}
ranks = [data["United State"], data["England"], data['Vietnam'], data["Lao"]]
bars = ('United State', 'England', 'VietNam', 'Lao')

#Horizontal bar
y_pos = np.arange(len(bars))
#Create names on the x-axis
plt.yticks(y_pos, bars)
#Create verticle bars
plt.barh(y_pos, ranks)
#Show graphic
plt.show()
