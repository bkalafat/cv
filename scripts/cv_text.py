"""Plain-text companion to the ATS PDF, using the same canonical content."""

from cv_data import PROJECT_ROOT, load_cv, profile_links


def generate_ats_text():
    data = load_cv()
    profile = data["sidebar"]
    lines = [profile["name"], profile["tagline"], profile["location"], profile["timezone"]]
    lines.extend(label for label, _ in profile_links(data))
    lines.extend(["", "SUMMARY", data["career-profile"]["summary"], "", "TECHNICAL SKILLS"])
    lines.extend(f'{category["name"]}: {", ".join(category["items"])}' for category in data["skills"]["categories"])
    lines.extend(["", "PROFESSIONAL EXPERIENCE"])
    for job in data["experiences"]["info"]:
        lines.extend([f'{job["role"]} | {job["company"]}', job["time"], job["location"]])
        lines.extend(f"- {bullet}" for bullet in job["bullets"])
        lines.append("")
    lines.append("EDUCATION")
    for degree in data["education"]["info"]:
        lines.extend([degree["degree"], f'{degree["university"]}, {degree["location"]}', degree["time"]])
    lines.extend(["", "CERTIFICATIONS"])
    for credential in data["certifications"]["list"]:
        lines.extend([credential["name"], f'{credential["organization"]} | {credential["kind"]}'])
        if credential.get("start"):
            lines.append(str(credential["start"]))
        if credential.get("expires"):
            lines.append("Expires " + credential["expires"])
        if credential.get("credentialurl"):
            lines.append(f'{credential["credentialname"]}: {credential["credentialurl"]}')
        lines.append("")
    lines.append("LANGUAGES")
    lines.extend(f'{item["idiom"]}: {item["level"]}' for item in profile["languages"]["info"])
    lines.extend(["", "INTERESTS", "; ".join(item["item"] for item in profile["interests"]["info"])])
    path = PROJECT_ROOT / "downloads" / "Burak_Kalafat_ATS_CV.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated ATS plain text: {path}")
    return path
