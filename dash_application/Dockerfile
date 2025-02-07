
#Using python
FROM python:3.9-slim
# Using Layered approach for the installation of requirements

WORKDIR /app
COPY requirements.txt .

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
#Copy files to your container

#Running your APP and doing some PORT Forwarding
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8050"]