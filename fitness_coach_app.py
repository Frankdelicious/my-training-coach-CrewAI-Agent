#!/usr/bin/env python3
"""
MIT AI Studio - CrewAI Fitness Coach System
A comprehensive AI fitness coach using CrewAI agents that represents a personalized health assistant.

This system demonstrates:
- Creating multiple specialized health and fitness agents
- Processing comprehensive health data from wearables
- Generating personalized workout and nutrition plans
- Terminal-based interaction for health data input

Author: MIT AI Studio Student
"""

import os
from datetime import datetime
from typing import Dict, Any
from crewai import Agent, Task, Crew, Process
from crewai_tools import FileWriterTool

# Import our comprehensive health data model
from health_data_model import (
    ComprehensiveHealthData, UserProfile, CardiovascularMetrics,
    ActivityMetrics, SleepMetrics, BodyComposition, RecoveryMetrics,
    EnvironmentalMetrics, WorkoutMetrics, NutritionMetrics,
    create_sample_health_data
)

def create_research_assistant_agent():
    """Create a Research Assistant agent that processes comprehensive health metrics."""
    return Agent(
        role='Research Assistant',
        goal='To analyze comprehensive health data from wearables and provide insights on fitness status, recovery, and health trends',
        backstory="""You are an expert health data analyst with deep knowledge of 
        sports science, exercise physiology, and wearable technology. You specialize in 
        interpreting complex health metrics including heart rate variability, sleep stages, 
        VO2 max, body composition, and recovery indicators. You can identify patterns in 
        health data that indicate readiness for exercise, need for recovery, or potential 
        health concerns that should be addressed before physical activity.""",
        verbose=True,
        allow_delegation=False
    )

def create_fitness_content_writer_agent():
    """Create a Content Writer agent that creates personalized workout plans."""
    return Agent(
        role='Content Writer - Fitness',
        goal='To create personalized, science-based workout plans that adapt to individual health metrics, fitness levels, and recovery status',
        backstory="""You are a certified personal trainer and exercise physiologist with 
        expertise in creating adaptive fitness programs. You understand how to adjust workout 
        intensity based on heart rate variability, sleep quality, stress levels, and recovery 
        metrics. You specialize in progressive overload, periodization, and injury prevention. 
        You can design workouts for all fitness levels and adapt them based on real-time 
        health data from wearable devices.""",
        verbose=True,
        allow_delegation=False,
        tools=[FileWriterTool()]
    )

def create_nutrition_content_writer_agent():
    """Create a Content Writer agent that provides meal recommendations."""
    return Agent(
        role='Content Writer - Nutrition',
        goal='To provide personalized nutrition recommendations that support fitness goals and optimize recovery based on activity levels and body composition',
        backstory="""You are a registered dietitian and sports nutritionist with expertise 
        in performance nutrition and body composition optimization. You understand how to 
        adjust nutritional recommendations based on training load, recovery metrics, body 
        composition goals, and metabolic health indicators. You specialize in meal timing, 
        macronutrient optimization, and hydration strategies for athletic performance.""",
        verbose=True,
        allow_delegation=False,
        tools=[FileWriterTool()]
    )

def create_health_analysis_task(agent, health_data: ComprehensiveHealthData):
    """Create a comprehensive health analysis task."""
    return Task(
        description=f"""Analyze the following comprehensive health data and provide detailed insights:

{health_data.to_summary_string()}

Your analysis should include:
1. Current fitness and health status assessment
2. Recovery status and readiness for exercise
3. Identification of strengths and areas for improvement
4. Risk factors or concerns that should be addressed
5. Recommendations for workout intensity and type based on current metrics
6. Sleep and stress impact on training readiness
7. Cardiovascular fitness assessment and trends

Focus on actionable insights that can guide personalized fitness and nutrition planning.""",
        expected_output="""A comprehensive health analysis report containing:
        - Overall health and fitness status assessment (1-10 scale)
        - Current recovery status and exercise readiness
        - Cardiovascular health evaluation
        - Sleep quality impact on performance
        - Stress and recovery recommendations
        - Suggested workout intensity levels
        - Key health metrics trends and concerns
        - Actionable recommendations for improvement""",
        agent=agent
    )

def create_workout_planning_task(agent, health_analysis_task):
    """Create a personalized workout planning task."""
    return Task(
        description="""You are a Content Writer specializing in fitness plans. Based on the comprehensive health analysis provided by the Research Assistant, create a personalized workout plan.

IMPORTANT: Review the health analysis output from the previous task and use those specific findings and recommendations to create your workout plan.

Create a comprehensive workout plan that includes:
1. Weekly workout schedule (7 days) with specific exercises
2. Intensity recommendations based on heart rate zones from the analysis
3. Progressive difficulty adjustments
4. Recovery and rest day recommendations based on the user's recovery metrics
5. Specific exercises targeting weaknesses identified in the analysis
6. Warm-up and cool-down routines
7. Injury prevention strategies
8. Performance tracking metrics to monitor

The plan should directly address the findings from the health analysis and be aligned with the user's fitness level and goals.

STEPS:
1. Review the health analysis from the Research Assistant
2. Create the workout plan content
3. Use the File Writer Tool to save as 'personalized_workout_plan.md'""",
        expected_output="""A detailed workout plan saved as 'personalized_workout_plan.md' containing:
        - 7-day weekly schedule with specific workouts
        - Exercise descriptions and proper form instructions
        - Heart rate zone recommendations for each workout
        - Progressive difficulty adjustments week by week
        - Recovery strategies and rest day activities
        - Injury prevention exercises and mobility work
        - Performance tracking metrics and milestones
        - Modifications for different fitness levels""",
        agent=agent
    )

def create_nutrition_planning_task(agent, health_analysis_task):
    """Create a personalized nutrition planning task."""
    return Task(
        description="""You are a Content Writer specializing in nutrition plans. Based on the comprehensive health analysis provided by the Research Assistant, create a personalized nutrition plan.

IMPORTANT: Review the health analysis output from the previous task and use those specific findings and recommendations to create your nutrition plan.

Develop a comprehensive nutrition strategy that includes:
1. Daily caloric and macronutrient targets based on the user's body composition and goals
2. Pre and post-workout nutrition timing recommendations
3. Hydration recommendations based on activity levels
4. Meal timing for optimal recovery based on sleep and recovery metrics
5. Supplements that may benefit performance based on the analysis
6. Weekly meal planning with specific foods
7. Strategies for different training phases
8. Body composition optimization recommendations

The plan should directly address the findings from the health analysis and support the user's specific fitness goals.

STEPS:
1. Review the health analysis from the Research Assistant
2. Create the nutrition plan content
3. Use the File Writer Tool to save as 'personalized_nutrition_plan.md'""",
        expected_output="""A detailed nutrition plan saved as 'personalized_nutrition_plan.md' containing:
        - Daily caloric and macronutrient breakdown
        - Pre/post workout nutrition strategies
        - Optimal meal timing and frequency
        - Hydration guidelines and recommendations
        - Sample weekly meal plans with recipes
        - Supplement recommendations with timing
        - Strategies for different training phases
        - Progress tracking and adjustment guidelines""",
        agent=agent
    )

def get_user_health_data() -> ComprehensiveHealthData:
    """Interactive function to collect comprehensive health data from user input."""
    print("🏥 COMPREHENSIVE HEALTH DATA INPUT")
    print("=" * 50)
    print("Please provide your health metrics. Enter 'skip' for any metric you don't have.\n")
    
    # User Profile
    print("👤 USER PROFILE:")
    age = input("Age: ").strip()
    gender = input("Gender (male/female/other): ").strip().lower()
    fitness_level = input("Fitness level (beginner/intermediate/advanced): ").strip().lower()
    
    goals_input = input("Fitness goals (comma-separated, e.g., weight_loss,muscle_gain,endurance): ").strip()
    goals = [goal.strip() for goal in goals_input.split(',')] if goals_input and goals_input != 'skip' else []
    
    # Cardiovascular
    print("\n❤️  CARDIOVASCULAR METRICS:")
    resting_hr = input("Resting heart rate (bpm): ").strip()
    hrv = input("Heart rate variability (ms): ").strip()
    bp_sys = input("Blood pressure systolic (mmHg): ").strip()
    bp_dia = input("Blood pressure diastolic (mmHg): ").strip()
    vo2_max = input("VO2 Max (ml/kg/min): ").strip()
    
    # Activity
    print("\n🚶 ACTIVITY METRICS:")
    steps = input("Daily steps: ").strip()
    distance = input("Distance walked/run today (km): ").strip()
    calories = input("Calories burned: ").strip()
    active_minutes = input("Active minutes: ").strip()
    
    # Sleep
    print("\n😴 SLEEP METRICS:")
    total_sleep = input("Total sleep last night (hours): ").strip()
    deep_sleep = input("Deep sleep (hours): ").strip()
    rem_sleep = input("REM sleep (hours): ").strip()
    sleep_score = input("Sleep score (1-100): ").strip()
    
    # Body Composition
    print("\n⚖️  BODY COMPOSITION:")
    weight = input("Weight (kg): ").strip()
    height = input("Height (cm): ").strip()
    body_fat = input("Body fat percentage: ").strip()
    
    # Recovery
    print("\n🔋 RECOVERY METRICS:")
    stress_level = input("Stress level (1-100): ").strip()
    recovery_score = input("Recovery score (1-100): ").strip()
    
    # Recent Workout
    print("\n🏋️ RECENT WORKOUT:")
    workout_type = input("Last workout type (e.g., strength_training, running, yoga): ").strip()
    workout_duration = input("Workout duration (minutes): ").strip()
    workout_intensity = input("Workout intensity (low/moderate/high): ").strip()
    
    # Helper function to convert input to appropriate type
    def safe_convert(value, convert_func, default=None):
        if not value or value.lower() == 'skip':
            return default
        try:
            return convert_func(value)
        except ValueError:
            return default
    
    # Create the comprehensive health data object
    user_profile = UserProfile(
        age=safe_convert(age, int),
        gender=gender if gender and gender != 'skip' else None,
        fitness_level=fitness_level if fitness_level and fitness_level != 'skip' else None,
        fitness_goals=goals if goals else None,
        medical_conditions=[],
        current_medications=[],
        activity_preferences=[]
    )
    
    cardiovascular = CardiovascularMetrics(
        resting_heart_rate=safe_convert(resting_hr, int),
        heart_rate_variability=safe_convert(hrv, float),
        blood_pressure_systolic=safe_convert(bp_sys, int),
        blood_pressure_diastolic=safe_convert(bp_dia, int),
        vo2_max=safe_convert(vo2_max, float)
    )
    
    activity = ActivityMetrics(
        steps=safe_convert(steps, int),
        distance=safe_convert(distance, float),
        calories_burned=safe_convert(calories, int),
        active_minutes=safe_convert(active_minutes, int)
    )
    
    sleep = SleepMetrics(
        total_sleep_duration=safe_convert(total_sleep, float),
        deep_sleep_duration=safe_convert(deep_sleep, float),
        rem_sleep_duration=safe_convert(rem_sleep, float),
        sleep_score=safe_convert(sleep_score, int)
    )
    
    # Calculate BMI if height and weight provided
    bmi = None
    if weight and height:
        try:
            weight_val = float(weight)
            height_val = float(height) / 100  # convert cm to m
            bmi = weight_val / (height_val ** 2)
        except ValueError:
            pass
    
    body_composition = BodyComposition(
        weight=safe_convert(weight, float),
        height=safe_convert(height, float),
        bmi=bmi,
        body_fat_percentage=safe_convert(body_fat, float)
    )
    
    recovery = RecoveryMetrics(
        stress_level=safe_convert(stress_level, int),
        recovery_score=safe_convert(recovery_score, int)
    )
    
    environmental = EnvironmentalMetrics()
    
    recent_workouts = []
    if workout_type and workout_type != 'skip':
        recent_workouts.append(WorkoutMetrics(
            workout_type=workout_type,
            duration=safe_convert(workout_duration, int),
            intensity=workout_intensity if workout_intensity and workout_intensity != 'skip' else None
        ))
    
    nutrition = NutritionMetrics()
    
    return ComprehensiveHealthData(
        timestamp=datetime.now(),
        user_profile=user_profile,
        cardiovascular=cardiovascular,
        activity=activity,
        sleep=sleep,
        body_composition=body_composition,
        recovery=recovery,
        environmental=environmental,
        recent_workouts=recent_workouts,
        nutrition=nutrition
    )

def main():
    """Main function to run the CrewAI Fitness Coach system."""
    print("🏋️ MIT AI Studio - CrewAI Fitness Coach System")
    print("=" * 60)
    print("Your Personal AI Fitness Coach powered by CrewAI agents!")
    print("This system will analyze your health data and create personalized")
    print("workout and nutrition plans tailored specifically for you.\n")
    
    # Option to use sample data or input real data
    use_sample = input("Would you like to use sample health data for demo? (y/n): ").strip().lower()
    
    if use_sample == 'y':
        print("\n📊 Using sample health data for demonstration...")
        health_data = create_sample_health_data()
    else:
        print("\n📊 Let's collect your comprehensive health data:")
        health_data = get_user_health_data()
    
    print(f"\n📅 Processing health data from: {health_data.timestamp.strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    
    # Create agents
    print("\n🤖 Creating specialized AI agents...")
    research_assistant = create_research_assistant_agent()
    fitness_writer = create_fitness_content_writer_agent()
    nutrition_writer = create_nutrition_content_writer_agent()
    
    # Create tasks
    print("📋 Setting up AI agent tasks...")
    health_analysis_task = create_health_analysis_task(research_assistant, health_data)
    
    # Create workout planning task that uses the health analysis output
    workout_task = create_workout_planning_task(fitness_writer, health_analysis_task)
    workout_task.context = [health_analysis_task]
    
    # Create nutrition planning task that uses the health analysis output  
    nutrition_task = create_nutrition_planning_task(nutrition_writer, health_analysis_task)
    nutrition_task.context = [health_analysis_task]
    
    # Create crew
    print("👥 Assembling the AI fitness coach crew...")
    crew = Crew(
        agents=[research_assistant, fitness_writer, nutrition_writer],
        tasks=[health_analysis_task, workout_task, nutrition_task],
        process=Process.sequential,  # Tasks executed in sequence
        verbose=True
    )
    
    # Execute the crew
    print("\n🎯 Starting AI fitness coach analysis...")
    print("=" * 60)
    
    try:
        result = crew.kickoff()
        
        print("\n✅ AI Fitness Coach analysis completed!")
        print("=" * 60)
        print("📄 Final Results:")
        print(result)
        
        # Check for generated files
        files_created = []
        for filename in ['personalized_workout_plan.md', 'personalized_nutrition_plan.md']:
            if os.path.exists(filename):
                files_created.append(filename)
                with open(filename, 'r') as f:
                    content = f.read()
                    print(f"\n📝 {filename} created ({len(content)} characters)")
        
        if files_created:
            print(f"\n🎉 Success! Created {len(files_created)} personalized plan(s):")
            for file in files_created:
                print(f"   • {file}")
            print("\nYour personalized fitness and nutrition plans are ready!")
        else:
            print("\n⚠️  No plan files were created. The agents may need additional configuration.")
            
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("\n💡 Note: This system requires a valid OpenAI API key to function properly.")
        print("Please ensure your OPENAI_API_KEY environment variable is set correctly.")

if __name__ == "__main__":
    main()