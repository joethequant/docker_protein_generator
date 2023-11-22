# Include Python
from python:3.11.1-buster

# Define your working directory
WORKDIR /

# Install runpod
RUN pip install runpod

#copy models over
COPY /model_checkpoints /model_checkpoints

# Add your file
COPY app.py .

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .

#COPY progen model over
COPY /models /models

#COPY progen model over
COPY tokenizer.json .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Call your file when your container starts
CMD [ "python", "-u", "/app.py" ]