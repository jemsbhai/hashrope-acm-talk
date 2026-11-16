#!/usr/bin/env python3
"""Append section 12 (Challenges) to hashrope_demo.ipynb.

Writes the student (stub) version to the repo notebook, and a solution-filled
copy to /tmp for execution testing.
"""
import json, copy

NB = '/home/hatch/workspace/hashrope-acm-talk/hashrope_demo.ipynb'
TEST = '/tmp/hashrope_demo_solved.ipynb'

def md(src):
    return {'cell_type': 'markdown', 'metadata': {}, 'source': src.splitlines(keepends=True)}

def code(src):
    return {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [],
            'source': src.splitlines(keepends=True)}

INTRO = """## 12. Challenges

Three exercises, using only operations from the sections above. Each code cell sets up the problem and ends with a check that prints PASS when your answer is right. The checks never print the answer itself.

If you finished the hands-on early, start here."""

CH1_MD = """### Challenge 1: find every divergence

Section 5 found the *first* differing byte with one `rope_lcp`. This copy of a 256 KB sequence was tampered with in **three** places. Find all three offsets.

Hint: `rope_range_lcp(a, start, b, start, n)` returns the length of the common prefix of the two ranges starting at `start`. After a difference at position `p`, continue the comparison from `p + 1`."""

CH1_CODE = """import random
from hashrope import rope_range_lcp

rng = random.Random(20261120)
base = bytes(rng.randrange(256) for _ in range(256 * 1024))
orig = rope_from_chunks(base, 4096, h)

tampered = bytearray(base)
_truth1 = sorted(rng.sample(range(1000, len(base) - 1000), 3))
for p in _truth1:
    tampered[p] ^= 0xFF
copy1 = rope_from_chunks(bytes(tampered), 4096, h)

diffs = []  # your code here: fill with the three offsets, ascending

print("PASS" if diffs == _truth1 else f"not yet: you found {diffs}")"""

CH1_SOL = """diffs = []
pos = 0
n = len(base)
while pos < n:
    step = rope_range_lcp(orig, pos, copy1, pos, n - pos)
    pos += step
    if pos < n:
        diffs.append(pos)
        pos += 1"""

CH2_MD = """### Challenge 2: compose a cache key without the parts

A bundle is `header || payload`. A cache already stores the fingerprint of each part and the payload's length, but not the bytes. Compose the fingerprint of the whole bundle from those three numbers alone, then check it against the real rope.

This is `hash_concat` from the recipes: the key of A followed by B, from the keys of the parts, with no re-read of either part."""

CH2_CODE = """header = b"HDR:" + bytes(range(64))
payload = bytes((i * 7) % 256 for i in range(10_000))
ra, rb = rope_from_chunks(header, 4096, h), rope_from_chunks(payload, 4096, h)

fp_a, len_b, fp_b = rope_hash(ra), rope_len(rb), rope_hash(rb)

key_ab = None  # your code here: compose it from fp_a, len_b, fp_b only

_truth2 = rope_hash(rope_concat(ra, rb, h))
print("PASS" if key_ab == _truth2 else "not yet: that is not the bundle's fingerprint")"""

CH2_SOL = """key_ab = h.hash_concat(fp_a, len_b, fp_b)"""

CH3_MD = """### Challenge 3: find the repeated window

A 32 KB stream contains a 2 KB chunk that appears **twice**. You are given the fingerprint of the chunk. Find the offset of its second occurrence, using window fingerprints (`rope_substr_hash`) rather than comparing bytes.

The first occurrence is at offset 6,000. Windows can start at any byte offset, so scan."""

CH3_CODE = """rng3 = random.Random(42)
stream = bytearray(rng3.randrange(256) for _ in range(32 * 1024))
stream[20_000:22_000] = stream[6_000:8_000]          # the same 2 KB, again
srope = rope_from_chunks(bytes(stream), 4096, h)

target = rope_substr_hash(srope, 6_000, 2_000, h)    # fingerprint of the chunk

second = None  # your code here: the offset of the second occurrence

print("PASS" if second == 20_000 else f"not yet: {second}")"""

CH3_SOL = """for off in range(6_001, 32 * 1024 - 2_000 + 1):
    if rope_substr_hash(srope, off, 2_000, h) == target:
        second = off
        break"""

OUTRO = """Done all three? You have used the whole argument of the talk: fingerprints to find candidates cheaply, exact comparisons to decide, and composition to avoid re-reading data.

Stuck on one: re-read section 2 (substring fingerprints), section 5 (verify and locate), and the cache-key recipe in the talk's cheat sheet."""

nb = json.load(open(NB))
cells = nb['cells']

# audience fix in section 11: "your hackathon project" -> "your next project"
for c in cells:
    if c['cell_type'] == 'markdown':
        c['source'] = [s.replace('your hackathon project', 'your next project') for s in c['source']]

new_cells = [md(INTRO), md(CH1_MD), code(CH1_CODE), md(CH2_MD), code(CH2_CODE),
             md(CH3_MD), code(CH3_CODE), md(OUTRO)]
nb['cells'] = cells + new_cells
json.dump(nb, open(NB, 'w'), indent=1)
print('student version written:', len(nb['cells']), 'cells')

solved = copy.deepcopy(nb)
sol = {CH1_CODE.split('diffs = []')[0]: None}  # placeholder
# fill solutions by replacing the stub lines
for c in solved['cells']:
    if c['cell_type'] != 'code':
        continue
    src = ''.join(c['source'])
    if 'diffs = []  # your code here' in src:
        src = src.replace('diffs = []  # your code here: fill with the three offsets, ascending', CH1_SOL)
    elif 'key_ab = None  # your code here' in src:
        src = src.replace('key_ab = None  # your code here: compose it from fp_a, len_b, fp_b only', CH2_SOL)
    elif 'second = None  # your code here' in src:
        src = src.replace('second = None  # your code here: the offset of the second occurrence', CH3_SOL)
    c['source'] = src.splitlines(keepends=True)
json.dump(solved, open(TEST, 'w'), indent=1)
print('solved test copy written:', TEST)
