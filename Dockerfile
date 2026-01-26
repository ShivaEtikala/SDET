# 1. Use an official lightweight Python image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependency list first (for better Docker caching)
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the project into the container
COPY . .

# 6. Default command: run pytest
CMD ["pytest", "-v"]
