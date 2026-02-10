
# Google Cloud Next Gen 2026 Conference Site

A simple, responsive informational website for a 1-day technical conference. Built with Flask.

## Features
- **Schedule View**: View the full day's agenda including speaker sessions and breaks.
- **Search & Filter**: Real-time filtering by category, speaker name, or talk title.
- **Responsive Design**: Works on desktop and mobile.
- **Data Driven**: Easy to update `data.py` to change content.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Flask

### Installation

1.  **Clone the repository** (or navigate to the project directory):
    ```bash
    cd <project_directory>
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install flask
    ```

4.  **Run the Application**:
    ```bash
    python app.py
    ```

5.  **View locally**:
    Open your browser to `http://127.0.0.1:5000`

## Project Structure
- `app.py`: Main Flask server logic.
- `data.py`: Dummy data for speakers and schedule.
- `templates/index.html`: Main frontend HTML.
- `static/`: Contains `style.css` and `script.js`.

## Customization
To update the schedule, edit the `SCHEDULE` and `SPEAKERS` dictionaries in `data.py`. 
To change the event name or location, update `EVENT_INFO` in `data.py`.
