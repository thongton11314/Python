#py -3 -m venv .venv
#.venv\scripts\activate
#Windows (may require elevation)
#python -m pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Make fake dataset
data = {"United State": 100, "England": 75, "Vietnam": 50, "Lao": 25}
rank = [data["United State"], data["England"], data['Vietnam'], data["Lao"]]
bars = ('United State', 'England', 'VietNam', 'Lao')
y_pos = np.arange(len(bars))
# Create horizontal bars
plt.barh(y_pos, rank)
# Create names on the y-axis
plt.yticks(y_pos, bars)
# Show graphic
plt.show()
