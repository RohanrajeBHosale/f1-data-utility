# F1 Data Collection Utility 🏎️

https://imgur.com/a/ErNZRTu

## 1. Overview

The F1 Data Collection Utility is a user-friendly web application designed to automate the process of downloading and storing Formula 1 race weekend data. Built with Python, this tool leverages the power of the **FastF1** library for data access and **Streamlit** for a clean, interactive user interface.

The primary goal of this project is to eliminate the tedious, manual steps involved in data collection. Instead of writing one-off scripts or dealing with complex APIs, users can simply input a year and a Grand Prix, click a button, and have all the key session data (Lap Times, Weather) systematically saved to their local machine in an efficient, analysis-ready format.

This tool serves as the perfect starting point for any F1 data analysis, data science, or visualization project.

---

## 2. Key Features

-   **Interactive Web UI:** A simple and intuitive interface built with Streamlit. No command-line interaction needed.
-   **Automated Session Downloads:** Fetches data for all standard sessions of a Grand Prix weekend (Practice 1-3, Qualifying, and Race).
-   **Structured Data Storage:** Automatically creates an organized folder structure for the saved data: `f1_data_storage/year/grand_prix_name/`.
-   **Efficient File Format:** Saves data as **Parquet files (`.parquet`)**, which are significantly smaller and faster to read than traditional CSV files, making them ideal for data analysis workloads.
-   **Robust Error Handling:** Gracefully handles cases where a session might not exist (e.g., a non-sprint weekend) and continues operation without crashing.
-   **Separation of Concerns:** A clean project structure that separates the backend data collection logic from the frontend user interface.

---

## 3. How to Use

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2.  **(Recommended) Create a virtual environment:**
    ```bash
    # For Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Once the installation is complete, launch the Streamlit application with the following command:

```bash
streamlit run app.py
