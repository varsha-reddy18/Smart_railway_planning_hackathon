import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = {
    "train_id": np.arange(1000, 1000+n),
    "arrival_hour": np.random.randint(0, 24, n),
    "departure_hour": np.random.randint(0, 24, n),
    "passenger_count": np.random.randint(100, 1000, n),
    "platform_number": np.random.randint(1, 6, n),
    "track_number": np.random.randint(1, 4, n),
    "delay_minutes": np.random.randint(0, 30, n)
}

df = pd.DataFrame(data)

df.to_csv("data/railway_data.csv", index=False)

print("Dataset generated successfully!")