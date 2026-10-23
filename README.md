# 📚 Online Course and Learning Platform Analysis

An interactive data-analysis project that explores online course enrolment, ratings, categories, pricing, difficulty levels, and completion rates.

## Project Overview
This project uses Python, Pandas, Matplotlib, and Streamlit to turn course records into summary metrics and visualizations. Users can filter by platform, category, difficulty, and minimum rating.

## Features
- KPI cards for course count, total enrolments, average rating, and completion rate
- Top courses by enrolment
- Average ratings by category
- Completion rates by difficulty
- Price-versus-rating scatter plot
- Interactive filters and downloadable filtered data
- Responsive Streamlit dashboard layout

## Dataset
`data/online_courses.csv` contains 200 **synthetic sample records** prepared for demonstration and academic use. These are not official statistics or records from Coursera, Udemy, edX, LinkedIn Learning, or Skillshare. Replace the sample with a verified public dataset if real-world conclusions are required.

## Tech Stack
- Python
- Pandas
- Matplotlib
- Streamlit

## Run Locally
1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch the dashboard:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL shown in the terminal (usually `http://localhost:8501`).

## Upload to GitHub
1. Sign in to GitHub and create a new public repository named `online-course-learning-platform-analysis`.
2. Upload all files and folders from this project (or use Git).
3. Ensure `README.md`, `app.py`, `requirements.txt`, and `data/online_courses.csv` are included.
4. Add a repository description such as: `Interactive analysis of online course enrolment, ratings, pricing and completion patterns using Python and Streamlit.`

## Suggested Repository Topics
`data-analysis`, `python`, `streamlit`, `education`, `visualization`, `pandas`

## Limitations
The dataset is synthetic and intended for demonstrating the analysis workflow. It should not be treated as evidence of actual platform popularity or learner behaviour.
