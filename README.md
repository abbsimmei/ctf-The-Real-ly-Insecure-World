# Real(ly Insecure) World

Cybersecurity Simon Meier

## Planering

Planeringen hittar du i PDF:en på main 🔥🔥🔥🦅🦅🦅🦅🗽🗽🗽🗽


# Hosta Hemsidan på en Raspberry PI 5

Projektet använde sig av den senaste stabila ubuntu desktop versionen. 

## Fast API

Detta ska du göra i foldern API, där skapar vi en virtual environment för att kunna köra python.

´´´
# Installera virtualenv
sudo apt update
sudo apt install python3-venv -y

# Skapa en virtual environment
python3 -m venv myenv

# Aktivera virtual environment
source myenv/bin/activate
´´´

Det borde nu stå (myenv) på din shell prompt.

´´´
# Installera fastapi

pip install --upgrade pip 
pip install "fastapi[standard]" 

´´´

Nu kan vi starta API'n.

´´´

# Installera uvicorn
pip install uvicorn

# Starta appen.
uvicorn main:app --reload --host 0.0.0.0 --port 8000

´´´




# Kör hemsidan lokalt ("outdated")

## Hemsidan
<sub>(All info under Hemsidan och FAST API rubrikerna är för att köra koden lokalt på datorn. Mer dokumentation för hur jag kommer sätta upp det på Raspberry PI kommer vid senare skede.)</sub>

Hemsidan använder sig av Nuxt och Tailwind. För att ladda ner alla dependencies kör kommandot i terminalen:

```
npm install
```

För att sedan köra hemsidan, kör kommandot i terminalen:

```
npm run dev
```

## FAST API

API:et ligger i foldern API och all kod finns i main.py. Datan som API ska ge finns i /storage och ligger I JSON dokument. 

För att ladda ner Fast API kör detta kommando i terminalen:

```
pip install "fastapi[standard]"
```

Sedan för att starta API:et kör detta kommando I terminalen:

```
fastapi dev main.py
```





