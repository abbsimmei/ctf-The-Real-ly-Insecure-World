# Real(ly Insecure) World

Cybersecurity Simon Meier

## Planering

Planeringen hittar du i de två PDF:erna på main
Den första är version 1.0 och den andra är 2.0.

# Hur ska CTF:en delas med klassen vid tävlingen.

Jag kommer att hosta hemsidan som de ska hacka på en raspberry pi. Jag kommer sätta på den på tisdag innan lektionen. Men för att ni ska kunna plannera så är jag 99% på att detta är ip:adressen: http://10.22.5.91/

# Known bugs

- Images have the wrong name. This is easily fixed by changing the case of their letters.

# Hosta Hemsidan på en Raspberry PI 5

Projektet använde sig av den senaste stabila ubuntu desktop versionen. 

## Fast API

Detta ska du göra i foldern API, där skapar vi en virtual environment för att kunna köra python.


### Installera virtualenv
 > sudo apt update

 > sudo apt install python3-venv -y

### Skapa en virtual environment
 > python3 -m venv myenv

### Aktivera virtual environment
 > source myenv/bin/activate

Det borde nu stå (myenv) på din shell prompt.

### Installera fastapi

 > pip install --upgrade pip 

 > pip install "fastapi[standard]" 

Nu kan vi starta API'n.

### Installera uvicorn
 > pip install uvicorn

### Starta appen.
 > uvicorn main:app --reload --host 0.0.0.0 --port 8000

API'n körs nu på raspberry PI ens IP:8000 vilket du kan hitta med hostname -I


## Hemsidan

Hemsidan körs med hjälp av en node-server och Nginx som reverse proxy. 

### Installera Node.js

 > sudo apt update

 > sudo apt install nodejs npm

 > node -v #Kolla om versionen är över 18+

### Build Hemsidan

Innan du buildar måste du ändra ipAdressen som hemsidan använder sig för att requesta API. Så I Real_World_Nuxt/server/api/ipAdress.js bytt ut adressen till adressen på API't
Det borde vara Raspberry pi'ens ip address som du kan få med hostname -I och sen :8000

I Real_World_Nuxt kör:

 > npm install

 > npm run build

 > npm run start

En Node server borde nu ha startat. 

### Nginx reverse proxy

 > sudo apt install nginx

 > sudo systemctl start nginx

 > sudo systemctl enable nginx

I /etc/nginx/sites-available/default lägg in det här:

(Denna del renderas konstigt i github av nån anledning???)

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        proxy_pass http://localhost:3000; # Forward to Nuxt
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}


 > sudo systemctl restart nginx

Gå nu in på raspberry Pi'ens IP adress och allt borde fungera! Fråga Simon eller ChatGPT om det inte gör det...



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





