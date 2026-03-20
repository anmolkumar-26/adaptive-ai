GRAPH = {
    "python": [],
    "backend": ["python"],
    "api": ["backend"],
    "system design": ["api"]
}

def generate_roadmap(missing):
    roadmap = []

    for skill in missing:
        deps = GRAPH.get(skill, [])
        for d in deps:
            roadmap.append({"skill": d, "level": "basic"})
        roadmap.append({"skill": skill, "level": "advanced"})

    return roadmap