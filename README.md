# LCC Archive & Django Polls

A Django 5.1 project containing two applications:

1. **LCC Entries** - An archive system for Lightsaber Choreography Competition entries, tracking competitions, creators, production companies, and video submissions
2. **Polls** - A simple polling application from the Django tutorial

## Requirements

- Python 3.12+
- Django 5.1.5

## Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/djangotutorial.git
cd djangotutorial

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## Usage

- **Admin interface**: http://localhost:8000/admin/
- **LCC Archive**: http://localhost:8000/lcc_entries/
- **Polls**: http://localhost:8000/polls/

## LCC Archive Features

- Browse competitions from LCC01 through SC24
- View entries with embedded YouTube videos
- Search entries by creator
- Track entry status (Pending, Accepted, Rejected, Disqualified, Withdrawn, Live)
- Associate entries with creators and production companies

## Project Structure

```
mysite/          # Django project configuration
polls/           # Tutorial polling application
lcc_entries/     # LCC archive application
```

## License

This project is for educational purposes.
