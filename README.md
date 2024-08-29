# AI-Powered Project Roadmap Generator

This Streamlit application leverages the power of AI and code analysis to automatically generate detailed project roadmaps.

## How It Works

1. **Project Details:** You provide essential information about your project, including its name, description, goals, milestones, timelines, resources, and potential constraints.

2. **Codebase Analysis (Optional):** If you have an existing codebase (e.g., a GitHub repository), the app can optionally analyze it to understand the project's current state and functionalities.

3. **AI Generation:** Using OpenAI's language model, the app generates a comprehensive project roadmap, taking into account your inputs and any codebase analysis results. The roadmap includes:

    * Task breakdown for each milestone
    * Dependencies between tasks
    * Estimated task durations
    * Resource allocation suggestions
    * Risk identification and mitigation strategies

4. **Web Search (Optional):** If the provided project details are insufficient, the app can perform web searches to gather additional context about similar projects, further enhancing the roadmap generation.

## Features

* **User-friendly Streamlit Interface:** Easy-to-use web form for inputting project details.
* **AI-Powered Roadmap Generation:** Leverages advanced language models for creating detailed and insightful roadmaps.
* **Codebase Analysis:** Optionally integrates with your codebase to understand existing project structure.
* **Web Search:** Supplements project information with additional context from the web.
* **Markdown Output:** Generates roadmaps in markdown format for easy readability and sharing.

## Getting Started

1. **Install Dependencies:** 
   pip install streamlit toolhouse openai

   
 2. Set API Keys: Obtain API keys for Toolhouse and OpenAI and replace the placeholders in the code.

 3. Run the App:
    streamlit run your_app_name.py