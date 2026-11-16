# Hashrope: One Data Structure, Four Languages

Talk materials for the ACM chapter talk by **Muntaser Syed** (Researcher and PhD Candidate, Florida Institute of Technology), invited by Dr. Marius Silaghi.

## Summary

Persistent sequences across Python, Rust, Java, and TypeScript, with live demos and cross-language conformance. Hashrope is a persistent rope data structure with content hashing: exact comparison, structural sharing, and cheap forking, shipped as one specification in four languages on a single version line.

Logarithmic edits, one comparison to verify a copy, four languages on one version line.

## Materials

- `hashrope-acm-talk.pptx` / `hashrope-acm-talk.pdf` — slide deck for the one-hour slot: 25 slides + 2 backup, with full speaker notes timed to 60 minutes
- `TALK_PLAN.md` — the hour, slide by slide, with timings and flex points
- `hashrope_demo.ipynb` — companion demo notebook: edit, verify, and locate in Python; same bytes, same fingerprint in TypeScript. [Open it in Colab](https://colab.research.google.com/github/jemsbhai/hashrope-acm-talk/blob/master/hashrope_demo.ipynb)

## Links

- Interactive demo: https://hashrope.lovable.app
- Code: https://github.com/jemsbhai/hashrope
- Packages (all 0.3.4): PyPI, npm, crates.io, Maven Central

## Provenance

This deck is the DevFest Florida 2026 talk ("Hashrope: One Data Structure, Four Languages", Nov 7, 2026), expanded from 30 minutes to a full hour for the ACM chapter: an agenda slide, a hands-on segment, the two research-depth slides promoted from backup, a closing discussion, and speaker notes retimed to 60 minutes. The research results draw on the IEEE ICTAI 2026 paper "Hashrope: A Persistent Data Structure for Mechanisms of LLM Context Management".

Recording of the DevFest Florida talk: https://youtu.be/S2hAXooVOQQ

## License

MIT
