#!/usr/bin/env python3
"""Generate a Django Case Study III LaTeX provenance table with verified committer dates.

Run with internet access:
  python django_committer_dates_table.py
Or using an existing full Django repository clone:
  python django_committer_dates_table.py --repo /path/to/django

No extra Python packages required. GitHub API anonymous rate limit: 60 requests/hour.
"""
import argparse
import csv
import json
import subprocess
import urllib.request
from pathlib import Path

ROWS = [
    ("Ticket \\#30289", "e245046b", "Vulnerable", "Admin permission checks"),
    ("", "8335d592", "Corrected", ""),
    ("", "0027ca76", "Post-fix 1", ""),
    ("", "f9f09a8a", "Post-fix 2", ""),
    ("", "7191beec", "Post-fix 3", ""),
    ("", "3d465f77", "Post-fix 4", ""),
    ("", "3e01aab5", "Post-fix 5", ""),
    ("", "93daed25", "Post-fix 6", ""),
    ("", "7cbcf2e2", "Post-fix 7", ""),
    ("CVE-2019-12308", "98c0fe19", "Vulnerable", "Admin URL rendering"),
    ("", "deeba6d9", "Corrected", ""),
    ("CVE-2021-31542", "8de4ca74", "Vulnerable", "Uploaded-file and storage paths"),
    ("", "0b79eb36", "Corrected", ""),
    ("CVE-2021-33203", "f66ae7a2", "Vulnerable", "Admin documentation path handling"),
    ("", "46572de2", "Corrected", ""),
]


def date_for_sha(sha: str, repo: Path | None) -> str:
    if repo:
        return subprocess.check_output(
            ["git", "-C", str(repo), "show", "-s", "--format=%cs", sha],
            text=True,
        ).strip()
    url = "https://api.github.com/repos/django/django/commits/" + sha
    request = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "django-s3dt-checkpoint-provenance/1.0",
    })
    with urllib.request.urlopen(request, timeout=30) as r:
        record = json.load(r)
    assert record["sha"].startswith(sha), f"SHA mismatch for {sha}"
    return record["commit"]["committer"]["date"][:10]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, help="Existing Django Git clone (avoids GitHub API)")
    parser.add_argument("--out", type=Path, default=Path("django_history_committer_dates.tex"))
    args = parser.parse_args()
    rows = []
    for issue, sha, role, component in ROWS:
        date = date_for_sha(sha, args.repo)
        rows.append((issue, sha, date, role, component))
        print(f"{sha}  {date}  {role}")

    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Historical Django checkpoints, Git committer dates, and their roles in the evaluation.}",
        r"\label{tab:django-history}",
        r"\scriptsize",
        r"\begin{tabularx}{\linewidth}{@{}llll>{\raggedright\arraybackslash}X@{}}",
        r"\toprule",
        r"\textbf{Security history} & \textbf{Git revision} & \revision{\textbf{Commit date}} & \textbf{Role} & \revision{\textbf{Source component}} \\",
        r"\midrule",
    ]
    for issue, sha, date, role, component in rows:
        if issue and lines[-1] != r"\midrule" and not lines[-1].endswith(r"\toprule"):
            lines.append(r"\midrule")
        comp = r"\revision{" + component + "}" if component else ""
        lines.append(f"{issue} & \\texttt{{{sha}}} & \\revision{{{date}}} & {role} & {comp} " + r"\\")
    lines.extend([r"\bottomrule",r"\end{tabularx}",r"\end{table}"])
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    csvpath = args.out.with_suffix(".csv")
    with csvpath.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Security history", "Git revision", "Git committer date", "Role", "Source component"])
        for row in rows:
            writer.writerow((row[0].replace(r"\#", "#"), *row[1:]))
    print(f"\nSaved {args.out} and {csvpath}")
    print("Preamble requires \\usepackage{booktabs,tabularx,array}.")

if __name__ == "__main__":
    main()
