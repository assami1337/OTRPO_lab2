FROM python:3.9-slim

RUN dpkg --add-architecture arm64 && \
    apt-get update && apt-get install -y \
    libsm6:arm64 \
    libxext6:arm64 \
    libxrender-dev:arm64 \
    libgl1-mesa-glx:arm64 \
    libglib2.0-0:arm64 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "face_detection.py"]
