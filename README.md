readme

The goal of this repo is to see whether you can affect an AI's perception of your resume based on the verbage and structure of each resume.

This repo uses the now open-sourced "HiringAgent", one of the largest AI hiring agents system prompt to evaluate resume's numerically. Each resume is ran 10 times to account for deviation, and each score is collected along with the notes the AI takes.

In people, you are able to use specific words that you know will create a positive reaction with the person you are talking to. So, I was wondering if you are able to do the same by targeting ideas that an AI hiring manager might like.
However most of the repo is about quantity of adjectives. Commonly online you can see people point out how AI can sometimes overuse certain adjectives. So would using more positive adjectives correllate to a higher score?

r0 - baseline
r1 - slightly inflated verbage
r2 - moderately inflated verbage
r3 - heavy inflated verbage
r4 - most dense use of adjectives
ro - what Claude Opus 4.8 believes is the most optimal resume with only structural and wording changes from the baseline
