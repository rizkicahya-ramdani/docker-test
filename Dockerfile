# Gunakan base image Python
FROM python:3.11-slim

# Buat workdir
WORKDIR /app

# Salin semua file
COPY . .

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Expose port untuk Flask
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
