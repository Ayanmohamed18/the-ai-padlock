# Pit Stop Time Calculator - Episode 1
#The AI Padlock

# --- Race data (variables) ---
team = "Red Bull Racing"
driver = "Max Verstappen"
total_laps = 57
laps_completed = 22
avg_lap_time = 92.4      # seconds per lap
pit_stop_time = 2.4      # seconds stationary in the box
pit_lane_loss = 20.0     # seconds lost driving through the pit lane

# --- Calculations (operators) ---
total_pit_cost = pit_stop_time + pit_lane_loss
laps_remaining = total_laps - laps_completed
time_on_track = laps_remaining * avg_lap_time
projected_finish = time_on_track + total_pit_cost

minutes = int(projected_finish // 60)
seconds = round(projected_finish % 60, 1)

pit_is_cheap = total_pit_cost < 25   # a boolean (True/False)

# --- Output ---
print("=== PIT STOP CALCULATOR ===")
print("Driver:", driver, "|", team)
print("Laps remaining:", laps_remaining)
print("Total pit stop cost:", total_pit_cost, "seconds")
print("Projected finish time:", minutes, "min", seconds, "sec")
print("Is this a cheap stop?", pit_is_cheap)