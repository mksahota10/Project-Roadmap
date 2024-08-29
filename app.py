import streamlit as st
from toolhouse import Toolhouse, WebSearch, CodebaseAnalysis
from openai import OpenAI

# Initialize clients (with API keys directly in the code - NOT RECOMMENDED for production)
toolhouse = Toolhouse("c6a4a49c-e71f-404a-b101-255c8d1c502e")
openai_client = OpenAI(api_key="sk-njwd4fUtgEvAKoo0HggIa1DRbkLBlJi7mAnT6Pb7EQT3BlbkFJJQL92nfNOrFsjjwuJuluCVFCVnjmegarLC8x0zQrsA")

# Function to generate roadmap using LLM, codebase analysis, and web search
def generate_roadmap(project_details, codebase_path=None):
    # (1) Analyze codebase if provided
    code_analysis_results = "" 
    if codebase_path:
        code_analysis_results = toolhouse.use_tool(
            CodebaseAnalysis, 
            repo_url=codebase_path,  # Or local_path if applicable
            query="Summarize the main functionalities and components of the codebase"
        )

    # (2) Construct prompt incorporating codebase analysis (if available)
    prompt = f"""
    You are a project management expert. 
    Create a detailed project roadmap based on the following:

    Project Name: {project_details['name']}
    Description: {project_details['description']}
    Goals: {project_details['goals']}
    Milestones: {project_details['milestones']}
    Timelines: {project_details['timelines']}
    Resources: {project_details['resources']}
    Constraints/Risks: {project_details['constraints']}

    {f"Codebase Analysis: {code_analysis_results}" if code_analysis_results else ""} 

    Include:
    * Task breakdown for each milestone
    * Dependencies between tasks
    * Estimated durations for each task
    * Resource allocation suggestions
    * Risk identification & mitigation strategies

    Format the output clearly and concisely, potentially using markdown for better readability.
    """

    # (3) Optional: Use Web Search Tool to gather additional context (if needed)
    if not codebase_path and any(detail == "" for detail in project_details.values()):
        search_query = f"project roadmap for {project_details['name']} or similar projects"
        search_results = toolhouse.use_tool(WebSearch, query=search_query)
        prompt += f"\n\nWeb Search Results (for reference):\n{search_results}"

    # (4) Call OpenAI
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Streamlit App
def main():
    st.title("AI-Powered Project Roadmap Generator")

    # User input form 
    project_details = {
        'name': st.text_input("Project Name"),
        'description': st.text_area("Project Description"),
        'goals': st.text_area("Project Goals"),
        'milestones': st.text_area("Key Milestones (one per line)"),
        'timelines': st.text_area("Estimated Timelines for Milestones (one per line)"),
        'resources': st.text_area("Available Resources"),
        'constraints': st.text_area("Constraints/Potential Risks")
    }

    # Additional input for codebase path (optional)
    codebase_path = st.text_input("Codebase Path (Optional, for GitHub repos)")

    # Generate button
    if st.button("Generate Roadmap"):
        if all(project_details.values()): 
            with st.spinner("Generating roadmap..."):
                # Generate roadmap using LLM, codebase analysis, and web search (if applicable)
                roadmap = generate_roadmap(project_details, codebase_path)

                st.success("Roadmap Generated!")
                st.markdown(roadmap)  # Render the roadmap using markdown

        else:
            st.warning("Please fill in all the details.")

# Run the Streamlit app
if __name__ == "__main__":
    main()