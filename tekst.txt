Cel projektu:
Celem projektu jest stworzenie i zarządzanie prostą aplikacją webową przy użyciu narzędzi DevOps. Projekt obejmuje kluczowe aspekty zarządzania kodem źródłowym, konteneryzacji aplikacji oraz automatyzacji procesu Continuous Integration (CI).

Opis projektu:
Stworzono aplikację wizytówkę trenera personalnego w języku Python z wykorzystaniem frameworka Flask. Została ona zintegrowana z procesem CI/CD przy użyciu narzędzi takich jak GitHub Actions oraz Docker.

Etapy realizacji projektu:

Przygotowanie środowiska:

Połączenie z VirtualBox Ubuntu przez SSH (localhost: 2222).
Instalacja niezbędnych pakietów: Python3, Flask, Docker oraz Git.
Tworzenie aplikacji:

Utworzono plik app.py z podstawowym kodem aplikacji Flask.
Przygotowano plik requirements.txt do zarządzania zależnościami.
Uruchomiono aplikację pod adresami: 127.0.0.1:5000 oraz 10.0.2.15:5000.
Konteneryzacja:

Przygotowano plik Dockerfile.
Zbudowano obraz Docker: docker build -t flask-app ..
Zarządzanie kodem źródłowym:

Utworzono repozytorium na GitHub.
Skonfigurowano SSH do bezpiecznego połączenia.
Przygotowano .gitignore do ignorowania niepotrzebnych plików systemowych.
Wykonano kilka Pull Requestów (PR) jako część procesu wprowadzania zmian.
Automatyzacja CI/CD:

Przygotowano workflow GitHub Actions:
Automatyczne budowanie obrazu Docker.
Uruchamianie testów (placeholder echo "Test").
Publikowanie obrazu w Docker Hub.
Workflow uruchamia się na push do gałęzi main oraz przy PR.



