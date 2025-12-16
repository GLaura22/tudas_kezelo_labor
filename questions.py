
# 0. question
print('''
Does your company has to follow NIS2 directive?
	yes if (all of them have to be true):
	1, you provide services or carry out activities in the EU
	2, you have more than 50 employees and have more than 10 million euro in revenue
	3, you operate in any of these sectors:
		Energy
		Transport
		Banking
		Financial market infrastructures
		Health
		Drinking water
		Waste water
		Digital infrastructure
		ICT service management (business-to-business)
		Public administration
		Space
		Postal and courier services
		Waste management
		Manufacture, production, and distribution of chemicals
		Production, processing, and distribution of food
		Manufacturing
		Digital providers
		Research''')
nis2ApplicabelCompany = input()
if nis2ApplicabelCompany == "No":
    print("It1s still a good praktice to follow NIS2 directive, but legally you dont have to.")
    exit()

#################### Responsibilities of senior management ##########################
# 1. question
print("What are the responsibilities of senior managenment regarding cyber security in the company?")
print("*approve cybersecurity measures* \n*oversee cybersecurity implementation* \n*holding accountability for cybersec measures being implemented*")
seniorManagementResponsibilities = input()

#################### Importance of training ##########################
# 2. question
print("Is top management required to take cyber security trainings?")
topManagementTraining = input()

# 3. question: 
print("Can the employees take part of cybersec trainings regularly?")
employeeTraining = input()

#################### Risk-based approach to cybersecurity ##########################
# 4. question
print("What four factors do you take into accountability, when asessing cyber security risks?") 
print("*exposure risks*\n*company size*\n*likelihood of occurrence of incidents and their severity*\n*societal and economic impacts of incidents*")
riskAssessmentFactors = input()

#################### Supply chain security ##########################
# 5. question
print("Do you know the vulnerabilities of your suppliers and service providers?")
supplyChainVulnerabilities = input()

#################### Reporting incidents ##########################
# 6. question
print("Is there currently a process where employees can report incidents to the computer security incident response teams?")
incidentReportingProcess = input()

# 7. question
print("Do you analise and categorize the reported incidents based on their severity?")
incidentAnalysisAndCategorization = input()

# 8. question
print("Is there a dokument where you store the status updates of the reported incidents?")
incidentStatusUpdatesDokument = input()

# 9. question
print("How long after the incident gets reported will be the incident report created?")
incidentReportCreationTime = input()

################### Using certified IT products and services ##########################
# 10. question
print("Do your company use certified IT products and services?")
certifiedITProductsUsage = input()

#################### Supervision ###########################
# 11. question
print("How do you make sure, that the required measures are beeing implemented and maintained?")
print("*on-site inspections*\n*off-site supervision*\n*cybersecurity audits*\n*security scans*")
supervisionMethods = input()

#################### Required Dokuments ##########################
# 12. question
