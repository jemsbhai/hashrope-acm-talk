# Hashrope: One Data Structure, Four Languages

Talk materials for the ACM chapter talk by **Muntaser Syed** (Researcher and PhD Candidate, Florida Institute of Technology), invited by Dr. Marius Silaghi.

## Summary

Persistent sequences across Python, Rust, Java, and TypeScript, with live demos and cross-language conformance. Hashrope is a persistent rope data structure with content hashing: exact comparison, structural sharing, and cheap forking, shipped as one specification in four languages on a single version line.

Logarithmic edits, one comparison to verify a copy, four languages on one version line.

## Materials

- `hashrope-acm-talk.pptx` / `hashrope-acm-talk.pdf` — slide deck (20 slides + 3 backup)
- `hashrope_demo.ipynb` — companion demo notebook: edit, verify, and locate in Python; same bytes, same fingerprint in TypeScript

## Links

- Interactive demo: https://hashrope.lovable.app
- Code: https://github.com/jemsbhai/hashrope
- Packages (all 0.3.4): PyPI, npm, crates.io, Maven Central

## Provenance

This deck is the DevFest Florida 2026 talk ("Hashrope: One Data Structure, Four Languages", Nov 7, 2026), adapted for the ACM chapter audience. The research results slide draws on the IEEE ICTAI 2026 paper "Hashrope: A Persistent Data Structure for Mechanisms of LLM Context Management".

Recording of the DevFest Florida talk: https://youtu.be/S2hAXooVOQQ

## License

MIT
