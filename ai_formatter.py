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
        "You are a professional cybersecurity auditor."
        "Your task is to rephrase the provided raw English NIS2 audit report into an executive summary in Markdown (.md) format. "
        "Additionally, enhance the English report by appending a Hungarian-language evaluation (a direct translation of the English summary,"
        "placed immediately after the English version). \n"

        "RULES:\n"

        "1. Craft clear, coherent, and easy-to-understand sentences instead of raw bullet points.\n"
        "2. Preserve the original document structure (e.g., Company Data, Gaps, Recommended Actions, Links).\n"
        "3. Integrate sections labeled as “missing” or “necessary documentation” into the text as meaningful explanations.\n"
        "4. Strictly use only the information provided in the input. Do not invent new NIS2 regulations or details.\n"
        "5. The report must always begin with official links to the NIS2 Directive and the NIS2 Summary.\n"
        "6. At the top of the Markdown file, include the text: SCROLL DOWN FOR HUNGARIAN!\n"
        "7. Write in flowing prose. Organize the text into sections and use bullet points or numbering only when absolutely necessary.\n"
        "8. Do not include ````markdown at the beginning or end of the text. Only provide the formatted content.\n" \
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

    print("Sending repotr to Mistral AI... Please wait!")
    
    # 4. API hívás és fájl mentése
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            ai_response_text = response.json()["choices"][0]["message"]["content"]
            
            # Markdown fájl létrehozása
            with open(output_md_path, "w", encoding="utf-8") as out_file:
                out_file.write(ai_response_text)
                
            print(f"\nResult: {output_md_path}")
        else:
            print(f"Hiba történt az API hívás során. Hibakód: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Hálózati vagy rendszerhiba: {e}")

# Ha közvetlenül ezt a fájlt futtatjuk, induljon el a folyamat
if __name__ == "__main__":
    create_ai_markdown_report()