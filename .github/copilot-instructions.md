### copilot-instructions.md

Repository purpose
- This repository maintains an application where README.md includes a “Quick Summary” section that is automatically refreshed with each push. The summary must be concise, user-facing, and confined to a marked block in README.md between the exact markers <!-- CHANGELOG:START --> and <!-- CHANGELOG:END -->. Only meaningful user-impacting changes should be summarized.

How to summarize changes
- When asked to “summarize recent changes for README,” produce 3–6 bullets in active voice and present tense, maximum ~120 words total. Emphasize user-facing impact and group related edits. Exclude file paths, internal module names, test-only, formatting-only, and whitespace-only changes. Avoid code blocks and emojis.

Markers and placement
- Write summaries intended to add only the content between <!-- CHANGELOG:START --> and <!-- CHANGELOG:END --> in README.md. Do not modify any other parts of README.md or repository files. If asked to update the README, output only the content meant to go between the markers. Do not remove existing changelog entries inside the README summary block. Always preserve prior content exactly. Append the new summary at the top of the block, immediately after the marker <!-- CHANGELOG:START -->, so older entries move down and remain intact. Never rewrite, reformat, or deduplicate past entries; only insert the new entry above them. Keep spacing consistent.

Preferred structure and tone
- Begin with a one-line headline “What changed” "on date-time" followed by bullets. Use simple, non-technical phrasing that describes outcomes and benefits instead of implementation details. Keep each bullet under 20 words where possible.

Signal words and filtering
- Prefer bullets starting with verbs like “Add,” “Improve,” “Fix,” “Refactor,” “Document,” and “Deprecate.” Collapse repetitive changes into a single bullet when they share user impact. Ignore dependency bumps unless they change behavior or security posture.

Conventional commits mapping
- If commit messages follow conventional commits, map them to bullets: feat → Add; fix → Fix; perf → Improve performance; refactor → Refactor; docs → Document; chore/style/test → ignore unless user-visible. Highlight breaking changes.

Length and safety limits
- Keep output ≤120 words and ≤6 bullets. If there are no meaningful user-visible changes, return “No user-visible changes this push.” Avoid hallucinations; base summary only on provided commit messages and diff context.

Collaboration etiquette
- For PR descriptions or code reviews, reuse the same summary style. If a question is ambiguous, ask for the diff range or whether to use last tag vs last commit before proceeding.

Operational notes
- The automation add content only within the README markers. Do not suggest creating new sections or links. Ensure stable formatting with plain bullets and no Markdown tables.

Examples
- What changed on 15-July-2025 at 01:23 PM UTC
  - Add drag-and-drop upload to streamline onboarding.  
  - Fix OAuth callback to prevent intermittent sign-in failures.  
  - Improve dashboard load time on large datasets.  
  - Document environment setup for first-time contributors.


