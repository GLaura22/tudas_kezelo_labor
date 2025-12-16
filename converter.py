from rdflib import Graph

# Step 1: Create a graph
g = Graph()

# Step 2: Parse the existing TTL file
g.parse("nis2_audit_onthology.ttl", format="turtle")

# Step 3: Serialize the graph into RDF/XML (OWL-compatible format)
g.serialize(destination="nis2_audit_onthology.owl", format="xml")

print("✅ Converted TTL to OWL successfully!")
