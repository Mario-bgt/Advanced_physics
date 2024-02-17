#!/usr/bin/env python3

import sys
import io
import os
from hashlib import sha256
import inspect
import logging
import re
from logging import info, warning, error

logging.basicConfig(format='%(levelname)10s: %(message)s', level=logging.DEBUG)

DISTANCE=12

# distance calculation
def lev(s1, s2):
    if len(s1) < len(s2):
        return lev(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def abort():
    print("-- Validation aborted, fix the error above if you wish to continue --")
    sys.exit(1)

# check if submission.py is present and unchanged
if not os.path.exists("submission.py"):
    error("submission.py does not exist; are you running this script from the folder containing this task's submission.py?")
    abort()
else:
    with open("submission.py", "rb") as f:
        reference = "b474838841167554dc88dbda052261ffb3436e8e6228105c24f27e1d58473d95"
        checksum = sha256(f.read()).hexdigest()
        if reference != checksum:
            warning("submission.py appears to be different from your original submission.")
            warning("Did you change submission.py? Or did you even just open and (auto-) save submission.py?")
            warning("Some editors will auto-save files you opened and use a different encoding or apply formatting.")
            warning("-> this validation will only be valid if submission.py is exactly as you received it in the review zip file.")

# validate correction
if not os.path.exists("correction.py"):
    error(f"correction.py: does not exist; nothing to do")
    abort()
else:
    try:
        # mute output temporarily
        sys.stdout = sys.stderr = io.StringIO()
        import correction
        # unmute output
        sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__
        info("successfully imported correction.py")
    except Exception as e:
        sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__
        error(f"correction.py exists but unable to import ({e}); this correction will not be evaluated!")
        abort()

    # check if correction adheres to edit limit
    with open("submission.py") as f:
        submission = f.read()
    with open("correction.py") as f:
        correction = f.read()
    # count test class signature as 1 character
    testsig = r"class\s+Tests\(\s*TestCase\s*\):"
    submission = re.sub(testsig, "", submission)
    correction = re.sub(testsig, "", correction)
    # ignore imports
    imports = re.compile(r"^(?:from|import).*", re.MULTILINE)
    submission = re.sub(imports, "", submission)
    correction = re.sub(imports, "", correction)
    # ignore repeated characters
    repeats = re.compile(r"(.)\1+")
    submission = re.sub(repeats, r"\1", submission)
    correction = re.sub(repeats, r"\1", correction)
    # ignore trailing newlines
    submission = submission.rstrip()
    correction = correction.rstrip()
    distance = lev(submission, correction)
    if distance == 0:
        warning(f"correction.py: edit distance is {distance}, so apparently nothing has changed compared to submission.py.")
    elif distance <= DISTANCE:
        info(f"correction.py: edit distance is {distance} (OK); this correction will be evaluated")
    else:
        error(f"correction.py: edit distance is {distance} and thus above {DISTANCE}; this correction will not be evaluated!")

