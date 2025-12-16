from owlready2 import get_ontology, sync_reasoner_pellet


def load_requirement_document_mapping(ontology_path="nis2_audit_onthology.owl"):
    """
    Returns:
        dict: {
            "SupplyChainSecurity": ["Supplier_Security_Policy", "Confidentiality_Statement"],
            "RiskBasedApproach": ["Risk_Assessment_Methodology", "Risk_Treatment_Plan"],
            ...
        }
    """

    onto = get_ontology(ontology_path).load()
    sync_reasoner_pellet(infer_property_values=True)

    requirement_to_docs = {}

    # Iterate over Dokument instances
    for doc in onto.Dokument.instances():
        related_reqs = getattr(doc, "belongs_to", [])
        for req in related_reqs:
            req_name = req.name
            doc_name = doc.name.replace("_", " ")

            requirement_to_docs.setdefault(req_name, []).append(doc_name)

    return requirement_to_docs

def load_requirement_document_mapping(ontology_path="nis2_audit_onthology.owl"):
    onto = get_ontology(ontology_path).load()
    sync_reasoner_pellet(infer_property_values=True)

    mapping = {}

    for doc in onto.Dokument.instances():
        related_reqs = getattr(doc, "belongs_to", [])
        for req in related_reqs:
            mapping.setdefault(req.name, set()).add(
                doc.name.replace("_", " ")
            )

    # convert sets to sorted lists
    return {k: sorted(v) for k, v in mapping.items()}


def print_missing_requirement_docs(missing_requirements, ontology_path="nis2_audit_onthology.owl"):
    """
    missing_requirements: list of requirement class names (strings)
    """

    mapping = load_requirement_document_mapping(ontology_path)

    for req in missing_requirements:
        print(f" - {req}")
        docs = mapping.get(req, [])
        if docs:
            print("       necessary documentation:")
            for d in docs:
                print(f"              - {d}")
        else:
            print("       necessary documentation:")
            print("              - No documentation defined in ontology")

load_requirement_document_mapping()
