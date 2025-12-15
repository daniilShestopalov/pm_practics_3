import numpy as np
import pandas as pd

WEEKS_FILE = "weekly_hours.csv"
TASKS_FILE = "phase5_tasks.csv"
N_RUNS = 50000
RNG = np.random.default_rng(12345)

weekly = pd.read_csv(WEEKS_FILE)
if 'hours' not in weekly.columns:
    raise ValueError("weekly_hours_test.csv must have column 'hours'")
weekly_hours = weekly['hours'].values
if len(weekly_hours) == 0:
    raise ValueError("weekly_hours_test.csv empty")

tasks = pd.read_csv(TASKS_FILE, sep=';')
req_cols = ['optimistic_hours','most_likely_hours','pessimistic_hours']
for c in req_cols:
    if c not in tasks.columns:
        raise ValueError(f"phase5_tasks.csv must have column {c}")

def sample_one_run():
    # 1) sample task durations
    a = tasks['optimistic_hours'].values
    m = tasks['most_likely_hours'].values
    b = tasks['pessimistic_hours'].values
    if not np.all((a <= m) & (m <= b)):
        raise ValueError("Ensure optimistic <= most_likely <= pessimistic for all tasks")
    sampled = RNG.triangular(a, m, b)
    total_work = sampled.sum()
    # 2) consume weekly capacities until done
    weeks = 0
    while total_work > 0:
        cap = RNG.choice(weekly_hours)
        total_work -= cap
        weeks += 1
        if weeks > 1000:
            break
    return weeks

results = np.empty(N_RUNS, dtype=float)
for i in range(N_RUNS):
    results[i] = sample_one_run()

p10 = np.percentile(results, 10)
p50 = np.percentile(results, 50)
p90 = np.percentile(results, 90)
mean = results.mean()

print(f"Runs: {N_RUNS}")
print(f"Median weeks: {p50:.1f}")
print(f"Mean weeks: {mean:.2f}")
print(f"80% central interval (10%-90%): [{p10:.1f}, {p90:.1f}] weeks")
