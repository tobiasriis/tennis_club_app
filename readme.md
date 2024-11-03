# Tennis Club Reservation System

A Django-based application for managing tennis courts and reservations, designed for tennis clubs. Users can view court details, make hourly reservations, and see upcoming reservations in a calendar view.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Models](#models)
- [Future Improvements](#future-improvements)

## Features

- **Court Management**: Add, edit, delete, and view details of tennis courts.
- **Reservation System**: Make hourly reservations for tennis courts, ensuring no double-booking.
- **Calendar View**: View upcoming reservations in a calendar-style interface for each court.
- **Admin Dashboard**: Manage courts and reservations through the Django admin interface.

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x
- (Optional) PostgreSQL or SQLite database

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/tennis_club_reservation.git
   cd tennis_club_reservation
   ```

2. **Create Virtual Environment**:

   ```python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Requirements**:

   ```pip install -r requirements.txt

   ```

4. **Mgrate database**:

   ```$ python manage.py makemigrations
   $ python manage.py migrate
   ```

5. **Run the server**:
   ```$ python manage.py runserver
   Access application at http://127.0.0.1:8000
   ```
