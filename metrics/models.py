from django.db import models
from django.contrib.auth.models import User

# The below lists hold the machines and equipment
METRIC_TYPES = (
    ('personal_record', 'Personal Record'),
    ('bench_press', 'Bench Press'),
    ('squat', 'Squat'),
    #Below is new
    
    # Standing Calf Raise machine
    ('standing_calf_raises', 'Standing Calf Raises'),
    ('single_leg_standing_calf_raises', 'Single-Leg Standing Calf Raises'),
    # Seated calf raise machine
    ('seated_calf_raises', 'Seated Calf Raises'),
    # Hip abduction machine
    ('hip_abduction', 'Hip Abduction'),
    ('side_leg_raises', 'Side Leg Raises'),
    # Hip adduction machine
    ('hip_adduction', 'Hip Adduction'),
    ('inner_thigh_squeezes', 'Inner Thigh Squeezes'),
    # Lying hamstring curl machine
    ('lying_hamstring_curls', 'Lying Hamstring Curls'),
    # Leg extension machine
    ('leg_extensions', 'Leg Extensions'),
    # Hip thrust machine
    ('hip_thrusts', 'Hip Thrusts'),
    # Leg press
    ('leg_press', 'Leg Press'),
    ('single_leg_press', 'Single-Leg Press'),
    # Squat rack
    ('back_squats', 'Back Squats'),
    ('front_squats', 'Front Squats'),
    ('overhead_squats', 'Overhead Squats'),
    # Deadlift platform
    ('conventional_deadlifts', 'Conventional Deadlifts'),
    ('sumo_deadlifts', 'Sumo Deadlifts'),
    # Adjustable benches
    ('bench_press', 'Bench Press'),
    ('incline_bench_press', 'Incline Bench Press'),
    ('decline_bench_press', 'Decline Bench Press'),
    ('dumbbell_bench_press', 'Dumbbell Bench Press'),
    ('dumbbell_flyes', 'Dumbbell Flyes'),
    # Dumbbells
    ('dumbbell_lunges', 'Dumbbell Lunges'),
    ('dumbbell_rows', 'Dumbbell Rows'),
    ('dumbbell_shoulder_press', 'Dumbbell Shoulder Press'),
    ('dumbbell_bicep_curls', 'Dumbbell Bicep Curls'),
    ('dumbbell_tricep_extensions', 'Dumbbell Tricep Extensions'),
    # Barbells
    ('barbell_rows', 'Barbell Rows'),
    ('barbell_shoulder_press', 'Barbell Shoulder Press'),
    ('barbell_bicep_curls', 'Barbell Bicep Curls'),
    ('skull_crushers', 'Skull Crushers'),
    # Bamboo bar
    ('bamboo_bar_squats', 'Bamboo Bar Squats'),
    ('bamboo_bar_press', 'Bamboo Bar Press'),
    # Deadlift bar
    ('deficit_deadlifts', 'Deficit Deadlifts'),
    ('romanian_deadlifts', 'Romanian Deadlifts'),
    # Safety squat bar
    ('safety_squat_bar_squats', 'Safety Squat Bar Squats'),
    # Easy bars
    ('easy_bar_bicep_curls', 'Easy Bar Bicep Curls'),
    ('easy_bar_skull_crushers', 'Easy Bar Skull Crushers'),
    # Smith machine
    ('smith_machine_squats', 'Smith Machine Squats'),
    ('smith_machine_lunges', 'Smith Machine Lunges'),
    ('smith_machine_bench_press', 'Smith Machine Bench Press'),
    ('smith_machine_shoulder_press', 'Smith Machine Shoulder Press'),
    # Stair master
    ('stair_climbing', 'Stair Climbing'),
    # Treadmill
    ('treadmill_running', 'Treadmill Running'),
    ('treadmill_sprints', 'Treadmill Sprints'),
    # Preacher curl machine
    ('preacher_curls', 'Preacher Curls'),
    # Pull-up stations
    ('pull_ups', 'Pull-ups'),
    ('chin_ups', 'Chin-ups'),
    ('hanging_leg_raises', 'Hanging Leg Raises'),
    # Boxes
    ('box_jumps', 'Box Jumps'),
    ('step_ups', 'Step-ups'),
    # Kettlebells
    ('kettlebell_swings', 'Kettlebell Swings'),
    ('kettlebell_goblet_squats', 'Kettlebell Goblet Squats'),
    # Yoga balls
    ('stability_ball_crunches', 'Stability Ball Crunches'),
    ('plank_on_stability_ball', 'Plank on Stability Ball'),
    # Row machine
    ('rowing_machine_rows', 'Rowing Machine Rows'),
    # Cable row machine
    ('cable_rows', 'Cable Rows'),
    # Pull down machine
    ('lat_pulldowns', 'Lat Pulldowns'),
    ('tricep_pushdowns', 'Tricep Pushdowns'),
    # Adjustable rope machine
    ('tricep_pushdowns', 'Tricep Pushdowns'),
    ('bicep_curls', 'Bicep Curls'),
    ('face_pulls', 'Face Pulls'),
    # Incline Hyperextension machine
    ('incline_hyperextensions', 'Incline Hyperextensions'),
    # Flat hyperextension machine
    ('flat_hyperextensions', 'Flat Hyperextensions'),
    # Reverse hyperextension machine
    ('reverse_hyperextensions', 'Reverse Hyperextensions'),
    # Row machine
    ('machine_rows', 'Machine Rows'),
    # Dip station
    ('dips', 'Dips'),
    # Roman chair
    ('roman_chair_leg_raises', 'Roman Chair Leg Raises'),
    ('roman_chair_back_extensions', 'Roman Chair Back Extensions'),
    # Stationary exercise bicycle
    ('stationary_bike_cardio', 'Stationary Bike Cardio'),
    ('seated_sprints', 'Seated Sprints'),
    # Shoulder press station
    ('machine_shoulder_press', 'Machine Shoulder Press'),
    ('arnold_press', 'Arnold Press'),
    # Bench press station
    ('machine_bench_press', 'Machine Bench Press'),
    # Incline bench press station
    ('machine_incline_press', 'Machine Incline Press'),
    # Pec fly machine
    ('pec_flyes', 'Pec Flyes'),
    # Hammer strength bench press
    ('hammer_strength_bench_press', 'Hammer Strength Bench Press'),
    # Hammer strength incline press
    ('hammer_strength_incline_press', 'Hammer Strength Incline Press'),
    # Hammer strength decline press
    ('hammer_strength_decline_press', 'Hammer Strength Decline Press'),
    # Hammer strength shoulder press
    ('hammer_strength_shoulder_press', 'Hammer Strength Shoulder Press'),
    # Hammer strength row
    ('hammer_strength_rows', 'Hammer Strength Rows'),
    # Hammer strength pull down
    ('hammer_strength_lat_pulldowns', 'Hammer Strength Lat Pulldowns'),
    # Abdominal Crunch Machine
    ('ab_crunch_machine', 'Ab Crunch Machine'),
    # Chest press machine
    ('machine_chest_press', 'Machine Chest Press'),
    # Resistance Bands
    ('resistance_band_pull_aparts', 'Resistance Band Pull-aparts'),
    ('banded_squats', 'Banded Squats'),
    ('band_pull_throughs', 'Band Pull-throughs'),
    ('banded_lateral_raises', 'Banded Lateral Raises'),
    ('band_face_pulls', 'Band Face Pulls'),

    #Below are machines
    ('standing_calf_raise_machine', 'Standing Calf Raise Machine'),
    ('seated_calf_raise_machine', 'Seated Calf Raise Machine'),
    ('hip_abduction_machine', 'Hip Abduction Machine'),
    ('hip_adduction_machine', 'Hip Adduction Machine'),
    ('lying_hamstring_curl_machine', 'Lying Hamstring Curl Machine'),
    ('leg_extension_machine', 'Leg Extension Machine'),
    ('hip_thrust_machine', 'Hip Thrust Machine'),
    ('leg_press', 'Leg Press'),
    ('squat_rack', 'Squat Rack'),
    ('deadlift_platform', 'Deadlift Platform'),
    ('adjustable_benches', 'Adjustable Benches'),
    ('dumbbells', 'Dumbbells'),
    ('barbells', 'Barbells'),
    ('bamboo_bar', 'Bamboo Bar'),
    ('deadlift_bar', 'Deadlift Bar'),
    ('safety_squat_bar', 'Safety Squat Bar'),
    ('easy_bars', 'Easy Bars'),
    ('smith_machine', 'Smith Machine'),
    ('stair_master', 'Stair Master'),
    ('treadmill', 'Treadmill'),
    ('preacher_curl_machine', 'Preacher Curl Machine'),
    ('pull-up_stations', 'Pull-Up Stations'),
    ('boxes', 'Boxes'),
    ('kettlebells', 'Kettlebells'),
    ('yoga_balls', 'Yoga Balls'),
    ('row_machine', 'Row Machine'),
    ('cable_row_machine', 'Cable Row Machine'),
    ('pull_down_machine', 'Pull Down Machine'),
    ('adjustable_rope_machine', 'Adjustable Rope Machine (Tricep Pushdowns/Bicep Curls/Face Pulls/Etc)'),
    ('incline_hyperextension_machine', 'Incline Hyperextension Machine'),
    ('flat_hyperextension_machine', 'Flat Hyperextension Machine'),
    ('reverse_hyperextension_machine', 'Reverse Hyperextension Machine'),
    ('dip_station', 'Dip Station'),
    ('roman_chair', 'Roman Chair'),
    ('stationary_exercise_bicycle', 'Stationary Exercise Bicycle'),
    ('shoulder_press_station', 'Shoulder Press Station'),
    ('bench_press_station', 'Bench Press Station'),
    ('incline_bench_press_station', 'Incline Bench Press Station'),
    ('pec_fly_machine', 'Pec Fly Machine'),
    ('hammer_strength_bench_press', 'Hammer Strength Bench Press'),
    ('hammer_strength_incline_press', 'Hammer Strength Incline Press'),
    ('hammer_strength_decline_press', 'Hammer Strength Decline Press'),
    ('hammer_strength_shoulder_press', 'Hammer Strength Shoulder Press'),
    ('hammer_strength_row', 'Hammer Strength Row'),
    ('hammer_strength_pull_down', 'Hammer Strength Pull Down'),
    ('abdominal_crunch_machine', 'Abdominal Crunch Machine'),
    ('chest_press_machine', 'Chest Press Machine'),
    ('resistance_bands', 'Resistance Bands'),
)

MACHINES = [
    'Abdominal Crunch Machine', 'Adjustable Rope Machine', 'Bench Press Station',
    'Cable Row Machine', 'Chest Press Machine', 'Deadlift Platform', 'Dip Station',
    'Flat Hyperextension Machine', 'Hammer Strength Bench Press', 'Hammer Strength Decline Press',
    'Hammer Strength Incline Press', 'Hammer Strength Pull Down', 'Hammer Strength Row',
    'Hammer Strength Shoulder Press', 'Hip Abduction Machine', 'Hip Adduction Machine',
    'Hip Thrust Machine', 'Incline Bench Press Station', 'Incline Hyperextension Machine',
    'Leg Extension Machine', 'Leg Press', 'Lying Hamstring Curl Machine', 'Pec Fly Machine',
    'Preacher Curl Machine', 'Pull Down Machine', 'Pull-Up Stations', 'Reverse Hyperextension Machine',
    'Roman Chair', 'Row Machine', 'Seated Calf Raise Machine', 'Shoulder Press Station',
    'Squat Rack', 'Stair Master', 'Standing Calf Raise Machine', 'Stationary Exercise Bicycle',
    'Treadmill',
]


EQUIPMENT = [
    'Adjustable Benches', 'Barbells', 'Bamboo Bar', 'Boxes', 'Deadlift Bar', 'Dumbbells',
    'Easy Bars', 'Kettlebells', 'Resistance Bands', 'Safety Squat Bar', 'Yoga Balls',
]

EXERCISES = [
    ('arnold_press', 'Arnold Press'),
    ('back_squats', 'Back Squats'),
    ('bamboo_bar_press', 'Bamboo Bar Press'),
    ('bamboo_bar_squats', 'Bamboo Bar Squats'),
    ('barbell_bicep_curls', 'Barbell Bicep Curls'),
    ('barbell_rows', 'Barbell Rows'),
    ('bench_press', 'Bench Press'),
    ('bicep_curls', 'Bicep Curls'),
    ('box_jumps', 'Box Jumps'),
    ('cable_rows', 'Cable Rows'),
    ('chin_ups', 'Chin-ups'),
    ('conventional_deadlifts', 'Conventional Deadlifts'),
    ('decline_bench_press', 'Decline Bench Press'),
    ('deficit_deadlifts', 'Deficit Deadlifts'),
    ('dips', 'Dips'),
    ('dumbbell_bench_press', 'Dumbbell Bench Press'),
    ('dumbbell_bicep_curls', 'Dumbbell Bicep Curls'),
    ('dumbbell_flyes', 'Dumbbell Flyes'),
    ('dumbbell_lunges', 'Dumbbell Lunges'),
    ('dumbbell_rows', 'Dumbbell Rows'),
    ('dumbbell_shoulder_press', 'Dumbbell Shoulder Press'),
    ('easy_bar_bicep_curls', 'Easy Bar Bicep Curls'),
    ('easy_bar_skull_crushers', 'Easy Bar Skull Crushers'),
    ('face_pulls', 'Face Pulls'),
    ('front_squats', 'Front Squats'),
    ('hammer_strength_bench_press', 'Hammer Strength Bench Press'),
    ('hammer_strength_decline_press', 'Hammer Strength Decline Press'),
    ('hammer_strength_incline_press', 'Hammer Strength Incline Press'),
    ('hammer_strength_lat_pulldowns', 'Hammer Strength Lat Pulldowns'),
    ('hammer_strength_rows', 'Hammer Strength Rows'),
    ('hammer_strength_shoulder_press', 'Hammer Strength Shoulder Press'),
    ('hip_abduction', 'Hip Abduction'),
    ('hip_adduction', 'Hip Adduction'),
    ('hip_thrusts', 'Hip Thrusts'),
    ('hanging_leg_raises', 'Hanging Leg Raises'),
    ('incline_bench_press', 'Incline Bench Press'),
    ('incline_hyperextensions', 'Incline Hyperextensions'),
    ('inner_thigh_squeezes', 'Inner Thigh Squeezes'),
    ('kettlebell_goblet_squats', 'Kettlebell Goblet Squats'),
    ('kettlebell_swings', 'Kettlebell Swings'),
    ('lat_pulldowns', 'Lat Pulldowns'),
    ('leg_extensions', 'Leg Extensions'),
    ('leg_press', 'Leg Press'),
    ('lying_hamstring_curls', 'Lying Hamstring Curls'),
    ('machine_bench_press', 'Machine Bench Press'),
    ('machine_chest_press', 'Machine Chest Press'),
    ('machine_incline_press', 'Machine Incline Press'),
    ('machine_rows', 'Machine Rows'),
    ('machine_shoulder_press', 'Machine Shoulder Press'),
    ('overhead_squats', 'Overhead Squats'),
    ('pec_flyes', 'Pec Flyes'),
    ('plank_on_stability_ball', 'Plank on Stability Ball'),
    ('preacher_curls', 'Preacher Curls'),
    ('pull_ups', 'Pull-ups'),
    ('resistance_band_pull_aparts', 'Resistance Band Pull-aparts'),
    ('reverse_hyperextensions', 'Reverse Hyperextensions'),
    ('roman_chair_back_extensions', 'Roman Chair Back Extensions'),
    ('roman_chair_leg_raises', 'Roman Chair Leg Raises'),
    ('rowing_machine_rows', 'Rowing Machine Rows'),
    ('safety_squat_bar_squats', 'Safety Squat Bar Squats'),
    ('seated_calf_raises', 'Seated Calf Raises'),
    ('seated_sprints', 'Seated Sprints'),
    ('single_leg_press', 'Single-Leg Press'),
    ('single_leg_standing_calf_raises', 'Single-Leg Standing Calf Raises'),
    ('side_leg_raises', 'Side Leg Raises'),
    ('smith_machine_bench_press', 'Smith Machine Bench Press'),
    ('smith_machine_lunges', 'Smith Machine Lunges'),
    ('smith_machine_shoulder_press', 'Smith Machine Shoulder Press'),
    ('smith_machine_squats', 'Smith Machine Squats'),
    ('squat_jumps', 'Squat Jumps'),
    ('stability_ball_crunches', 'Stability Ball Crunches'),
    ('stair_climbing', 'Stair Climbing'),
    ('step_ups', 'Step-ups'),
    ('sumo_deadlifts', 'Sumo Deadlifts'),
    ('tricep_pushdowns', 'Tricep Pushdowns'),
    ('tricep_pushdowns', 'Tricep Pushdowns'),
    ('treadmill_running', 'Treadmill Running'),
    ('treadmill_sprints', 'Treadmill Sprints'),
]

# Captures performance metrics and associated them with a user and stores their details
class PerformanceMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric_type = models.CharField(choices=METRIC_TYPES, max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

# Represents the weight logs
class WeightLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weight_logs')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date_logged = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.date_logged} - {self.weight} lbs'