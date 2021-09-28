def createReport(mass: list) -> list:
    result = []
    for i in mass:
        video = {"id": str(i[0]), "status": i[1], "current_progress": i[2], "result_aggregation": {
            "faces_count": i[3]
        }}
        result.append(video)
    return result
