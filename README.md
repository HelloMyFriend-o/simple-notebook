# Записная книжка

1. Clone the repository:
```bash
git clone https://github.com/HelloMyFriend-o/simple-notebook.git
```
2. Create and activate a virtual environment

3. Install dependencies from file ***requirements.txt***:
```bash
pip install -r requirements.txt
```
4. Rename the file from ***.env(example)*** to ***.env***

5. Generate Django SECRET_KEY (например тут: djecrety.ir) and fill in the corresponding variable in the file ***.env***

6. Create DB PostgreSQL and fill in the corresponding variables in the file ***.env***

7. Go to folder:
```bash
cd snotebook
```

8. Create application migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

9. Run the app:
```bash
python manage.py runserver
```

10. The application will be available at: http://127.0.0.1:8000/
