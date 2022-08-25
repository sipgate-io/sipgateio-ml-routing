# sipgateio-ml-routing
## Vorbereitung
1. Neue virtuelle Umgebung anlegen: `python3 -m venv .env`
2. Virtuelle Umgebung aktivieren: `source .env/bin/activate`
3. Abhängigkeiten installieren: `pip install -r requirements.txt`
4. Virtuelle Umgebung deaktivieren: `deactivate`

## Daten untersuchen
### `csv_most_calls.py`
Dieses Skript liest die exportierte CSV ein und produziert eine Statistik über die Häufigkeit von Anrufen pro Kunde.

Zum Ausführen: `python3 csv_most_calls.py <pfad zu der CSV>`
