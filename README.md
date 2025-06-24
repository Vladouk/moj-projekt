# Mój Projekt

## 🧾 Opis projektu
Ten projekt to pełna aplikacja demonstracyjna łącząca HTML, Pythona, testy jednostkowe, Docker oraz CI/CD z deploymentem do Railway.

---

## 📦 Struktura projektu

```
moj-projekt/
├── index.html                # Strona startowa (Lab 1)
├── lab1-py/                  # Logika aplikacji w Pythonie (Lab 2)
│   ├── main.py
│   ├── requirements.txt
│   └── tests/
│       └── test_main.py
├── Dockerfile                # Obraz Dockera (Lab 3)
└── .github/workflows/ci-cd.yaml  # CI/CD workflow (Lab 3)
```

---

## 🛠 Tech Stack
- HTML
- Python
- Docker
- GitHub Actions (CI/CD)
- Railway (Deployment)

---

## 🚀 Deployment Workflow

### CI: Continuous Integration
- ✅ Automatyczne testy przy każdym `push` / `pull_request`
- ✅ Budowanie aplikacji
- ✅ Sprawdzanie jakości kodu (`flake8`, `pytest`)
- ✅ Budowanie obrazu Docker

### CD: Continuous Deployment
- ✅ Automatyczne wdrażanie na główny branch `main`
- ✅ Deployment na Railway
- ✅ Health check po wdrożeniu
- ✅ Rollback w przypadku błędu

---

## 🔐 Sekrety CI/CD

### GitHub Secrets
- `RAILWAY_TOKEN`: token do autoryzacji deploymentu
- Inne zmienne środowiskowe:
  - `NODE_ENV=production`
  - `PORT=3000`

---

## 🧪 Testowanie

W katalogu `lab1-py/`:

```bash
pip install -r requirements.txt
pytest tests/
```

---

## 🐳 Docker

### Budowanie i uruchamianie lokalnie:

```bash
docker build -t my-python-app .
docker run -p 5000:5000 my-python-app
```

---

## 🌍 Production URL

[https://moj-projekt-production-e111.up.railway.app](https://moj-projekt-production-e111.up.railway.app)

---

## ⚙️ Railway Config

- Deployment przez Dockerfile
- Automatyczny build i start
- 1 instancja w EU West (Amsterdam)

---

## 📘 Dokumentacja konfliktu

Podczas próby połączenia `feature/header-design-a` i `feature/header-design-b` w `main`, powstał konflikt:

```python
# main.py
print("=== HEADER A + B ===")
```

Rozwiązanie: ręczne połączenie wersji. Zatwierdzono jako:

```bash
git commit -m "fix: resolved conflict between header A and B"
```

---

## 📌 Semantic Versioning

- `v1.0.0` – pierwsze wydanie z pełnym CI/CD
- `v1.1.0` – dodano Docker + Railway
- `v1.1.1` – poprawki testów i README

---

## 📄 Licencja

MIT – możesz używać i modyfikować swobodnie.