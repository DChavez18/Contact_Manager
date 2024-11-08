# Contact Manager

A simple web application for managing contacts, built with Flask and PostgreSQL. This project allows users to add, view, and manage their contacts easily.

## Features

- **Add Contacts**: Submit new contacts with names and phone numbers.
- **View Contacts**: Retrieve and display a list of all contacts.
- **User-Friendly Interface**: Intuitive HTML/CSS interface for easy interaction.

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Analytics**: PostHog for tracking user interactions

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Flask
- psycopg2
- python-dotenv

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/contact_manager.git
   cd contact_manager
   ```
2. Create a virtual env and activate:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```
3. Install packages:
   ```bash
   pip install Flask psycopg2 python-dotenv
   ```
4. Create a .env file in the root directory with DB credentials
   ```bash
   DB_NAME=contact_manager
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   ```
### Running the Application

  ```bash
  flask run
  ```
  Access the application at http://127.0.0.1:5000/.

## Future Iterations

- **User Authentication**: Implement user login and registration to manage contacts securely.
- **Enhanced UI**: Improve the front-end design using frameworks like Bootstrap or React.
- **Search Functionality**: Allow users to search for contacts by name or phone number.
- **Mobile Responsiveness**: Ensure the application is fully responsive on mobile devices.
- **Analytics Dashboard**: Create a dashboard to visualize user interactions and contact metrics using PostHog.