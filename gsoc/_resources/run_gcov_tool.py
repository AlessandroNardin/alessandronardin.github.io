#!/usr/bin/env python
import base64
import subprocess
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("test_log", help="The path to the log file with the GCOV info")
args = parser.parse_args()

print(args)
gcov_block = ""
with open(args.test_log) as f:
    for line in f:
        if "GCOV INFO" in line:
            break
    for line in f:
        if "GCOV INFO" in line:
            break
        gcov_block += line.strip()
stream = base64.b64decode(gcov_block)

gcov_env = os.environ.copy()
subprocess.run(["arm-rtems6-gcov-tool", "merge-stream"], input=stream, env=gcov_env)
