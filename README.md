# moj-projekt

## 🛠 Stos technologiczny
- HTML
- Docker
- Railway
- GitHub Actions (CI/CD)

## 🚀 Workflow wdrożeniowy

### CI: Integracja ciągła
- Automatyczna instalacja zależności (`npm install`)
- Uruchamianie testów (`npm test`)
- Sprawdzenie jakości kodu (`npm run lint`)
- Budowanie projektu (`npm run build`)

### CD: Ciągłe wdrażanie
- Automatyczne wdrożenie do Railway po przejściu CI
- Użycie GitHub Secrets (`RAILWAY_TOKEN`)
- Health check po wdrożeniu (komenda `curl`)

### ⚙️ Konfiguracja Railway
- Sekret: `RAILWAY_TOKEN`
- Zmienne środowiskowe:
  - `NODE_ENV=production`
  - `PORT=3000`

### 🔗 Link do produkcji
[https://moj-projekt-production-e111.up.railway.app](https://moj-projekt-production-e111.up.railway.app)
