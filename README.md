# Restaurant Project

Django project for managing dishes and cooks in Restaurant

## Check it out!

## [RESTAURANT](https://restaurant-npav.onrender.com)

#### To log in into Restaurant Website you can use:
#### Username: test_user
#### Password: user1234

## Installation
1. **Clone the repository:**

    ```bash
    git clone https://github.com/Aeros72/restaurant
    cd restaurant
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser account (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

## Features
* Authentication functionality for Cook/User
* Managing dishes, cooks & dish types directly from website interface
* Powerful admin panel for advanced managing
