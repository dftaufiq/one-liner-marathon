import os

LINE = "My Wi-Fi died 10 minutes into a job interview, so I shouted my answers through the wall. My neighbour Mr. Hartono heard every word \u2014 and got the job."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-280 chars,
# not only whitespace, a single line. Fail loudly instead of shipping
# an invalid entry.
if not 1 <= len(LINE) <= 280 or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-280 char single-line gate")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
