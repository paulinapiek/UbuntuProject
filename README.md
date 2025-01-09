# Projekt Zaliczeniowy DevOps

## 📜 Cel projektu
Celem projektu jest stworzenie i zarządzanie prostą aplikacją webową przy użyciu narzędzi DevOps. Projekt obejmuje kluczowe aspekty:
- zarządzania kodem źródłowym,
- konteneryzacji aplikacji,
- automatyzacji procesu Continuous Integration (CI).

---

## 🖥️ Opis projektu
Stworzono aplikację wizytówkę trenera personalnego w języku Python z wykorzystaniem frameworka Flask. Aplikacja została zintegrowana z procesem CI/CD przy użyciu narzędzi takich jak:
- **GitHub Actions**,
- **Docker**.

---

## ⚙️ Etapy realizacji projektu

### 1. Przygotowanie środowiska
- Połączono się z VirtualBox Ubuntu przez SSH (localhost: 2222).
- Zainstalowano niezbędne pakiety: Python3, Flask, Docker oraz Git.

### 2. Tworzenie aplikacji
- Utworzono plik `app.py` z podstawowym kodem aplikacji Flask.
- Przygotowano plik `requirements.txt` do zarządzania zależnościami.
- Uruchomiono aplikację pod adresami:
  - `http://127.0.0.1:5000`
  - `http://10.0.2.15:5000`

### 3. Konteneryzacja
- Przygotowano plik `Dockerfile`.
- Zbudowano obraz Docker:
  docker build -t flask-app .

