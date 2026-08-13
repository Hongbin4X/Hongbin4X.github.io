# Homepage Publications Update

## Scope

Update the homepage News for HPFA and StackPlanner and the HPFA publication card without changing the existing layout or styles.

## Content changes

- Add HPFA as the newest publication card, using `images/publication4.jpg`.
- Present HPFA as accepted by COLM 2026 and retain the `Co-first Author` contribution label.
- Add a July 2026 news item announcing the HPFA acceptance.
- Present StackPlanner as submitted to EMNLP 2026 and under review in News only.
- Retain `Co-author` for StackPlanner; do not describe it as co-first-authored.
- Use the full title `HPFA: Hypergraph-Based Paired Failure Attribution for LLM Reasoning`.
- Do not add an HPFA paper URL because none was provided.

## Presentation

Follow the existing paper-card markup. Order the publication cards with HPFA first, followed by MolRecBench-Wild and Efficient Graph Continual Learning. Keep StackPlanner out of Publications.

## Verification

- Build the Jekyll site successfully.
- Check the generated homepage for the COLM card, `publication4.jpg`, EMNLP under-review wording, and correct author-role labels.
- Confirm the old ACL 2026 StackPlanner wording is absent.
