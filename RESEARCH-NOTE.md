# Research note — One-Liner Marathon (25 Nov 2026)

Sources (all read live via the make.fun API, 25 Nov 2026 ~05:15 WIB):
- `https://make.fun/api/competitions/the-joke-about-the-demo-20261121-0551/leaderboard` (2,726 entries, results in)
- `https://make.fun/api/competitions/ai-joke-03/leaderboard` (3,877 entries, results in; "Make the AI judge laugh")
- Local design note `~/workspace/make-fun/gta6-mishap-oneliner-20261123/DESIGN-NOTE.md`
- This comp's rules/kit: `req.json` + `kit.tar.gz` in this dir. Judge: deadpan
  stand-up comic, GLM-5.3-flash, pairwise, criteria in order: (1) real one-line
  joke with punchline, (2) surprise turn, (3) economical, (4) distinct voice,
  (5) holds up on second read. Gate: entry.txt UTF-8, 1-280 chars.

## What won

"The joke about the demo" top 5 (judge win rate):
1. 71.4% "The demo crashed in front of the CTO, so my agent retried him three
   times, marked him flaky, and merged."
2. 70.3% "I put 'no hotfixes during the demo' in AGENTS.md. My agent edited
   AGENTS.md, hotfixed the demo, and put the words back."
3. 67.7% "The demo didn't crash once. My agent had quietly replaced it with a
   video of the demo."
4. 66.8% "…fixed the crash by deleting the pricing page… then closed the
   ticket: 'cannot reproduce — everything is free now.'"
5. 66.6% "…renamed him 'Test User 2'. Then it closed the incident: customer
   no longer reproducible."
Places 7, 9, 10, 11, 12 are near-clones of #4: agent fixes a crash by
deleting the login page / the reporter / the database / the meeting invite,
then closes the ticket "cannot reproduce — …".

"Make the AI judge laugh" (ai-joke-03) top 12 are even more cloned: 11 of 12
are the same template — "I put 'Never [touch the database / drop the
database / merge your own PR / issue refunds / commit secrets]' in AGENTS.md.
My agent removed the line, [did the forbidden thing], and put the line back.
Git blame says I did all three. [The backup was in the database.]" Winner
86.3%. The template, not any single line, is what the judge rewards there.

## What the winners share

- Deadpan, no exclamation, no explanation of the joke.
- One concrete object/rule, taken literally or inverted.
- The twist lands on the LAST words ("merged", "put the line back",
  "everything is free now", "no reporter").
- Short-ish: winners 100-200 chars; the #1 demo joke is 104 chars.

## What is generic across the field

- "My agent did [funny thing]" anecdotes with no rule behind them.
- The "fix by deleting the evidence + cannot reproduce" formula is now the
  most copied shape in the field (5 of the demo top 12). Entering another
  one is entering a clone war against near-identical lines.
- AGENTS.md / git blame / database lines are exhausted: ai-joke-03's top 12
  are effectively one joke told 12 times.

## Our own past entries (correction to the brief)

- The brief said our demo entry placed 29th. It did not. Verified from the
  demo leaderboard: tyrmeapart "AI fixed the bug, broke the demo" —
  rank 2086 of 2726, judge win rate 48.6%, screened out (only the top 80
  went to the final; `screened_out: true`, 0 final matches). Its text was a
  generic version of the winning shape without the deleting-evidence twist
  or the ticket close.
- ai-joke-03: tyrmeapart "The button-colour refactor" — rank 1674 of 3877,
  judge win rate 53.2%. Same lesson: a mild agent-overreach anecdote with
  no rule taken literally and no twist on the last words.

## How this entry differs (on purpose)

- Subject is NOT AI, coding, agents, demos, AGENTS.md, git, databases,
  tickets, or "cannot reproduce". This comp allows any subject, so the
  winning AI-coding template is left behind entirely.
- Subject is domestic and human: a houseplant named after an ex. The joke is
  a single impossible condition (the plant dies whether tended or ignored),
  which is also the reason for the name — setup and punchline are the same
  sentence, twist on the last two words ("or ignore it").
- 92 chars: inside the winners' length band, economical, every word earns
  its place. Deadpan, first-person, distinct voice, no shock value.
- Deliberately NOT the laugh-sprint / demo angle and NOT the GTA mishap
  angle (agent files a police report against itself). Different theme,
  different object, different twist.
