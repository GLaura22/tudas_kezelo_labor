from onthology_mapping import load_requirement_document_mapping
from owlready2 import get_ontology, sync_reasoner_pellet
from datetime import datetime
from requironment_mapping import REPORT_TO_ONTOLOGY
from advice_mapping import ONTOLOGY_ADVICE
from advice_text import ADVICE_TEXTS
from requironment_texts import REQUIREMENT_TEXTS
import json



# Példa: Hogyan használd, ha az ontológia/kód alapján hiányzik az "Exposure risks"
###### hianyzo_kulcs = "Exposure risks"
###### if hianyzo_kulcs in ai_knowledge:
######     adat = ai_knowledge[hianyzo_kulcs]
######     print(f"Téma: {adat['tema']}")
######     print(f"Tény: {adat['teny']}")
######     print(f"Lépés: {adat['lepes']}")


def generate_report(company_data, output_path="nis2_report.txt"):

    with open("ai_knowledgebase.json", "r", encoding="utf-8") as file:
        ai_knowledge = json.load(file)
    # -------------------------------------------------
    # Helper functions
    # -------------------------------------------------
    def yes(value):
        return value == "Yes"

    def missing_items(selected, required):
        return [item for item in required if item not in selected]

    def incident_report_time_ok(value):
        try:
            days = int(value)
            return days <= 22
        except (ValueError, TypeError):
            return False

    # -------------------------------------------------
    # Determine NIS2 applicability
    # -------------------------------------------------
    q1 = company_data.get("nis2ApplicabelCompany")
    q2 = company_data.get("nis2ApplicabelCompany2")
    q3 = company_data.get("nis2ApplicabelCompany3")

    # such as mobile network suppliers
    exception_case = (
        q1 == "Yes" and
        q2 == "No" and
        q3 == "Digital infrastructure"
    )

    nis2_applicable = (
        q1 == "Yes" and
        q3 != "None of the above" and
        (q2 == "Yes" or exception_case)
    )

    # -------------------------------------------------
    # Requirement definitions (with expected items)
    # -------------------------------------------------
    requirements = [
        {
            "name": "Senior management responsibilities (Art. 20)",
            "expected": [
                "Approve cybersecurity measures",
                "Oversee cybersecurity implementation",
                "Hold accountability for implementation"
            ],
            "selected": company_data.get("seniorManagementResponsibilities", [])
        },
        {
            "name": "Risk-based cybersecurity approach (Art. 21)",
            "expected": [
                "Exposure risks",
                "Company size",
                "Likelihood & severity of incidents",
                "Societal & economic impacts"
            ],
            "selected": company_data.get("riskAssessmentFactors", [])
        },
        {
            "name": "Incident analysis & categorization (Art. 23)",
            "fulfilled": yes(company_data.get("incidentAnalysisAndCategorization"))
        },
        {
            "name": "Incident status documentation (Art. 23)",
            "fulfilled": yes(company_data.get("incidentStatusUpdatesDokument"))
        },
        {
            "name": "Incident report creation time ≤ 5 working days (Art. 23)",
            "fulfilled": incident_report_time_ok(
                company_data.get("incidentReportCreationTime")
            )
        },
        {
            "name": "Supervision of cybersecurity measures (Art. 21)",
            "expected": [
                "On-site inspections",
                "Off-site supervision",
                "Cybersecurity audits",
                "Security scans"
            ],
            "selected": company_data.get("supervisionMethods", [])
        }
    ]

    # -------------------------------------------------
    # Evaluate missing requirements
    # -------------------------------------------------
    missing_requirements = []

    for req in requirements:
        if "expected" in req:
            missing = missing_items(req["selected"], req["expected"])
            if missing:
                missing_requirements.append((req["name"], missing))
        else:
            if not req["fulfilled"]:
                missing_requirements.append((req["name"], None))


    # --------------------------------------------------
    # Collect advice based on missing ontology classes
    # --------------------------------------------------
    advice_seen = set()
    advice_lines = []

    for req_name, _ in missing_requirements:
        ontology_class = REPORT_TO_ONTOLOGY.get(req_name)
        if ontology_class in ONTOLOGY_ADVICE:
            for advice_key in ONTOLOGY_ADVICE[ontology_class]:
                if advice_key not in advice_seen:
                    advice_seen.add(advice_key)
                    advice_lines.append(advice_key)


    # -------------------------------------------------
    # Load onthology
    # -------------------------------------------------
    mapping = load_requirement_document_mapping()
    # -------------------------------------------------
    # Generate report content
    # -------------------------------------------------
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    company_name = company_data.get("companyName", "Unknown Company")

    lines = []
    lines.append("NIS2 COMPLIANCE REPORT")
    lines.append("=" * 50)
    lines.append(f"Company name: {company_name}")
    lines.append(f"Report generated: {now}")
    lines.append("")
    lines.append(f"NIS2 applicable: {'YES' if nis2_applicable else 'NO'}")
    lines.append("")
    lines.append("Link for the official NIS2 directive document: https://eur-lex.europa.eu/eli/dir/2022/2555")
    lines.append("")
    lines.append("Link for a summary of the key rules of NIS2 and implementation steps: https://advisera.com/articles/nis2-implementation-steps/")
    lines.append("")

    if not nis2_applicable:
        lines.append("The company is currently NOT required to comply with NIS2.")
    else:
        if missing_requirements:
            lines.append("Missing / incomplete requirements:")
            ontology_docs = load_requirement_document_mapping()

            for name, missing in missing_requirements:
                lines.append(f" - {name}")

                # Missing checkbox items (if any)
                if missing:
                    for item in missing:
                        lines.append(f"       missing: {item}")

                ontology_class = REPORT_TO_ONTOLOGY.get(name)
                docs = ontology_docs.get(ontology_class, [])

                lines.append("       necessary documentation:")
                if docs:
                    for doc in docs:
                        lines.append(f"              - {doc}")
                else:
                    lines.append("              - No documentation defined in ontology")

                # Detailed description for the requirement
                text = REQUIREMENT_TEXTS.get(name)
                if text:
                    lines.append("       requirement description:")
                    for line in text.splitlines():
                        lines.append(f"       {line}")

        else:
            lines.append("All evaluated NIS2 requirements are fulfilled.")

        if advice_lines:
            lines.append("\nRecommended next steps:\n")

            for advice_key in advice_lines:
                advice_text = ADVICE_TEXTS.get(advice_key)
                if advice_text:
                    lines.append(f"- {advice_text}\n")


    lines.append("")
    lines.append("End of report")

    # -------------------------------------------------
    # Write file
    # -------------------------------------------------
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path
