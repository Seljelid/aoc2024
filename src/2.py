def red_nosed_reports():
    with open("data/2.txt") as f:
        lines = f.readlines()

    reports = []
    for line in lines:
        report = [int(x) for x in line.split(" ")]
        reports.append(report)

    safe_reports = sum(
        _classify_report(report) in ("decreasing", "increasing") for report in reports
    )
    print(f"Star 1: {safe_reports}")

    safe = 0
    for report in reports:
        altered_reports = [report[:i] + report[i + 1 :] for i in range(len(report))]
        if not all(_classify_report(r) == "neither" for r in altered_reports):
            safe += 1

    print(f"Star 2: {safe}")


def _classify_report(report: list) -> str:
    diffs = [j - i for i, j in zip(report[:-1], report[1:])]
    if all(x in (-1, -2, -3) for x in diffs):
        return "decreasing"
    elif all(x in (1, 2, 3) for x in diffs):
        return "increasing"
    else:
        return "neither"


if __name__ == "__main__":
    red_nosed_reports()
