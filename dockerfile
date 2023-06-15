# Verwende das offizielle Python-Basisimage
FROM python:3.9

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Skriptdatei in das Arbeitsverzeichnis
COPY mein_skript.py /app

# Installiere die erforderlichen Abhängigkeiten
RUN pip install selenium requests

# Installiere den Chrome Webdriver im Container
# Füge die entsprechenden Schritte hinzu, abhängig von deinem Betriebssystem und der Chrome-Version
# Beispiel für den Chrome Webdriver unter Linux:
COPY chromedriver_linux64.zip /app
RUN apt-get update && apt-get install -y unzip && unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip && mv chromedriver /usr/local/bin/chromedriver

# Führe das Skript aus, wenn der Container gestartet wird
CMD ["python", "script.py"]

