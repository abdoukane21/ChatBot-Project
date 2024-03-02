# ChatBot Project

This project is a simple chatbot implemented using Flask, jQuery, and a machine learning model for predicting responses.

## Project Structure

The project structure is as follows:

.
├── app.py
├── chatbot.py
├── static
│ └── styles.css
├── templates
│ └── index.html
└── README.md


- `app.py`: This is the main Flask application file containing the routes and configurations.
- `chatbot.py`: This file contains the implementation of the chatbot, including model training and response generation.
- `static`: This directory contains static assets such as CSS files.
- `templates`: This directory contains HTML templates.
- `README.md`: This file contains information about the project.

## Setup

1. Clone the repository to your local machine:

    ```
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```
    cd ChatBot
    ```

3. Create a virtual environment:

    ```
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```
    python app.py
    ```

2. Access the application in your web browser at `http://localhost:5000`.

## Additional Notes

- Make sure to update the machine learning model in `chatbot.py` according to your requirements.
- Customize the HTML and CSS files in the `templates` and `static` directories to match your desired design.

## Contributors

- Abdou Kane Diao

## License

This project is licensed under the [MIT License](LICENSE).
