# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    trainer = {
        "name": "Jan Nowak",
        "title": "Trener Personalny",
        "description": "Pomagam ludziom osiągać ich cele zdrowotne i fitnessowe. Specjalizuję się w treningach siłowych, cardio oraz dietetyce.",
        "phone": "+48 123 456 789",
        "email": "jan.nowak@fitnesspro.com",
        "address": "ul. Fitnessowa 10, 00-001 Warszawa",
        "education": "Absolwent Akademii Wychowania Fizycznego w Warszawie, certyfikowany trener personalny.",
        "passions": "Pasja do sportu, zdrowego stylu życia, a także motywowania innych do działania.",
        "expertise": "Pomoc w redukcji masy ciała, budowaniu masy mięśniowej, poprawie wydolności oraz tworzeniu zrównoważonych planów dietetycznych.",
        "team": "Pracuję samodzielnie, aby zapewnić Ci indywidualne podejście i pełne wsparcie na każdym etapie drogi do osiągnięcia Twoich celów.",
        "pricing": "Zapewniam przystępne ceny i elastyczne pakiety treningowe dopasowane do Twoich potrzeb.",
        "krakow_services": {
            "benefits": [
                "Nauczę Cię, jak powinien wyglądać zdrowy i bezpieczny trening.",
                "Podczas treningów przekażę Ci wiedzę treningową oraz wspomogę wskazówkami dotyczącymi diety.",
                "Pomogę Ci w interpretacji wyników badań laboratoryjnych.",
                "Twoje zdrowie i samopoczucie są dla mnie priorytetem!"
            ],
            "help": [
                "Zapomnisz o bólach pleców, karku, stawów.",
                "Poprawisz postawę ciała.",
                "Zniwelujesz skutki siedzącego trybu życia.",
                "Nauczysz się poprawnej techniki ćwiczeń.",
                "Szybko zauważysz efekty."
            ]
        }
    }
    return render_template('business_card.html', trainer=trainer)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
