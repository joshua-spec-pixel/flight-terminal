import math
import tkinter as tk

#----------Window-----------

#Main window
root = tk.Tk()

root.geometry("1100x800")
root.title("Project 1: Plane Terminal")

main_frame = tk.Frame(
	root,
	bg = "black",
	highlightbackground = "gray20",
	highlightthickness = 4,
	bd = 8, relief = "sunken"
	)

def labeled_entry(parent, text, var):
	row = tk.Frame(parent, bg = parent['bg'])
	row.pack(fill = "x", pady = 4)

	tk.Label(
		row,
		text = text,
		bg = parent['bg'],
		fg = 'white',
		font = ('Consolas', 10, "bold"),
		width = 18,
		anchor = 'w'
		).pack(side = 'left')

	tk.Entry(
		row,
		textvariable = var,
		width = 10,
		font = ('Consolas', 10)
		).pack(side = 'right')

def show_specs():
	spec_window = tk.Toplevel(root)
	spec_window.title('Aircraft Specifications')
	spec_window.geometry('700x500')
	spec_window.configure(bg = '#001122')

	tk.Label(
		spec_window,
		text = 'AIRCRAFT BENCHMARK SPECIFICATIONS',
		bg = '#001122',
		fg = 'cyan',
		font = ('Times New Roman', 11, 'bold')
		).pack(pady = 10)

	text_frame = tk.Frame(spec_window, bg = '#001122')
	text_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)

	scrollbar = tk.Scrollbar(text_frame)
	scrollbar.pack(side = 'right', fill = 'y')

	spec_text = tk.Text(
		text_frame,
		bg = '#000a1a',
		fg = 'lime',
		font = ('Times New Roman', 10),
		yscrollcommand = scrollbar.set,
		wrap = 'word'
		)

	spec_text.pack(expand = 'True', fill = 'both')
	scrollbar.config(command = spec_text.yview)

	specs = """
═══════════════════════════════════════════════════════════════
CESSNA 172 SKYHAWK (Civilian)
═══════════════════════════════════════════════════════════════

PERFORMANCE:

• Airspeed: 30–75 m/s
• Weight: ~10,000 N
• Thrust: ~1,000–1,200 N
• Max Throttle: 2700 RPM

AERODYNAMICS:

• Wing area: ~16 m²
• Air density (sea level): ~1.225 kg/m³
• CL: 0.2 – 1.4
• CD: 0.02 – 0.08

═══════════════════════════════════════════════════════════════
BEECHCRAFT T-6 TEXAN II (Military)
═══════════════════════════════════════════════════════════════

PERFORMANCE:

• Airspeed: 70–160 m/s
• Weight: ~30,000–40,000 N
• Thrust: ~10,000+ N
• Max Throttle: 1100 HP

AERODYNAMICS:

• Wing area: ~22 m²
• Air density (sea level): ~1.225 kg/m³
• CL: 0.3 – 1.5
• CD: 0.03 – 0.1

═══════════════════════════════════════════════════════════════
NOTES
═══════════════════════════════════════════════════════════════
The Cessna 172 Skyhawk is a single-engine, fixed-wing aircraft
used for general aviation, flight training, and recreational
flying.

The Beechcraft T-6 Texan II is a turboprop military trainer
aircraft used for basic pilot training in various air forces
worldwide.
 """

	spec_text.insert('1.0', specs)
	spec_text.config(state = 'disabled')

def show_formulas():
	formula_window = tk.Toplevel(root)
	formula_window.title('FLight Dynamics Formulas')
	formula_window.geometry('800x600')
	formula_window.configure(bg = '#001122')

	tk.Label(
		formula_window,
		text = 'FLIGHT DYNAMICS FORMULAS',
		bg = '#001122',
		fg = 'orange',
		font = ('Times New Roman', 11, 'bold')
		).pack(pady = 10)

	text_frame = tk.Frame(formula_window, bg = '#001122')
	text_frame.pack(expand = True, fill = 'both', padx = 20, pady = 10)

	scrollbar = tk.Scrollbar(text_frame)
	scrollbar.pack(side = 'right', fill = 'y')

	formula_text = tk.Text(
		text_frame,
		bg = '#000a1a',
		fg = 'lime',
		font = ('Times New Roman', 10),
		yscrollcommand = scrollbar.set,
		wrap = 'word'
		)

	formula_text.pack(expand = 'True', fill = 'both')
	scrollbar.config(command = formula_text.yview)

	formulas = """
═══════════════════════════════════════════════════════════════
AIR DENSITY (BAROMETRIC FORMULA)
═══════════════════════════════════════════════════════════════

• FOR ALTITUDES < 11,000m (Troposphere):

  ρ = ρ₀ × (1 - L·h/T₀)^(g·M/R·L)

• FOR ALTITUDES ≥ 11,000m (Stratosphere):

  ρ = ρ₀ × (1 - L·11000/T₀)^(g·M/R·L) × e^(-g·M·(h-11000)/(R·(T₀-L·11000)))

Where:
  ρ₀ = 1.225 kg/m³       (sea level air density)
  L  = 0.0065 K/m        (temperature lapse rate)
  h  = altitude (m)
  T₀ = 288.15 K          (sea level temperature)
  g  = 9.80665 m/s²      (gravitational acceleration)
  M  = 0.0289644 kg/mol  (molar mass of air)
  R  = 8.31447 J/(mol·K) (universal gas constant)

═══════════════════════════════════════════════════════════════
LIFT COEFFICIENT
═══════════════════════════════════════════════════════════════

• CL = min(CL_max, 0.1 × α)

Where:
  CL_max = maximum lift coefficient (from aircraft specs)
  α      = angle of attack (degrees)

═══════════════════════════════════════════════════════════════
LIFT COEFFICIENT
═══════════════════════════════════════════════════════════════

• CD = CD_min + 0.02 × CL²

Where:
  CD_min = minimum drag coefficient (from aircraft specs)
  CL     = lift coefficient  

═══════════════════════════════════════════════════════════════
LIFT FORCE
═══════════════════════════════════════════════════════════════ 

• L = 0.5 × ρ × V² × S × CL

Where:
  ρ  = air density (kg/m³)
  V  = airspeed (m/s)
  S  = wing area (m²)
  CL = lift coefficient

═══════════════════════════════════════════════════════════════
DRAG FORCE
═══════════════════════════════════════════════════════════════ 

• n = L / W

Where:
  L = lift force (N)
  W = aircraft weight (N)

Note: n = 1 means steady level flight
      n > 1 means climbing or turning
      n < 1 means descending

═══════════════════════════════════════════════════════════════
LIFT-TO-DRAG FORCE
═══════════════════════════════════════════════════════════════ 

• L/D = CL / CD

Higher L/D ratios indicate more efficient flight.

═══════════════════════════════════════════════════════════════
ASPECT RATIO
═══════════════════════════════════════════════════════════════ 

• AR = b² / S

Where:
  b = wingspan (m)
  S = wing area (m²)

═══════════════════════════════════════════════════════════════
LIFT SLOPE (per radian)
═══════════════════════════════════════════════════════════════ 

• CL_α = (2π × AR) / (2 + √(4 + AR² × (1 + tan²(Λ))))

Where:
  AR = aspect ratio
  Λ  = wing sweep angle (radians)

═══════════════════════════════════════════════════════════════
AVAILABLE THRUST
═══════════════════════════════════════════════════════════════ 

• T_available = T_max × (Throttle %)

Where:
  T_max    = maximum thrust (N)
  Throttle = throttle percentage (0-100%)

═══════════════════════════════════════════════════════════════
FLIGHT CONDITIONS
═══════════════════════════════════════════════════════════════ 

• AIRBORNE  				: L > W  AND  α < α_stall
• STEADY  					: |L - W| < 100 N
• STALLING  				: α ≥ α_stall (typically 18°)
• INSUFFICIENT  			: L < W  AND  α < α_stall

"""

	formula_text.insert('1.0', formulas)
	formula_text.config(state = 'disabled')


upper = tk.Frame(main_frame, bg = '#004488')
upper.grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)

upper.columnconfigure((0, 1, 2), weight = 1)
upper.rowconfigure(0, weight = 1)

pilot = tk.LabelFrame(
	upper,
	text = "PILOT CONTROLS",
	bg = '#112233',
	fg = "lime",
	font = ("Consolas", 12, "bold"),
	width = 350,
	height = 500
)
pilot.grid(row = 0, column = 0, sticky = 'nsew', padx = 5, pady = 5)

#Main frame
main_frame.pack(padx = 20, pady = 20, expand = True, fill = "both")

main_frame.rowconfigure(0, weight = 7)
main_frame.rowconfigure(1, weight = 2)
main_frame.columnconfigure(0, weight = 1)

#pilot panel configuration
pilot.rowconfigure(0, weight = 7)
pilot.rowconfigure(1, weight = 3)
pilot.columnconfigure(0, weight = 1)

#---------------------------

#left panel - PILOT CONTROLS

mil = 'military'
civ = 'civilian'	

AIRCRAFT_LIMITS = {
	'civ': {
		'airspeed':(30, 80),
		'wing_area': (16.17, 16.20),
		'altitude': (1350, 4200),
		'lift_coefficient': (0.2, 1.4),
		'drag_coefficient': (0.02, 0.08),
		'aircraft_classification': 10000,
		'wingspan': 11.00
	},

	'mil': {
		'airspeed': (70, 170),
		'wing_area': (16.28, 16.49),
		'altitude': (150, 9550),
		'lift_coefficient': (0.03, 1.5),
		'drag_coefficient': (0.03, 0.10),
		'aircraft_classification': 40000,
		'wingspan': 10.19
	}
}

live_frame = tk.LabelFrame(
	pilot,
	bg = '#001122',
	bd = 2,
	font = ("Consolas", 12, "bold"),
	relief = "ridge",
	padx = 10, 
	pady = 10
	)
live_frame.grid(row = 0, column = 0, sticky = 'nsew', padx = 6, pady = (8, 4))

static_frame = tk.Frame(
	pilot,
	bg = '#0a1a33',
	bd = 1, relief = "groove",
	padx = 10, pady = 10
	)
static_frame.grid(row = 1, column = 0, sticky = 'nsew', padx = 6, pady = (4, 8))

wing_area_var = tk.DoubleVar()
labeled_entry(static_frame, 'Wing_area(m²):', wing_area_var)

weight_var = tk.DoubleVar()
labeled_entry(static_frame, 'Weight(N):', weight_var)

airspeed_var = tk.DoubleVar()
labeled_entry(live_frame, 'Airspeed (m/s):', airspeed_var)

altitude_var = tk.DoubleVar()
labeled_entry(live_frame, 'Altitude (m):', altitude_var)

throttle_var = tk.DoubleVar()
labeled_entry(live_frame, 'Throttle %:', throttle_var)

aoa_var = tk.DoubleVar()
labeled_entry(live_frame, 'Angle_of_attack:', aoa_var)

sweep_var = tk.DoubleVar()
labeled_entry(static_frame, 'Sweep (deg):', sweep_var)

def compute_flight():
	try:
		α_stall = 18.0

		civ_throttle_max = 2700 
		civ_thrust_max = 1200 

		mil_throttle_max = 1100 
		mil_thrust_max = 10000

		terminal.delete('1.0', 	'end')
		warn_terminal.delete('1.0', 'end')

		ac = aircraft_var.get()
		limits = AIRCRAFT_LIMITS[ac]

		airspeed = airspeed_var.get()
		altitude = altitude_var.get()
		throttle = throttle_var.get() / 100.0
		aoa_deg = aoa_var.get()
		wing_area = wing_area_var.get()
		aircraft_weight = weight_var.get()
		sweep_deg = sweep_var.get()

		def warn(text):
			terminal.insert('end', f'[WARNING] {text}\n')
			terminal.see('end')

		if not (limits['airspeed'][0] <= airspeed <= limits['airspeed'][1]):
			warn("AIRSPEED OUT OF RANGE")
			return

		if not (limits['wing_area'][0] <= wing_area <= limits['wing_area'][1]):
			warn("WING AREA INVALID")
			return

		#---------formulae----------

		rho_0 = 1.225 
		L  = 0.0065
		T_0 = 288.15 
		g = 9.80665
		M = 0.0289644 
		R = 8.31447

		if altitude < 11000:  #troposphere
			rho = rho_0 * (1 - (L * altitude / T_0)) ** ((g * M) / (R * L))
		else:  #for higher altitudes
			rho = rho_0 * (1 - (L * 11000 / T_0)) ** ((g * M) / (R * L)) * math.exp(-g * M * (altitude - 11000) / (R * (T_0 - L * 11000)))

		wingspan = limits['wingspan']

		Cl_max = limits['lift_coefficient'][1]
		Cl_min = limits['drag_coefficient'][0]

		Cl = min(limits['lift_coefficient'][1], 0.1 * aoa_deg)
		Cd = limits['drag_coefficient'][0] + 0.02 * (Cl ** 2)

		aoa_rad = math.radians(aoa_deg)
		sweep_rad = math.radians(sweep_deg)

		#Lift force-----------------
		L = (0.5 * rho * airspeed ** 2 * wing_area * Cl)
		print(f'Lift force:', L, 'Newton')

		#Drag-----------------------
		D = (0.5 * rho * airspeed ** 2 * wing_area * Cd) 
		print(f'Drag:', D, 'Newton')

		#Load Factor----------------
		n = L / aircraft_weight
		print(f'Load factor (n):', n)

		#Lift-To-Drag Ratio---------	
		L2D = Cl / Cd
		print(f'L/D Ratio:', L2D)

		#Aspect Ratio and Lift Slope---------------
		AR = (wingspan ** 2) / wing_area
		CL_alpha = (2 * math.pi * AR) / (2 + math.sqrt(4 + AR ** 2 * (1 + math.tan(sweep_rad) ** 2))) #Lift Slope
		print(f'Lift slope:', CL_alpha, 'per radian')

		#Thrust---------------------
		if ac == 'civ':
			avail_thrust = civ_thrust_max * civ_throttle_max
			print(f'Available Thrust: {avail_thrust} N')
		elif ac == 'mil':
			avail_thrust = mil_thrust_max * mil_throttle_max
			print(f'Available Thrust: {avail_thrust} N')

		rho_var.set(f'{rho:.3f}')
		cl_var.set(f'{Cl:.2f}')
		cd_var.set(f'{Cd:.2f}')
		lift_var.set(f'{L:.1f}')
		load_var.set(f'{n:.2f}')
		drag_var.set(f'{D:.1f}')
		l2d_var.set(f'{L2D:.2f}')
		lift_slope_var.set(f'{CL_alpha:.2f}')
		thrust_var.set(f'{avail_thrust:.1f} N')

		term_print(f'LIFT 		: {L:.1f} N')
		term_print(f'LOAD n		: {n:.2f}')
		term_print(f'DRAG 		: {D:.1f} N')
		term_print(f'THRUST 	: {avail_thrust:.1f} N')

		if L > aircraft_weight and aoa_deg < α_stall:
			condition = 'FLIGHT\nAIRBORNE'
		elif abs(L - aircraft_weight) < 100:
			condition = 'FLIGHT\nSTEADY'
		elif aoa_deg >= α_stall:
		    condition = 'FLIGHT\nSTALLING'
		else:
			condition = 'INSUFFICIENT\nLIFT'

		condition_var.set(condition)

		term_print('========== FLIGHT STATUS ==========')
		term_print(f'AIRSPEED 	: {airspeed:.2f} m/s')
		term_print(f'ALTITUDE 	: {altitude:.1f} m')
		term_print('===================================')


	except tk.TclError:
		term_print("ERROR: Invalid input detected")
	except ValueError:
		term_print("ERROR: Please enter valid numbers	")

tk.Button(
	pilot,
	text = '╢ RUN SIMULATION',
	font = ('Consolas', 11, 'bold'),
	bg = 'black',
	fg = 'lime',
	command = compute_flight
	).grid(row = 2, column = 0, pady = 10)

info_buttons = tk.Frame(pilot, bg = '#112233')
info_buttons.grid(row = 5, column = 0, pady = 10, sticky = 'ew', padx = 10)
info_buttons.columnconfigure((0, 1), weight = 1)

tk.Button(
	info_buttons,
	text = 'AIRCRAFT SPECS',
	font = ('Consolas', 9, 'bold'),
	bg = '#003366',
	fg = 'cyan',
	command = show_specs
	).pack(side = 'left', padx = 5, expand = True, fill = 'x')

tk.Button(
	info_buttons,
	text = 'FORMULAS',
	font = ('Consolas', 9, 'bold'),
	bg = '#663300',
	fg = 'orange',
	command = show_formulas
	).pack(side = 'left', padx = 5, expand = True, fill = 'x')

#---------------------------

#center panel - AIRCRAFT STATE

state = tk.LabelFrame(
	upper,
	text = "AIRCRAFT STATE",
	bg = '#001122',
	fg = "orange",
	font = ("Consolas", 14, "bold"),
	bd = 3, relief = "ridge",
	padx = 15, pady = 15
	)
state.grid(row = 0, column = 1, sticky = 'nsew', padx = 5, pady = 5)

thrust_var = tk.StringVar(value = '---')
condition_var = tk.StringVar(value = '---')

def state_label(parent, text, var):
	row = tk.Frame(parent, bg = parent['bg'])
	row.pack(anchor = 'w', pady = 5)

	tk.Label(
		row,
		text = text,
		bg = parent['bg'],
		fg = 'white',
		font = ('Consolas', 10, 'bold'),
		width = 14,
		anchor = 'w',
		).pack(side = 'left')

	tk.Label(
		row,
		textvariable = var,
		bg = parent['bg'],
		fg = 'orange',
		font = ('Consolas', 10, 'bold'),
		width = 14,
		anchor = 'w',
		).pack(side = 'left')

state_label(state, 'THRUST:', thrust_var)
state_label(state, 'CONDITION:', condition_var)	

aircraft_var = tk.StringVar(value = 'civ')

tk.Label(
	pilot,
	text = 'Aircraft type:',
	bg = '#112233',
	fg = 'white',
	font = ('Consolas', 10, 'bold')
	).grid(row = 3, column = 0, sticky = 'w', padx = 10)

tk.OptionMenu(
	pilot,
	aircraft_var,
	'civ',
	'mil',
	).grid(row = 4, column = 0, sticky = 'w', padx = 10)

#---------------------------

#right panel - AERODYNAMIC FORCES
rho_var = tk.StringVar(value = '---')
cl_var = tk.StringVar(value = '---')
cd_var = tk.StringVar(value = '---')
lift_var = tk.StringVar(value = '---')
drag_var = tk.StringVar(value = '---')
l2d_var = tk.StringVar(value = '---')
lift_slope_var = tk.StringVar(value = '---')
load_var = tk.StringVar(value = '---')

def force_label(parent, text, var):
	row = tk.Frame(parent, bg = parent['bg'])
	row.pack(anchor = 'w', pady = 3)

	tk.Label(
		row,
		text = text,
		bg = parent['bg'],
		fg = 'white',
		font = ('Consolas', 10, 'bold'),
		width = 16,
		anchor = 'w'
		).pack(side = 'left')

	tk.Label(
		row,
		textvariable = var,
		fg = 'lime',
		bg = parent['bg'],
		font = ('Consolas', 10, 'bold')
		).pack(side = 'left')

forces = tk.LabelFrame(
	upper,
	text = "AERODYNAMIC FORCES",
	bg = '#112233',
	fg = "yellow",
	font = ("Consolas", 12, "bold"),
	bd = 3, relief = "ridge",
	padx = 15, pady = 15
	)
forces.grid(row = 0, column = 2, sticky = 'nsew', padx = 5, pady = 5)

force_label(forces, 'Air_Density:', rho_var)
force_label(forces, 'Cl:', cl_var)
force_label(forces, 'LIFT (N):', lift_var)
force_label(forces, 'Load n:', load_var)
force_label(forces, 'DRAG (N):', drag_var)
force_label(forces, 'Lift Slope:', lift_slope_var)

#---------------------------

#bottom - WARNINGS | MESSAGES
bottom = tk.Frame(main_frame, bg = '#004488')
bottom.grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = 10)

bottom.columnconfigure((0, 1), weight = 1)
bottom.rowconfigure(0, weight = 1)

warn_frame = tk.LabelFrame(
	bottom,
	text = "WARNINGS",
	bg = '#330000',
	fg = "red",
	font = ("Consolas", 13, "bold"),
	bd = 4, relief = "ridge",
	padx = 15, pady = 15
	)
warn_frame.grid(row = 0, column = 0, sticky = 'nsew', padx = 5)

warn_terminal = tk.Text(
	warn_frame,
	bg = '#330000',
	fg = "red",
	font = ("Consolas", 10),
	height = 8,
	insertbackground = 'red'
	)
warn_terminal.pack(expand = 'True', fill = 'both')

msg = tk.LabelFrame(
	bottom,
	text = "MESSAGES",
	bg = '#003300',
	fg = "lime",
	font = ("Consolas", 13, "bold"),
	bd = 4, relief = "ridge",
	padx = 15, pady = 15
	)
msg.grid(row = 0, column = 1, sticky = 'nsew', padx = 5)

terminal = tk.Text(
	msg,
	bg = '#001900',
	fg = 'lime',
	font = ('Consolas', 10),
	height = 8,
	insertbackground = 'lime'
	)
terminal.pack(expand = 'True', fill = 'both')

def term_print(text):
	terminal.insert('end', text + '\n')
	terminal.see('end')

root.mainloop()
