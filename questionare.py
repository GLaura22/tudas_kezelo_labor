import tkinter as tk
from tkinter import ttk
import generate_report
from datetime import datetime

class QuestionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NIS2 Questions")
        self.root.geometry("700x350")

        self.data = {}  # store all answers

        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.current_question = 0
        self.questions = []
        self.setup_questions()
        self.show_question()

    # -------------------------------------------------------------------------
    # Define all questions here
    # -------------------------------------------------------------------------
    def setup_questions(self):
        # company name
        self.questions.append({
            "text": "What is the name of your company?",
            "type": "text",
            "key": "companyName"
        })
        # 0. NIS2 applicability
        self.questions.append({
            "text": "Do you provide services or carry out activities in the EU?",
            "type": "radio",
            "options": ["Yes", "No"],
            "key": "nis2ApplicabelCompany"
        })

        self.questions.append({
            "text": "Do you have more than 50 employees and have more than 10 million euro in revenue?",
            "type": "radio",
            "options": ["Yes", "No"],
            "key": "nis2ApplicabelCompany2"
        })

        self.questions.append({
            "text": "Do you operate in any of these sectors?",
            "type": "dropdown",
            "options": ["Energy", "Transport", "Banking", "Financial market infrastructures", "Health", "Drinking water", "Waste water", "Digital infrastructure", "ICT service management (business-to-business)", "Public administration", "Space", "Postal and courier services", "Waste management", "Manufacture, production, and distribution of chemicals", "Production, processing, and distribution of food", "Manufacturing", "Digital providers", "Research", "None of the above"],
            "key": "nis2ApplicabelCompany3"
        })

        # 1. Responsibilities of senior management
        self.questions.append({
            "text": "What are the responsibilities of senior management?",
            "type": "checkbox",
            "options": [
                "Approve cybersecurity measures",
                "Oversee cybersecurity implementation",
                "Hold accountability for implementation"
            ],
            "documentation_options": [
                "Measurement Report",
                "Internal Audit Report",
                "Management Review Minutes",
                "Not Documented"
            ],
            "key": "seniorManagementResponsibilities"
        })

        # 2. Top management training
        self.questions.append({
            "text": "Is top management required to take cyber security trainings?",
            "type": "radio",
            "options": ["Yes", "No"],
            "dokumentation_options": [
                "Training and Awareness Plan",
                "Not Documented"
            ],
            "key": "topManagementTraining"
        })

        # 3. Employee training
        self.questions.append({
            "text": "Do employees take part in cybersecurity trainings regularly?",
            "type": "radio",
            "options": ["Yes", "No"],
            "dokumentation_options": [
                "Training and Awareness Plan",
                "Not Documented"
            ],
            "key": "employeeTraining"
        })

        # 4. Risk assessment factors
        self.questions.append({
            "text": "Which factors do you consider when assessing cybersecurity risks?",
            "type": "checkbox",
            "options": [
                "Exposure risks",
                "Company size",
                "Likelihood & severity of incidents",
                "Societal & economic impacts"
            ],
            "dokumentation_options": [
                "Risk Assassment Methodology",
                "Risk Treatment Plan",
                "Access Control Policy",
                "Not Documented"
            ],
            "key": "riskAssessmentFactors"
        })

        # 5. Supply chain vulnerabilities
        self.questions.append({
            "text": "Do you know the vulnerabilities of your suppliers?",
            "type": "radio",
            "options": ["Yes", "No"],
            "dokumentation_options": [
                "Supplier Security Policy",
                "Not Documented"
            ],
            "key": "supplyChainVulnerabilities"
        })

        # 6. Incident reporting process
        self.questions.append({
            "text": "Is there a process for employees to report incidents to CSIRT?",
            "type": "radio",
            "options": ["Yes", "No"],
            "dokumentation_options": [
                "Incident Handling Policy",
                "Not Documented"
            ],
            "key": "incidentReportingProcess"
        })

        # 7. Categorization of incidents
        self.questions.append({
            "text": "Do you analyze and categorize reported incidents by severity?",
            "type": "radio",
            "options": ["Yes", "No"],
            "key": "incidentAnalysisAndCategorization"
        })

        # 8. Incident status documentation
        self.questions.append({
            "text": "Is there a document storing status updates of incidents?",
            "type": "radio",
            "options": ["Yes", "No"],
            "key": "incidentStatusUpdatesDokument"
        })

        # 9. Incident report timing
        self.questions.append({
            "text": "How long after an incident is the incident report created? (in working days)",
            "type": "text",
            "key": "incidentReportCreationTime"
        })

        # 10. Certified IT products
        self.questions.append({
            "text": "Does your company use certified IT products & services?",
            "type": "radio",
            "options": ["Yes", "No"],
            "key": "certifiedITProductsUsage"
        })

        # 11. Supervision methods
        self.questions.append({
            "text": "How do you ensure cybersecurity measures are implemented & maintained?",
            "type": "checkbox",
            "options": [
                "On-site inspections",
                "Off-site supervision",
                "Cybersecurity audits",
                "Security scans"
            ],
            "key": "supervisionMethods"
        })

        

    # -------------------------------------------------------------------------
    # Show a question
    # -------------------------------------------------------------------------
    def show_question(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        q = self.questions[self.current_question]

        label = tk.Label(self.container, text=q["text"], font=("Arial", 14), wraplength=600)
        label.pack(pady=10)

        self.answer_vars = []

        if q["type"] == "radio":
            var = tk.StringVar()
            var.set("")
            self.answer_vars.append(var)
            for option in q["options"]:
                rb = tk.Radiobutton(self.container, text=option, variable=var, value=option)
                rb.pack(anchor="w")
        
        elif q["type"] == "checkbox":
            for option in q["options"]:
                var = tk.BooleanVar()
                chk = tk.Checkbutton(self.container, text=option, variable=var)
                chk.pack(anchor="w")
                self.answer_vars.append((option, var))

        elif q["type"] == "text":
            var = tk.StringVar()
            entry = tk.Entry(self.container, textvariable=var, width=50)
            entry.pack(pady=10)
            self.answer_vars.append(var)

        elif q["type"] == "dropdown":
            var = tk.StringVar()
            var.set(q["options"][0])  # default value
            dropdown = ttk.Combobox(self.container, textvariable=var, values=q["options"], state="readonly", width=47)
            dropdown.pack(pady=10)
            self.answer_vars.append(var)


        next_btn = tk.Button(self.container, text="Next", command=self.save_and_next)
        next_btn.pack(pady=20)

    # -------------------------------------------------------------------------
    # Save answer and continue
    # -------------------------------------------------------------------------
    def save_and_next(self):
        q = self.questions[self.current_question]

        if q["type"] == "radio":
            self.data[q["key"]] = self.answer_vars[0].get()

        elif q["type"] == "checkbox":
            checked = [opt for opt, var in self.answer_vars if var.get()]
            self.data[q["key"]] = checked

        elif q["type"] == "text":
            self.data[q["key"]] = self.answer_vars[0].get()

        elif q["type"] == "dropdown":
            self.data[q["key"]] = self.answer_vars[0].get()


        # -----------------------------
        # NIS2 applicability logic
        # -----------------------------
        # After question 2 (index 2), check answers
        if self.current_question == 3:
            q0 = self.data.get("companyName")  
            q1 = self.data.get("nis2ApplicabelCompany")
            q2 = self.data.get("nis2ApplicabelCompany2")
            q3 = self.data.get("nis2ApplicabelCompany3")

            exception_case = (
                q1 == "Yes" and
                q2 == "No" and
                q3 == "Digital infrastructure"
            )

            # Normal stop condition (unless exception applies)
            if not exception_case:
                if q1 != "Yes" or q3 == "None of the above" or (q2 != "Yes"):
                    self.show_final_message(
                        "Your company does NOT have to follow the NIS2 directive.\nYou can find your report in 'nis2_report.txt'." 
                    )


                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    company_name = str(q0)

                    lines = []
                    lines.append("NIS2 COMPLIANCE REPORT")
                    lines.append("=" * 50)
                    lines.append(f"Company name: {company_name}")
                    lines.append(f"Report generated: {now}")
                    lines.append("")
                    lines.append(f"NIS2 applicable: NO")
                    lines.append("")
                    lines.append("For your company it is only recommended to follow NIS2 directive.")
                    lines.append("")
                    lines.append("Link for the official NIS2 directive document: https://eur-lex.europa.eu/eli/dir/2022/2555")
                    lines.append("Link for a summary of the key rules of NIS2 and implementation steps: https://advisera.com/articles/nis2-implementation-steps/")
                    lines.append("")
                    lines.append("End of report")

                    with open("nis2_reportx.txt", "w", encoding="utf-8") as f:
                        f.write("\n".join(lines))

                    return

        self.current_question += 1
        print(str(self.current_question))

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    # -------------------------------------------------------------------------
    # Final results screen
    # -------------------------------------------------------------------------
    def show_results(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        tk.Label(self.container, text="Completed!", font=("Arial", 18)).pack(pady=10)

        text = tk.Text(self.container, width=80, height=20)
        text.pack()

        company_name = self.data.get("companyName")
        text.insert("end", f"{company_name} answers:\n\n")
        for key, value in self.data.items():
            text.insert("end", f"{key}: {value}\n")


        report_path = generate_report.generate_report(self.data)

        text.insert("end", "\n\nReport generated:\n")
        text.insert("end", report_path)

    def show_final_message(self, msg):
        for widget in self.container.winfo_children():
            widget.destroy()
        tk.Label(self.container, text=msg, font=("Arial", 16)).pack(pady=40)

# -------------------------------------------------------------------------
# Start the app
# -------------------------------------------------------------------------
root = tk.Tk()
app = QuestionnaireApp(root)
root.mainloop()
