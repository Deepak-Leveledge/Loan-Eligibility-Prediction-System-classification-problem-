FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Copy the application code
COPY src/ src/
COPY templates/ templates/
COPY notebook/ notebook/
COPY catboost_info/ catboost_info/
COPY artifacts/ artifacts/



# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "run"]
