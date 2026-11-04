# Aktual Academy — sayt

Aktual Academy tədris mərkəzi üçün statik sayt (HTML + CSS + JS).

## Struktur
- `build.py` — **bütün səhifələri yaradır.** Header, menyu, footer, proqram məlumatları, liseylər və bloq yazıları buradadır.
- `*.html` — yaradılmış səhifələr (birbaşa redaktə etməyin, `build.py`-ı dəyişib yenidən işə salın)
- `styles.css` — dizayn (brend rəngləri: mavi `#1fb3e5`, qırmızı `#ee3347`, yaşıl `#55a746`)
- `script.js` — menyu, animasiyalar, qeydiyyat formu (WhatsApp-a göndərir)
- `assets/` — loqo və şəkillər

## Dəyişiklik etmək
```
python3 build.py
git add -A && git commit -m "..." && git push
```
`main` branch-a hər push GitHub Pages tərəfindən avtomatik deploy olunur.
