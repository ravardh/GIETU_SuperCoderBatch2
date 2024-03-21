def find_murderer(evidence, suspects):
    for i, suspect in enumerate(suspects, start=1):
        if evidence in suspect[:10]:
            return f"Suspect {i} is the murderer."
    return "Murderer not found based on the provided evidence."

if __name__ == "__main__":
    evidence = "GCTA"
    suspects = [
        "ATCGATCGATAGCTAGCTACTCAGTCACTGACTGACTGA",
        "ATAGCTAGCTCGATCGATCGATCGATCGATCGATCGATCGA",
        "ACTCAGTCACATCGATCGATCGATCGATCGATCGATCGAT",
        "TGACTGACTGATCGATCGATCGATCGATCGATCGATCGATC"
    ]

    print(find_murderer(evidence, suspects))
