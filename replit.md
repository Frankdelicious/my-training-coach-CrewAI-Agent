# Overview

This is a CrewAI-powered fitness coaching application that leverages multiple specialized AI agents to analyze comprehensive health data and generate personalized workout and nutrition plans. The system represents an MIT AI Studio student project demonstrating advanced AI agent coordination for health and fitness applications. It processes data from wearables and health monitoring devices to create science-based, personalized fitness recommendations.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Framework
- **CrewAI Multi-Agent System**: Uses specialized AI agents for different aspects of fitness coaching
  - Research Assistant Agent: Analyzes health data and provides insights on fitness status, recovery, and health trends
  - Content Writer Agent: Creates personalized workout plans based on health metrics and fitness levels
  - Nutrition Specialist Agent: Develops customized nutrition plans and meal recommendations

## Data Processing Architecture
- **Comprehensive Health Data Model**: Structured dataclasses covering all modern wearable metrics
  - Cardiovascular metrics (heart rate, HRV, VO2 max, blood pressure)
  - Activity metrics (steps, distance, calories, active minutes)
  - Sleep metrics (duration, efficiency, sleep stages, quality scores)
  - Body composition (weight, height, BMI, body fat percentage)
  - Recovery and environmental metrics
  - Workout and nutrition tracking

## Application Interfaces
- **CLI Application**: Terminal-based interface for direct health data input and plan generation
- **Web Server**: Flask-based web interface with production-ready Gunicorn deployment
- **File Output System**: Generates personalized plans as markdown files for easy sharing and reference

## AI Agent Workflow
- **Sequential Processing**: Agents work in a coordinated manner to analyze data, generate insights, and create plans
- **Specialized Expertise**: Each agent has domain-specific knowledge in health analysis, exercise physiology, and nutrition science
- **Adaptive Recommendations**: Plans adjust based on individual health metrics, fitness levels, and recovery status

## Data Flow Design
- **Input Processing**: Handles both sample data and user-provided health metrics
- **Agent Coordination**: Uses CrewAI's Process system for structured task execution
- **Output Generation**: Creates comprehensive workout and nutrition plans with specific timing and intensity recommendations

# External Dependencies

## AI and Machine Learning
- **OpenAI API**: Powers the language models used by CrewAI agents for natural language processing and plan generation
- **CrewAI Framework**: Multi-agent AI system for coordinating specialized agents and managing complex workflows
- **CrewAI Tools**: Includes FileWriterTool for generating output files

## Web Framework
- **Flask**: Lightweight web framework for the web server interface
- **Gunicorn**: Production WSGI server for deploying the web application

## Data Processing
- **Pandas**: Data manipulation and analysis library for processing health metrics
- **Python Dataclasses**: For structured health data modeling and type safety

## Configuration Management
- **Python-dotenv**: Manages environment variables and API key configuration