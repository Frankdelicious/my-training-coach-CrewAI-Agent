"""
Comprehensive Health Data Model for AI Fitness Coach
Covers all metrics that modern wearables and health apps can track
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, List
import json

@dataclass
class CardiovascularMetrics:
    """Heart rate and cardiovascular health metrics"""
    resting_heart_rate: Optional[int] = None  # bpm
    max_heart_rate: Optional[int] = None  # bpm
    heart_rate_variability: Optional[float] = None  # ms
    blood_pressure_systolic: Optional[int] = None  # mmHg
    blood_pressure_diastolic: Optional[int] = None  # mmHg
    vo2_max: Optional[float] = None  # ml/kg/min
    cardio_fitness_score: Optional[int] = None  # 1-100 scale

@dataclass
class ActivityMetrics:
    """Daily activity and movement metrics"""
    steps: Optional[int] = None
    distance: Optional[float] = None  # km
    calories_burned: Optional[int] = None
    active_minutes: Optional[int] = None
    floors_climbed: Optional[int] = None
    standing_hours: Optional[int] = None
    move_minutes: Optional[int] = None
    exercise_minutes: Optional[int] = None

@dataclass
class SleepMetrics:
    """Sleep quality and duration metrics"""
    total_sleep_duration: Optional[float] = None  # hours
    deep_sleep_duration: Optional[float] = None  # hours
    rem_sleep_duration: Optional[float] = None  # hours
    light_sleep_duration: Optional[float] = None  # hours
    sleep_efficiency: Optional[float] = None  # percentage
    time_to_fall_asleep: Optional[int] = None  # minutes
    times_awake: Optional[int] = None
    sleep_score: Optional[int] = None  # 1-100 scale

@dataclass
class BodyComposition:
    """Body measurements and composition"""
    weight: Optional[float] = None  # kg
    height: Optional[float] = None  # cm
    bmi: Optional[float] = None
    body_fat_percentage: Optional[float] = None  # percentage
    muscle_mass: Optional[float] = None  # kg
    bone_density: Optional[float] = None  # g/cm²
    water_percentage: Optional[float] = None  # percentage
    metabolic_age: Optional[int] = None  # years

@dataclass
class RecoveryMetrics:
    """Recovery and stress indicators"""
    stress_level: Optional[int] = None  # 1-100 scale
    recovery_score: Optional[int] = None  # 1-100 scale
    readiness_score: Optional[int] = None  # 1-100 scale
    training_load: Optional[int] = None  # 1-10 scale
    fatigue_level: Optional[int] = None  # 1-10 scale

@dataclass
class EnvironmentalMetrics:
    """Environmental and physiological sensors"""
    blood_oxygen_saturation: Optional[float] = None  # percentage
    skin_temperature: Optional[float] = None  # celsius
    ambient_temperature: Optional[float] = None  # celsius
    uv_exposure: Optional[int] = None  # UV index
    noise_exposure: Optional[int] = None  # decibels

@dataclass
class WorkoutMetrics:
    """Specific workout and exercise data"""
    workout_type: Optional[str] = None  # "cardio", "strength", "yoga", etc.
    duration: Optional[int] = None  # minutes
    intensity: Optional[str] = None  # "low", "moderate", "high", "peak"
    average_heart_rate: Optional[int] = None  # bpm
    max_heart_rate_reached: Optional[int] = None  # bpm
    calories_burned: Optional[int] = None
    distance: Optional[float] = None  # km
    power_output: Optional[float] = None  # watts (cycling/rowing)
    pace: Optional[str] = None  # min/km for running
    elevation_gain: Optional[float] = None  # meters

@dataclass
class NutritionMetrics:
    """Nutrition and hydration data"""
    water_intake: Optional[float] = None  # liters
    calories_consumed: Optional[int] = None
    protein_intake: Optional[float] = None  # grams
    carbs_intake: Optional[float] = None  # grams
    fat_intake: Optional[float] = None  # grams
    caffeine_intake: Optional[int] = None  # mg

@dataclass
class UserProfile:
    """User demographics and fitness goals"""
    age: Optional[int] = None
    gender: Optional[str] = None  # "male", "female", "other"
    fitness_level: Optional[str] = None  # "beginner", "intermediate", "advanced"
    fitness_goals: Optional[List[str]] = None  # ["weight_loss", "muscle_gain", "endurance", etc.]
    medical_conditions: Optional[List[str]] = None
    current_medications: Optional[List[str]] = None
    activity_preferences: Optional[List[str]] = None  # ["running", "cycling", "strength", etc.]

@dataclass
class ComprehensiveHealthData:
    """Complete health data structure containing all metrics"""
    timestamp: datetime
    user_profile: UserProfile
    cardiovascular: CardiovascularMetrics
    activity: ActivityMetrics
    sleep: SleepMetrics
    body_composition: BodyComposition
    recovery: RecoveryMetrics
    environmental: EnvironmentalMetrics
    recent_workouts: List[WorkoutMetrics]
    nutrition: NutritionMetrics
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'timestamp': self.timestamp.isoformat(),
            'user_profile': self.user_profile.__dict__,
            'cardiovascular': self.cardiovascular.__dict__,
            'activity': self.activity.__dict__,
            'sleep': self.sleep.__dict__,
            'body_composition': self.body_composition.__dict__,
            'recovery': self.recovery.__dict__,
            'environmental': self.environmental.__dict__,
            'recent_workouts': [workout.__dict__ for workout in self.recent_workouts],
            'nutrition': self.nutrition.__dict__
        }
    
    def to_summary_string(self) -> str:
        """Create a formatted summary for AI agent processing"""
        summary = f"""
=== COMPREHENSIVE HEALTH DATA SUMMARY ===
Date: {self.timestamp.strftime('%Y-%m-%d %H:%M')}

USER PROFILE:
- Age: {self.user_profile.age or 'Not provided'}
- Gender: {self.user_profile.gender or 'Not provided'}
- Fitness Level: {self.user_profile.fitness_level or 'Not provided'}
- Goals: {', '.join(self.user_profile.fitness_goals or ['Not specified'])}

CARDIOVASCULAR HEALTH:
- Resting HR: {self.cardiovascular.resting_heart_rate or 'N/A'} bpm
- HRV: {self.cardiovascular.heart_rate_variability or 'N/A'} ms
- Blood Pressure: {self.cardiovascular.blood_pressure_systolic or 'N/A'}/{self.cardiovascular.blood_pressure_diastolic or 'N/A'} mmHg
- VO2 Max: {self.cardiovascular.vo2_max or 'N/A'} ml/kg/min

ACTIVITY METRICS:
- Steps: {self.activity.steps or 'N/A'}
- Distance: {self.activity.distance or 'N/A'} km
- Calories Burned: {self.activity.calories_burned or 'N/A'}
- Active Minutes: {self.activity.active_minutes or 'N/A'}

SLEEP QUALITY:
- Total Sleep: {self.sleep.total_sleep_duration or 'N/A'} hours
- Deep Sleep: {self.sleep.deep_sleep_duration or 'N/A'} hours
- REM Sleep: {self.sleep.rem_sleep_duration or 'N/A'} hours
- Sleep Score: {self.sleep.sleep_score or 'N/A'}/100

BODY COMPOSITION:
- Weight: {self.body_composition.weight or 'N/A'} kg
- BMI: {self.body_composition.bmi or 'N/A'}
- Body Fat: {self.body_composition.body_fat_percentage or 'N/A'}%
- Muscle Mass: {self.body_composition.muscle_mass or 'N/A'} kg

RECOVERY STATUS:
- Stress Level: {self.recovery.stress_level or 'N/A'}/100
- Recovery Score: {self.recovery.recovery_score or 'N/A'}/100
- Readiness Score: {self.recovery.readiness_score or 'N/A'}/100

ENVIRONMENTAL:
- Blood Oxygen: {self.environmental.blood_oxygen_saturation or 'N/A'}%
- Skin Temperature: {self.environmental.skin_temperature or 'N/A'}°C

RECENT WORKOUTS:
"""
        for i, workout in enumerate(self.recent_workouts[-3:], 1):  # Last 3 workouts
            summary += f"- Workout {i}: {workout.workout_type or 'Unknown'} ({workout.duration or 'N/A'} min, {workout.intensity or 'N/A'} intensity)\n"
        
        summary += f"""
NUTRITION:
- Water Intake: {self.nutrition.water_intake or 'N/A'} L
- Calories Consumed: {self.nutrition.calories_consumed or 'N/A'}
- Protein: {self.nutrition.protein_intake or 'N/A'}g
"""
        return summary

def create_sample_health_data() -> ComprehensiveHealthData:
    """Create sample health data for testing"""
    return ComprehensiveHealthData(
        timestamp=datetime.now(),
        user_profile=UserProfile(
            age=28,
            gender="female",
            fitness_level="intermediate",
            fitness_goals=["weight_loss", "muscle_gain", "endurance"],
            medical_conditions=[],
            current_medications=[],
            activity_preferences=["running", "strength_training", "yoga"]
        ),
        cardiovascular=CardiovascularMetrics(
            resting_heart_rate=65,
            max_heart_rate=185,
            heart_rate_variability=45.2,
            blood_pressure_systolic=120,
            blood_pressure_diastolic=80,
            vo2_max=38.5,
            cardio_fitness_score=78
        ),
        activity=ActivityMetrics(
            steps=8500,
            distance=6.2,
            calories_burned=420,
            active_minutes=65,
            floors_climbed=12,
            standing_hours=8,
            move_minutes=240,
            exercise_minutes=45
        ),
        sleep=SleepMetrics(
            total_sleep_duration=7.5,
            deep_sleep_duration=1.8,
            rem_sleep_duration=1.2,
            light_sleep_duration=4.5,
            sleep_efficiency=85.0,
            time_to_fall_asleep=12,
            times_awake=2,
            sleep_score=82
        ),
        body_composition=BodyComposition(
            weight=65.0,
            height=168.0,
            bmi=23.0,
            body_fat_percentage=22.5,
            muscle_mass=28.2,
            bone_density=1.2,
            water_percentage=58.0,
            metabolic_age=25
        ),
        recovery=RecoveryMetrics(
            stress_level=35,
            recovery_score=75,
            readiness_score=80,
            training_load=6,
            fatigue_level=4
        ),
        environmental=EnvironmentalMetrics(
            blood_oxygen_saturation=98.5,
            skin_temperature=36.2,
            ambient_temperature=22.0,
            uv_exposure=3,
            noise_exposure=45
        ),
        recent_workouts=[
            WorkoutMetrics(
                workout_type="strength_training",
                duration=45,
                intensity="moderate",
                average_heart_rate=135,
                max_heart_rate_reached=165,
                calories_burned=280
            ),
            WorkoutMetrics(
                workout_type="running",
                duration=30,
                intensity="moderate",
                average_heart_rate=145,
                max_heart_rate_reached=170,
                calories_burned=320,
                pace="5:30"
            )
        ],
        nutrition=NutritionMetrics(
            water_intake=2.1,
            calories_consumed=1850,
            protein_intake=95.0,
            carbs_intake=210.0,
            fat_intake=65.0,
            caffeine_intake=120
        )
    )