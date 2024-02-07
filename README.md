# Health Care Web Application

This is a web application built with Flask for managing health-related information and reminders. It allows users to sign up, log in, update their personal information, view their eating schedule, exercise routine, and medical reminders.

## Features

- **User Authentication**: Users can sign up for an account and log in securely.
- **Profile Management**: Users can update their personal information such as name, age, gender, contact details, and address.
- **Eating Schedule**: Displays a recommended eating schedule for a specified age group.
- **Exercise Routine**: Provides exercise routines tailored to specific age groups and genders.
- **Medical Reminders**: Displays reminders for taking prescribed medicines, including information on the remaining doses and time left for the next dose.
- **Forgot Password**: Allows users to reset their password if they forget it.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/health-care-app.git

2. cd health-care-app
  ```bash
   cd health-care-app


3. Install the dependencies:
  ``bash
   pip install -r requirements.txt

4. Run the application:
  ```bash
  python app.py

5. Access the application in your web browser at http://localhost:5000.


  ## Technologies Used

  - **Flask**: Python web framework for building the backend of the application.
  - **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) for database management.
  - **Bootstrap**: Frontend framework for designing responsive and mobile-first websites.
  - **Jinja2**: Template engine for generating HTML markup with Python in the Flask application.
  - **JavaScript**: Used for dynamic updates in the frontend, such as countdown timers and remaining doses calculation.

