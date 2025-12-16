
class Company:
    def __init__(self, data_dict):

        # lists values
        self.seniorManagementResponsibilities = data_dict["seniorManagementResponsibilities"]
        self.riskAssessmentFactors = data_dict["riskAssessmentFactors"]
        self.incidentReportCreationTime = data_dict["incidentReportCreationTime"]
        self.supervisionMethods = data_dict["supervisionMethods"]

        # yes/no values
        self.topManagementTraining = data_dict["topManagementTraining"]
        self.employeeTraining = data_dict["employeeTraining"]        
        self.supplyChainVulnerabilities = data_dict["supplyChainVulnerabilities"]
        self.incidentReportingProcess = data_dict["incidentReportingProcess"]
        self.incidentAnalysisAndCategorization = data_dict["incidentAnalysisAndCategorization"]
        self.incidentStatusUpdatesDokument = data_dict["incidentStatusUpdatesDokument"]        
        self.certifiedITProductsUsage = data_dict["certifiedITProductsUsage"]


    def __str__(self):
        attrs = [
            f"Senior Management Responsibilities: {', '.join(self.seniorManagementResponsibilities)}",
            f"Risk Assessment Factors: {', '.join(self.riskAssessmentFactors)}",
            f"Incident Report Creation Time: {self.incidentReportCreationTime}",
            f"Supervision Methods: {', '.join(self.supervisionMethods)}",
            f"Top Management Training: {self.topManagementTraining}",
            f"Employee Training: {self.employeeTraining}",
            f"Supply Chain Vulnerabilities: {self.supplyChainVulnerabilities}",
            f"Incident Reporting Process: {self.incidentReportingProcess}",
            f"Incident Analysis and Categorization: {self.incidentAnalysisAndCategorization}",
            f"Incident Status Updates Documented: {self.incidentStatusUpdatesDokument}",
            f"Certified IT Products Usage: {self.certifiedITProductsUsage}"
        ]
        return "\n".join(attrs)

'''
nis2ApplicabelCompany: Yes
nis2ApplicabelCompany2: Yes
nis2ApplicabelCompany3: Energy
seniorManagementResponsibilities: ['Approve cybersecurity measures']
topManagementTraining: Yes
employeeTraining: Yes
riskAssessmentFactors: ['Company size', 'Likelihood & severity of incidents']
supplyChainVulnerabilities: Yes
incidentReportingProcess: Yes
incidentAnalysisAndCategorization: Yes
incidentStatusUpdatesDokument: No
incidentReportCreationTime: 1 week
certifiedITProductsUsage: No
supervisionMethods: ['Cybersecurity audits', 'Security scans']
'''