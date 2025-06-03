# GPU Compare

## Instalace závislostí

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install django
```

## Migrace databáze

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Vytvoření administrátora

```powershell
python manage.py createsuperuser
```

## Spuštění serveru

```powershell
python manage.py runserver
```

## Přístup
- Hlavní stránka: http://127.0.0.1:8000/
- Admin rozhraní: http://127.0.0.1:8000/admin/

## Popis
Tato aplikace umožňuje porovnávat grafické karty a upscaling technologie (DLSS, FSR, XeSS). Můžete filtrovat karty podle výrobce a podporovaných technologií, zobrazit detailní informace a spravovat data v administraci.
