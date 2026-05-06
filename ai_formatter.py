import os
import requests
from dotenv import load_dotenv

def create_ai_markdown_report(input_txt_path="nis2_report.txt", output_md_path="ai_ertekeles.md"):
    # 1. API kulcs betöltése
    load_dotenv()
    api_key = os.environ.get("MISTRAL_API_KEY")

    if not api_key:
        print("Hiba: Nem találom a MISTRAL_API_KEY környezeti változót a .env fájlban!")
        return

    # 2. Eredeti szöveges riport beolvasása
    try:
        with open(input_txt_path, "r", encoding="utf-8") as file:
            original_report = file.read()
    except FileNotFoundError:
        print(f"Hiba: A {input_txt_path} fájl nem található! Futtasd le előbb az auditort.")
        return

    # 3. Promptok előkészítése
    system_prompt = (
        "Te egy professzionális kiberbiztonsági auditor vagy. A feladatod, hogy a kapott "
        "angol nyelvű, nyers NIS2 audit riportot lefordítsd magyarra, és átfogalmazd egy "
        "vezetői összefoglalóvá Markdown (.md) formátumban.\n"
        "SZABÁLYOK:\n"
        "1. Fogalmazz szép, összefüggő, közérthető mondatokat a nyers felsorolások helyett.\n"
        "2. Tartsd meg az eredeti dokumentum struktúráját (Cégadatok, Hiányosságok, Javasolt lépések, Linkek).\n"
        "3. A 'missing' és 'necessary documentation' részeket sződd bele a szövegbe értelmes magyarázatként.\n"
        "4. Szigorúan csak azokat az információkat használd, amik a bemenetben szerepelnek! Ne találj ki új NIS2 szabályokat!"
    )

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "mistral-large-latest",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": original_report}
        ],
        "temperature": 0.2 # Alacsony érték: maradjon tényszerű és precíz
    }

    print("Riport küldése az AI-nak fordításra és átfogalmazásra... Kérlek várj.")
    
    # 4. API hívás és fájl mentése
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            ai_response_text = response.json()["choices"][0]["message"]["content"]
            
            # Markdown fájl létrehozása
            with open(output_md_path, "w", encoding="utf-8") as out_file:
                out_file.write(ai_response_text)
                
            print(f"\nSiker! Az AI által formázott értékelés elkészült: {output_md_path}")
        else:
            print(f"Hiba történt az API hívás során. Hibakód: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Hálózati vagy rendszerhiba: {e}")

# Ha közvetlenül ezt a fájlt futtatjuk, induljon el a folyamat
if __name__ == "__main__":
    create_ai_markdown_report()