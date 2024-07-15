# Contributing guide

## How to contribute

1. Fork the repository
2. Clone the repository
3. Create a new branch
4. Make your changes
5. Push your changes
6. Create a pull request
7. Wait for the maintainers to review your pull request
8. Make changes if necessary
9. Pull request is merged

## Development

For simplicity, we only support development via VSCode devcontainers. To get started, open the repository in VSCode and click on the "Reopen in Container" button.

### Create the database

To create the database, run the following command:

```bash
python manage.py migrate
```

### Create an admin user

To create an admin user, run the following command:

```bash
python manage.py createsuperuser
```

### Run the development server

To run the development server, open the debug tab in VSCode and click on the "Run" button next to "Django/Wagtail".
