# Reddit Analysis App

## Overview

The Reddit Analysis App is a Streamlit-based application that allows users to analyze top posts from a specified subreddit. It fetches data using Reddit's API, performs sentiment analysis, calculates engagement metrics, and provides visualizations and recommendations.

### Features

- Fetch and display subreddit information.
- Analyze sentiment of top posts.
- Calculate and display engagement metrics.
- Visualize trends and distributions.
- Provide recommendations based on analysis.
- Download analyzed data as a CSV file.

## Installation

### Prerequisites

- Python 3.7 or later
- Git (if cloning from GitHub)

### Steps to Install

1. **Clone the Repository or Download Files**

   - **GitHub**: Clone the repository using:
     ```bash
     git clone <repository-url>
     cd <repository-directory>
     ```

   - **Google Drive**: Download the files from Google Drive and unzip them if necessary.

2. **Set Up a Virtual Environment**

   Create and activate a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
Install the required Python packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**
Create a .env file in the root directory with the following content:
```bash

.env
REDDIT_CLIENT_ID=<your-client-id>
REDDIT_CLIENT_SECRET=<your-client-secret>
REDDIT_USER_AGENT=<your-user-agent>
Replace <your-client-id>, <your-client-secret>, and <your-user-agent> with your actual Reddit API credentials. You can obtain these credentials by creating a Reddit app at Reddit App Preferences.
```

5. **Run the App**
Start the Streamlit app with the following command:

```bash
streamlit run app.py
```
Open a web browser and navigate to http://localhost:8501 to access the app.

6. **Usage**
- Enter Subreddit Name: Type the name of a subreddit in the text input field and press Enter to fetch and analyze data.
- View Metrics: Check the displayed subreddit information, engagement metrics, and sentiment analysis.
- Visualizations: Review charts showing score and comments over time, distribution of engagement rates, and sentiment polarity.
- Recommendations: Read suggestions based on the analysis to improve content strategy.
- Download Data: Click the "Download CSV" button to save the analyzed data as a CSV file.
