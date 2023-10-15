def processLines(lines) -> str:
    N = int(lines[0])
    T = int(lines[1])
    total_tasks = T

    for i in range(2, 2 + N):
        V, U = map(int, lines[i].split())
        total_tasks += U - V

    if total_tasks == 0:
        return "OK"
    else:
        return "KO"
