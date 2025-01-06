# Wybierz oficjalny obraz bazowy z Pythona
FROM python:3.9-slim

# Ustaw katalog roboczy w kontenerze na /app
WORKDIR /app

# Skopiuj pliki aplikacji do katalogu roboczego w kontenerze
COPY . /app

# Zainstaluj wymagane biblioteki z pliku requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Wskazanie portu, na którym aplikacja będzie nasłuchiwać
EXPOSE 5000

# Uruchom aplikację za pomocą Pythona
CMD ["python3", "app.py"]
