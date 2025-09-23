import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


def plot_elevator_at(excel_path, sheet="Raw Data"):
    df = pd.read_excel(excel_path, sheet_name=sheet)
    time_col = "Time (s)"
    accel_col = "Linear Acceleration z (m/s^2)"

    intervals = {
        "Up 9 floors": (5.4, 29.4),
        "Down 9 floors": (39.6, 63.5),
        "Up 1 floor": (73.7, 81),
        "Down 1 floor": (90, 97.7),
    }

    out_dir = Path("at_plots")
    out_dir.mkdir(parents=True, exist_ok=True)

    for movement, (t_min, t_max) in intervals.items():
        seg = df[(df[time_col] >= t_min) & (df[time_col] <= t_max)].copy()
        seg["t_norm"] = seg[time_col] - t_min

        plt.figure(figsize=(8, 4))
        plt.plot(seg["t_norm"], seg[accel_col], label=movement)
        plt.xlabel("Time since segment start [s]")
        plt.ylabel("Acceleration [m/s²]")
        plt.title(f"Acceleration vs Time: {movement}")
        # Set grid with 1-second spacing
        plt.grid(True, which="both")
        plt.xticks(np.arange(0, seg["t_norm"].max() + 1, 1))
        plt.legend()
        save_path = out_dir / f"{movement.replace(' ', '_').lower()}_a_t.png"
        plt.savefig(save_path, bbox_inches="tight", dpi=150)
        plt.show()

if __name__ == "__main__":
    plot_elevator_at("lift_gut.xlsx")