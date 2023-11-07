<h1 align="center"> Project | Data Integration with Meli API </h1>

## Description

The project involves data extraction, transformation, and loading (ETL) processes, as well as security features like data encryption. It also follows software design principles like DRY and SOLID.

## Key Features

- Data extraction from Mercado Libre API.
- Data transformation and processing using Python libraries like Pandas.
- Secure storage with data encryption.
- ETL (Extract, Transform, Load) pipeline for handling large datasets.
- Abides by DRY and SOLID software design principles.

## Usage

To use the Data Integration with Meli API project, follow these steps:

1. Clone this repository to your local machine.

2. Configure the necessary credentials in the `.env` file. Make sure to provide values for `CLIENT_ID`, `CLIENT_SECRET`, `CODE`, and `REDIRECT_URI`.

3. Activate your virtual environment with `env\Scripts\activate`.

4. Run the application with `python main.py`.

5. Set up the necessary database by selecting Option 1 in the menu.

6. Follow the on-screen instructions to configure data extraction and processing.

## Configuration

Before running the application, ensure that you have installed the required dependencies by using the following command:

```bash
pip install -r requirements.txt
```
Additionally, set the environment variables in the .env file with the credentials for your Mercado Libre application.

## Technologies Used
Python
Pandas
SQLAlchemy
Fernet for data encryption

## Contribute
Contributions to this project are welcome. If you'd like to contribute, please follow these steps:

Fork the repository on GitHub.

Clone your forked repository to your local machine.

Create a branch for your changes.

Make your changes and commit them.

Push your changes to your forked repository.

Open a pull request in the main repository and provide a detailed description of your changes.

## License
This project is licensed under the MIT License. Please refer to the LICENSE.md file for more information.

## Contact
If you have questions or comments about this project, feel free to reach out:

Developer: Carlos Pérez Küper
Email: carlosperezkuper@gmail.com

## Acknowledgments
Special thanks to the open-source developer community and Mercado Libre for providing a robust API that enables this project.
