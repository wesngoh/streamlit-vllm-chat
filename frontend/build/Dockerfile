# Using python containers, especially 3.10 to standardise with triton servers
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Install python dependencies
COPY ./frontend/build/requirements.txt /app
RUN pip3 install -r requirements.txt

# Copy and run app
COPY ./frontend/src/. /app

# Expose front-end port
EXPOSE 8501

# Run app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]