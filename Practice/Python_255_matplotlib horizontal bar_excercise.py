#py -3 -m venv .venv
#.venv\scripts\activate
#Windows (may require elevation)
#python -m pip install matplotlib

import matplotlib as plt
import numpy as np
data = {"Vietnam": 50, "United State": 100, "England": 75, "Lao": 25}
y_pos = np.arrage(len(data))
plt.barh(y_pos, data)