def skill_gap(resume, jd):
    missing = list(set(jd) - set(resume))
    strong = list(set(resume) & set(jd))

    return {
        "missing": missing,
        "strong": strong
    }