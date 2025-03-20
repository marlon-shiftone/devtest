import random
import pandas as pd
from datetime import datetime, timedelta

def generate_synthetic_elevator_data(
    num_steps: int = 50,
    floors: int = 4,
    elevator_id: int = 1,
    seed: int = 42,
    start_time: str = "07:00",
    end_time: str = "21:00",
    reset_floor: int = 0,
    max_resting_minutes: int = 30
) -> pd.DataFrame:
    random.seed(seed)
    start_hour, start_min = map(int, start_time.split(":"))
    end_hour, end_min = map(int, end_time.split(":"))
    base_date = datetime.today().replace(hour=start_hour, minute=start_min, second=0, microsecond=0)

    TRANSITIONS = ["resting", "on_demand", "vacant"]
    transition_probs = {
        "resting": {"resting": 0.5, "on_demand": 0.5, "vacant": 0.0},
        "on_demand": {"resting": 0.4, "on_demand": 0.6, "vacant": 0.0},
        "vacant": {"resting": 1.0, "on_demand": 0.0, "vacant": 0.0},
    }

    def pick_next_transition(current_transition: str) -> str:
        probs = transition_probs[current_transition]
        r = random.random()
        cumulative = 0.0
        for t in TRANSITIONS:
            cumulative += probs[t]
            if r <= cumulative:
                return t
        return TRANSITIONS[-1]

    current_floor = random.randint(0, floors - 1)
    current_transition = "resting"
    current_time = base_date
    resting_duration = 0

    rows = []
    for _ in range(num_steps):
        rows.append({
            "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            "elevator_id": elevator_id,
            "transition": current_transition,
            "floor": current_floor
        })

        time_increment = timedelta(minutes=random.randint(1, 40))
        next_time = current_time + time_increment

        if next_time.hour >= end_hour and next_time.minute >= end_min:
            next_time = next_time.replace(hour=start_hour, minute=start_min) + timedelta(days=1)
            resting_duration = 0

        if current_transition == "resting":
            resting_duration += time_increment.total_seconds() / 60
        else:
            resting_duration = 0

        # Fixed Logic:
        if current_transition == "resting" and resting_duration > max_resting_minutes:
            if current_floor != reset_floor:
                next_transition = "vacant"
                next_floor = reset_floor
                resting_duration = 0
            else:
                # Already at reset floor, cannot go vacant
                next_transition = pick_next_transition("resting")
                if next_transition == "resting":
                    next_floor = current_floor
                else:  # on_demand
                    possible_floors = list(range(floors))
                    possible_floors.remove(current_floor)
                    next_floor = random.choice(possible_floors)

        elif current_transition == "vacant":
            next_transition = "resting"
            next_floor = reset_floor
            resting_duration = 0

        else:
            next_transition = pick_next_transition(current_transition)
            if next_transition == "resting":
                next_floor = current_floor
            elif next_transition == "on_demand":
                possible_floors = list(range(floors))
                possible_floors.remove(current_floor)
                next_floor = random.choice(possible_floors)

        current_transition = next_transition
        current_floor = next_floor
        current_time = next_time

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_synthetic_elevator_data(num_steps=100, floors=4, reset_floor=0)
    print(df)
