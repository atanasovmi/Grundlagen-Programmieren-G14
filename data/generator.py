import random
from datetime import datetime, timedelta

start = datetime(2025,1,1)
end   = datetime(2025,12,15)

exercises = {
    'Schwimmen': 8,
    'Joggen': 10,
    'Krafttraining': 6,
    'Radfahren': 6,
    'Yoga': 4,
}

entries = []

cur = start
while cur <= end:
    if random.random() < 0.45:  # 45% Trainigswahrscheinlichkeit ≈ 15–20% weniger als 0.55
        for _ in range(random.randint(1,3)):
            ex, factor = random.choice(list(exercises.items()))
            if ex == 'Yoga':
                minutes = max(15, int(random.gauss(50, 15)))
            elif ex == 'Joggen':
                minutes = max(20, int(random.gauss(40, 10)))
            elif ex == 'Krafttraining':
                minutes = max(25, int(random.gauss(55, 15)))
            elif ex == 'Radfahren':
                minutes = max(20, int(random.gauss(45, 12)))
            else:  # Schwimmen
                minutes = max(20, int(random.gauss(35, 10)))
            kcal = minutes * factor
            entries.append((cur.strftime('%d.%m.%Y'), ex, minutes, kcal))
    cur += timedelta(days=1)

print(len(entries))
print('\n'.join(f"{d},{e},{m},{k}" for d,e,m,k in entries))