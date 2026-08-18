import subprocess

cmd = [
    r"D:\AAA_projects\workspace1\spectrum-agent\.venv\Scripts\python.exe",
    "spectrum_agent.py",
    "analyze",
    "data",
    "--out",
    "output"
]

res = subprocess.run(
    cmd,
    capture_output=True,
    encoding="utf-8",
    cwd=r"D:\AAA_projects\workspace1\spectrum-agent"
)

print("stdout:\n", res.stdout)
print("stderr:\n", res.stderr)
print("returncode:", res.returncode)