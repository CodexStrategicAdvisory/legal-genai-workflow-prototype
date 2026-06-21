import json

def load_contract():
    with open("data/sample_contract.txt", "r") as f:
        return f.read()

def extract_facts(text):
    facts = []
    if "30 days" in text:
        facts.append(("Payment due in 30 days", "Found in payment clause"))
    if "confidential" in text.lower():
        facts.append(("Confidentiality obligations apply", "Found in confidentiality clause"))
    return facts

def two_pass_summary(facts):
    if not facts:
        return "Insufficient information to summarize."
    return "This contract includes: " + "; ".join([f[0] for f in facts]) + "."

def citation_or_abstain(facts):
    if not facts:
        return ["Insufficient information to identify risks."]
    return [f"{fact} ({cite})" for fact, cite in facts]

def build_schema(summary, facts):
    return {
        "summary": summary,
        "obligations": [f[0] for f in facts],
        "risks_identified": [],
        "citations": citation_or_abstain(facts)
    }

if __name__ == "__main__":
    text = load_contract()
    facts = extract_facts(text)
    summary = two_pass_summary(facts)
    schema = build_schema(summary, facts)

    print(json.dumps(schema, indent=4))
