# Project Setup Instructions

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Clone the Project

1. Clone the project repository to your desktop:

    ```bash
    git clone https://github.com/Baba14Yaga/VectorShift.git
    ```

### Backend Setup

2. Navigate to the backend directory:

    ```bash
    cd backend
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Replace the `CLIENT_ID` and `CLIENT_SECRET` in `hubspot.py` with your actual HubSpot credentials:

    Open `hubspot.py` and find the lines where `CLIENT_ID` and `CLIENT_SECRET` are defined. Replace the placeholder values with your actual HubSpot credentials.

7. Start the backend server:

    ```bash
    uvicorn main:app --reload
    ```

### Frontend Setup

8. Open a new terminal and navigate to the frontend directory:

    ```bash
    cd frontend
    ```

9. Install the required dependencies:

    ```bash
    npm i
    ```

10. Start the frontend server:

    ```bash
    npm start
    ```

The project should now be running with the backend server accessible at the specified URL (usually `http://localhost:8000` by default) and the frontend server running on its specified port (usually `http://localhost:3000` by default).
