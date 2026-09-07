import fastf1
import pandas as pd

fastf1.Cache.enable_cache('f1_cache')

#picks a race
YEAR = 2023
GRAND_PRIX = 'Singapore'
SESSION = 'R'  # R = Race
race_name = f'{YEAR} {GRAND_PRIX}'

session = fastf1.get_session(YEAR, GRAND_PRIX, SESSION)
session.load()  # downloads laps, telemetry, timing data

laps = session.laps

print(f"Loaded {len(laps)} laps from {YEAR} {GRAND_PRIX}")
print("-" * 50)

# --- PIT STOP LOSS TIME ---
# A pit stop shows up in the data as a lap with a PitInTime and the
# NEXT lap having a PitOutTime. We compare that lap's time to a normal
# "green flag" lap to estimate how much time the stop actually cost.

def estimate_pit_loss(laps_df):
    pit_laps = laps_df[laps_df['PitInTime'].notna()]
    results = []

    for _, pit_lap in pit_laps.iterrows():
        driver = pit_lap['Driver']
        lap_num = pit_lap['LapNumber']

        # Get that driver's "normal" lap time (median of their race,
        # excluding in/out laps) as a baseline to compare against.
        driver_laps = laps_df[laps_df['Driver'] == driver]
        normal_laps = driver_laps[
            driver_laps['PitInTime'].isna() &
            driver_laps['PitOutTime'].isna()
        ]

        if normal_laps.empty or pd.isna(pit_lap['LapTime']):
            continue

        median_lap_time = normal_laps['LapTime'].median()
        pit_lap_time = pit_lap['LapTime']

        if pd.isna(median_lap_time):
            continue

        loss = (pit_lap_time - median_lap_time).total_seconds()
        results.append({
            'Driver': driver,
            'Lap': lap_num,
            'PitLapTime': pit_lap_time,
            'NormalLapTime': median_lap_time,
            'EstimatedLoss_sec': round(loss, 2)
        })

    return pd.DataFrame(results)


pit_loss_df = estimate_pit_loss(laps)
print("PIT STOP TIME LOSS (per stop):")
print(pit_loss_df)
print()

if not pit_loss_df.empty:
    print(f"Average pit loss at {GRAND_PRIX}: "
          f"{pit_loss_df['EstimatedLoss_sec'].mean():.2f} sec")
print("-" * 50)


# --- TIRE DEGRADATION (fresh vs worn) ---
# For each stint, compare lap time early in the stint (lap 2-3 on that
# tire, letting the out-lap settle) vs later in the stint, same compound.

def estimate_tire_degradation(laps_df):
    results = []

    for driver in laps_df['Driver'].unique():
        driver_laps = laps_df[laps_df['Driver'] == driver]

        for stint_num in driver_laps['Stint'].unique():
            stint_laps = driver_laps[driver_laps['Stint'] == stint_num]
            stint_laps = stint_laps[stint_laps['LapTime'].notna()]

            if len(stint_laps) < 5:
                continue  # skip short stints, not enough data

            compound = stint_laps['Compound'].iloc[0]

            # Early stint = tire age 2-3 (skip lap 1, the out-lap)
            early = stint_laps[stint_laps['TyreLife'].between(2, 3)]
            # Late stint = last 3 laps of the stint
            late = stint_laps.iloc[-3:]

            if early.empty or late.empty:
                continue

            early_avg = early['LapTime'].mean().total_seconds()
            late_avg = late['LapTime'].mean().total_seconds()
            delta = late_avg - early_avg
            laps_elapsed = late['TyreLife'].mean() - early['TyreLife'].mean()

            if laps_elapsed <= 0:
                continue

            per_lap_deg = delta / laps_elapsed

            results.append({
                'Driver': driver,
                'Stint': stint_num,
                'Compound': compound,
                'EarlyStintPace_sec': round(early_avg, 2),
                'LateStintPace_sec': round(late_avg, 2),
                'DegPerLap_sec': round(per_lap_deg, 3)
            })

    return pd.DataFrame(results)

deg_df = estimate_tire_degradation(laps)
print("TIRE DEGRADATION (seconds lost per lap, by compound):")
print(deg_df)
print()

if not deg_df.empty:
    print("Average degradation per compound:")
    print(deg_df.groupby('Compound')['DegPerLap_sec'].mean().round(3))

# --- SAVE RESULTS ---
import os

# Pit loss results
file = 'pit_loss_results.csv'

if os.path.exists(file):
    with open(file, 'a', newline='') as f:
        f.write('\n')
        f.write(f'RACE: {race_name}\n')

pit_loss_df.to_csv(
    file,
    mode='a',
    header=not os.path.exists(file),
    index=False
)


# Tire degradation results
file = 'tire_degradation_results.csv'

if os.path.exists(file):
    with open(file, 'a', newline='') as f:
        f.write('\n')
        f.write(f'RACE: {race_name}\n')

deg_df.to_csv(
    file,
    mode='a',
    header=not os.path.exists(file),
    index=False
)

print(f"\nSaved results for {race_name}")


#working 13/8/26