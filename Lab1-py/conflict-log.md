# Dokumentacja konfliktu

## Opis
Podczas próby połączenia gałęzi `feature/header-design-a` i `feature/header-design-b` w `main`
powstał konflikt w pliku `main.py`.

## Przyczyna
Obie gałęzie zawierały zmiany w tym samym miejscu kodu — linia nagłówka (`print(...)`).

## Rozwiązanie
Po ręcznym przejrzeniu zmian wybrano wersję łączoną:

```python
print("=== HEADER A + B ===")
