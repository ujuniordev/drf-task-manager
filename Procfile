release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_task_manager.wsgi