# Real(ly Insecure) World

Cybersecurity Simon Meier

## Planering

Planeringen hittar du i PDF:en på main 👽



## Hemsidan
<small>(All info under Hemsidan och FAST API rubrikerna är för att köra koden lokalt på datorn. Mer dokumentation för hur jag kommer sätta upp det på Raspberry PI kommer vid senare skede.)</small>

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





