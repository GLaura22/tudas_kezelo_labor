from owlready2 import get_ontology, sync_reasoner_pellet

onto = get_ontology("nis2_audit_onthology.owl").load()

Company = onto.search_one(iri="*Company")
print(Company)


sync_reasoner_pellet()

for cls in onto.classes():
    print("Class:", cls)

#print("Inferred types:", acme.is_a)

for ind in onto.NIS2_requironment.instances():
    print(ind)

for doc in onto.Dokument.instances():
        related_reqs = getattr(doc, "belongs_to", [])
        if related_reqs:
            print(f"{doc.name} belongs to {[r.name for r in related_reqs]}")
        else:
            print(f"{doc.name} belongs to nothing")


