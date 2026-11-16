#!/usr/bin/env python3
"""Build the ACM chapter version of the Hashrope talk deck from the DevFest Florida deck."""
import copy
from pptx import Presentation

SRC = '/home/hatch/workspace/hashrope-acm-talk/hashrope-acm-talk.pptx'
prs = Presentation(SRC)
slides = list(prs.slides)
assert len(slides) == 23, len(slides)
by_old = {i + 1: s for i, s in enumerate(slides)}


def set_shape_text(shape, new_text):
    """Replace a shape's text paragraph by paragraph, preserving run formatting."""
    tf = shape.text_frame
    lines = new_text.split('\n')
    for idx, p in enumerate(tf.paragraphs):
        if idx < len(lines):
            if p.runs:
                p.runs[0].text = lines[idx]
                for r in p.runs[1:]:
                    r.text = ''
            elif lines[idx]:
                p.text = lines[idx]
        else:
            for r in p.runs:
                r.text = ''
    if len(lines) > len(tf.paragraphs) and tf.paragraphs:
        p = tf.paragraphs[-1]
        if p.runs:
            p.runs[0].text += '\n' + '\n'.join(lines[len(tf.paragraphs):])


def replace_in_slide(slide, old, new):
    for sh in slide.shapes:
        if not sh.has_text_frame:
            continue
        for p in sh.text_frame.paragraphs:
            for r in p.runs:
                if old in r.text:
                    r.text = r.text.replace(old, new)


def clone_slide(template):
    new = prs.slides.add_slide(template.slide_layout)
    for sh in list(new.shapes):
        sh._element.getparent().remove(sh._element)
    for sh in template.shapes:
        if sh.has_text_frame or sh.has_table:
            new.shapes._spTree.append(copy.deepcopy(sh._element))
    return new


def fill_slide(slide, texts):
    """Assign texts to the slide's NON-EMPTY text shapes, in order."""
    targets = [sh for sh in slide.shapes
               if sh.has_text_frame and sh.text_frame.text.strip()]
    assert len(targets) == len(texts), (len(targets), len(texts))
    for sh, t in zip(targets, texts):
        set_shape_text(sh, t)


# ---------- new slides ----------
agenda = clone_slide(by_old[19])  # 13 non-empty shapes
fill_slide(agenda, [
    'The next hour',
    'FOOTER',
    'The problem',
    'Large, edited, shared sequences break plain strings and plain hashes.',
    'The structure',
    'A rope with a fingerprint on every node: logarithmic edits, an always-current identity, every old version still valid.',
    'The demos',
    'Python and TypeScript live, then five minutes to run it yourself on the playground or the notebook.',
    'The evidence',
    'One conformance corpus grading four languages, and the ICTAI 2026 measurements, including the ones hashrope loses.',
    'The uses',
    'Verified sequences in editors, sync, caches, genomics, and AI agent memory.',
    'Questions throughout. Discussion at the end, with three questions worth arguing about.',
])

hands = clone_slide(by_old[15])  # 9 non-empty shapes
fill_slide(hands, [
    'Your turn: run it yourself',
    'FOOTER',
    'Open the playground\nhashrope.lovable.app: type into A and B, pick an operation, and watch the real tree redraw from the published npm package.',
    'Or run the notebook\nThe Colab notebook (Get started slide) runs the Python and npm packages side by side in under a minute, outputs saved.',
    'Three things to try\nEdit one byte and watch the root fingerprint change. Build the 2^60 repeat and read its fingerprint. Make the collision pair collide, then settle it with rope_equal.',
    'Compare with a neighbor\nSame bytes must give the same fingerprint in every language. If your number differs from your neighbor\u2019s, find out why before trusting either.',
    '',
    '',
    'Five minutes. The demo rope stays on screen; shout if your fingerprint disagrees with mine.',
])

disc = clone_slide(by_old[11])  # 15 non-empty shapes
fill_slide(disc, [
    'Discussion: three questions worth arguing',
    'FOOTER',
    '1',
    'When is a fingerprint enough?\nVerification by one comparison is a probability statement. Where in your own projects would you accept it, and where do you need the exact APIs or SHA-256?',
    'probability vs proof',
    '2',
    'Persistence or copying?\nAgent memory forks by sharing structure. In a system that keeps every version, what breaks first: memory, bookkeeping, or your ability to reason about it?',
    'every version kept is a version you can roll back to',
    '3',
    'What should the fifth language be?\nThe conformance corpus grades any port against one pinned oracle. Which language would you add next, and what would it have to prove?',
    'one oracle grades them all',
    '',
    '',
    '',
    'No slides for this part. Argue. The paper, and the benchmarks hashrope loses, are in the repository if you want ammunition.',
])

ledger = clone_slide(by_old[11])  # 15 non-empty shapes
fill_slide(ledger, [
    'Backup: the verification ledger',
    'FOOTER',
    '1',
    'Oracles\nWhole-string token IDs across three tokenizer families; byte-level scans; fork materialization; token oracles on the live stack. Every oracle comparison in the paper returned zero mismatches.',
    'zero mismatches, every study',
    '2',
    'Guards\nDeterministic structural bounds, std = 0: fork spine at most ceil(log2 w) + 3 nodes; identification in exactly 2 ceil(log2 N) steps; flatten performs zero splits, re-allocations and re-hashes.',
    'std = 0, deterministic',
    '3',
    'Negative controls\nInjected faults prove the gates can fail: a bit-flip on the maintained hash fails the gate; fixed-byte chunking drifts at token 1800 and leaves six invalid UTF-8 leaves; 105 of 105 corrupted cache entries caught at the exact position.',
    'injected faults, caught',
    '',
    '',
    '',
    'Source: IEEE ICTAI 2026 paper, Table III and Section III. Every claim is paired with an oracle and a control that can fail.',
])

# ---------- reorder ----------
order = [by_old[1], agenda,
         by_old[2], by_old[3], by_old[4], by_old[5], by_old[6], by_old[7],
         by_old[8], by_old[9], by_old[10], hands,
         by_old[11], by_old[12], by_old[13], by_old[14], by_old[22], by_old[23],
         by_old[15], by_old[16], by_old[17], by_old[18], by_old[19], disc,
         by_old[20], by_old[21], ledger]
sldIdLst = prs.slides._sldIdLst
elem_of = {id(s): e for s, e in zip(prs.slides, list(sldIdLst))}
for e in list(sldIdLst):
    sldIdLst.remove(e)
for s in order:
    sldIdLst.append(elem_of[id(s)])

final = list(prs.slides)
assert len(final) == 27, len(final)

# ---------- footers + text edits ----------
MAIN = 25
for pos, s in enumerate(final, 1):
    if pos <= MAIN:
        footer = f'hashrope  |  ACM Chapter Talk  |  {pos} / {MAIN}'
    else:
        footer = f'hashrope  |  ACM Chapter Talk  |  backup {pos - MAIN} / 2'
    for sh in s.shapes:
        if sh.has_text_frame and (sh.text_frame.text.strip().startswith('hashrope  |')
                                  or sh.text_frame.text.strip() == 'FOOTER'):
            set_shape_text(sh, footer)

replace_in_slide(final[0], 'DevFest Florida 2026  |  hackathon session',
                 'ACM Chapter Talk  |  Friday, November 20, 2026')
replace_in_slide(final[20], 'Hackathon recipes: four patterns you can ship this weekend',
                 'Recipes: four patterns you can ship')
replace_in_slide(final[24], 'github.com/jemsbhai/hashrope',
                 'github.com/jemsbhai/hashrope-acm-talk')
replace_in_slide(final[24], 'Colab demo and cheat sheet: scan on the previous slide',
                 'Colab demo and cheat sheet: see the Get started slide')
# promoted backups lose their "Backup:" title prefix (positions 17 and 18)
replace_in_slide(final[16], 'Backup: when the specialist wins', 'When the specialist wins')
replace_in_slide(final[17], 'Backup: what prefix reuse is worth on real hardware',
                 'What prefix reuse is worth on real hardware')

prs.save(SRC)
print('saved; slides:', len(final))
for pos, s in enumerate(final, 1):
    title = ''
    for sh in s.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            title = sh.text_frame.text.strip().split('\n')[0][:62]
            break
    print(pos, '|', title)
