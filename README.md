# Project 1: Flight Dynamics Simulator

A simple desktop flight-dynamics terminal built with Tkinter. Enter aircraft and flight-state parameters (airspeed, altitude, wing area, angle of attack, throttle, etc.) and the app computes aerodynamic quantities (air density, lift, drag, L/D, load factor, lift slope) and reports a flight condition (airborne, steady, stalling, insufficient lift).

This project is intended as an educational simulator/calculator for basic flight dynamics — not a full flight simulator.

## Features
- Interactive Tkinter UI with:
  - Pilot controls for airspeed, altitude, throttle, AoA, wing area, sweep angle
  - Aircraft type selection (civilian / military) with limits
  - Aerodynamic readouts (ρ, CL, CD, Lift, Drag, L/D, load factor, lift slope)
  - Warnings and detailed messages panel
- Built-in reference windows: aircraft benchmark specs and flight-dynamics formulas.

## Screenshot 
<img width="960" height="720" alt="Slide1" src="https://github.com/user-attachments/assets/1f2e4bdc-8fc7-43d6-9b9c-41cf7a0a7138" />
<img width="960" height="720" alt="Slide2" src="https://github.com/user-attachments/assets/77ce8789-457b-4174-b069-6a84fc7f49b2" />

(not the end of the window)
<img width="960" height="720" alt="Slide3" src="https://github.com/user-attachments/assets/230919ec-4d28-49aa-8b49-8209f2ef0232" />

(not the end of the window)

## Requirements

- Python 3.7
- tkinter (usually provided with the system Python; on Debian/Ubuntu: `sudo apt install python3-tk`)

No external pip packages are required.

## Quick start
1. Clone the repo
2. (Optional) create & activate a virtualenv
3. Run:

```bash
python flight_simulator.py
```

## Controls & Units
- Airspeed: meters per second (m/s)
- Altitude: meters (m)
- Wing area: square meters (m²)
- Weight: Newtons (N)
- Throttle %: 0–100 (entered as a percent)
- Angle of attack / Sweep: degrees (°)

## Example
Set:
- Aircraft: `civ`
- Airspeed: `50` (m/s)
- Altitude: `1000` (m)
- Wing_area: `16.2` (m²)
- Weight: `10000` (N)
- Throttle %: `70`
- Angle_of_attack: `5` (deg)

Click "RUN SIMULATION" and watch the Aerodynamic Forces and Messages panels.

## Known issues/notes
- This is an educational tool. Aerodynamic models are simplified (linear CL approximations, simple drag model).
- Controls are not validated strictly; invalid or missing inputs can produce errors.
- `tkinter` may require separate installation on some platforms.

## Packaging & CI
- Add a `requirements.txt` (or `pyproject.toml` if using Poetry) — even if minimal, mention required Python version.
- Add a GitHub Actions workflow to run unit tests and linters on push/PR.

## Contributing
1. Fork, create a branch, open a PR with a clear description of changes.
2. Include tests for non-trivial logic changes.
3. Follow style and linting rules (consider adding a pre-commit config).

## License
Choose a license (MIT recommended for small educational projects). Add a `LICENSE` file.

## Contact
If you'd like help testing or adding features, open an issue or PR in this repo.
