# CrewAI Fitness Coach System

## Overview
AI-powered fitness coaching application built using CrewAI, representing an MIT AI Studio student. The system uses multiple specialized AI agents to analyze health data and generate personalized fitness and nutrition plans.

## Setup Instructions

### Prerequisites
- Python 3.11 or higher
- OpenAI API key

### Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```
   
   Or create a `.env` file:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## Usage Instructions

### Running the CLI Application
```bash
python fitness_coach_app.py
```

The application will:
1. Prompt you to use sample data or input your own health metrics
2. Process health data through specialized AI agents
3. Generate personalized workout and nutrition plans
4. Save plans as markdown files

### Running the Web Server
For web-based access:
```bash
python web_server.py
```

Or with production server:
```bash
gunicorn web_server:app --bind 0.0.0.0:5000 --workers 2 --worker-class gthread
```

### Available Endpoints
- `GET /` - Home page with API documentation
- `GET /health` - Health check endpoint
- `POST /demo` - Generate demo plans with sample data
- `POST /generate-plans` - Generate custom plans
- `GET /plans` - Retrieve generated plans

## Project Structure
- `fitness_coach_app.py` - Main CrewAI application with agents and tasks
- `health_data_model.py` - Comprehensive health data models
- `web_server.py` - Flask web server for deployment
- `personalized_workout_plan.md` - Generated workout plan output
- `personalized_nutrition_plan.md` - Generated nutrition plan output

## Agents and Tasks

### Agents
1. **Research Assistant** - Analyzes health data and provides insights
2. **Fitness Content Writer** - Creates personalized workout plans
3. **Nutrition Content Writer** - Generates customized nutrition plans

### Tasks
1. **Health Analysis** - Processes comprehensive health metrics
2. **Workout Planning** - Creates exercise programs based on health data
3. **Nutrition Planning** - Develops meal plans aligned with fitness goals

## Terminal Interaction
The system provides interactive terminal prompts for:
- Choosing between sample or custom health data
- Inputting personal health metrics
- Viewing real-time agent processing
- Accessing generated fitness and nutrition plans