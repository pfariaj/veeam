# Veeam Job Search Selenium Test Suite

This Selenium test suite automates the job search functionality on the Veeam careers website. 
It uses the Selenium WebDriver for Chrome to perform actions such as accepting cookies, selecting a department, and filtering jobs based on language.

## Prerequisites

Before running the tests, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.x)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/pfariaj/veeam.git
    ```

2. Navigate to the project directory:

    ```bash
    cd veeam
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Tests

To run the Selenium test suite, execute the following command:

```bash
python veeam_job_search_test.py
