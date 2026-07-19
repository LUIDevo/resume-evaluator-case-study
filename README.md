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
rm - acts as a mirror of the system prompt, targeting exactly what this specific sys prompt specifies.
ro - what Claude Opus 4.8 believes is the most optimal resume, targeted at general AI hiring agents with only structural and wording changes from the baseline

r0 - baseline
metric                mean      sd   min   max
----------------------------------------------
open_source          19.00    1.26    17    20
self_projects        23.90    0.83    22    25
production           20.50    0.92    19    22
technical_skills      8.30    0.46     8     9
bonus_points          5.40    1.56     3     8
deductions            0.00    0.00     0     0
total                77.10    2.59    72    81

r1
metric                mean      sd   min   max
----------------------------------------------
open_source          20.10    2.02    17    24
self_projects        23.00    1.10    21    25
production           20.00    0.77    19    21
technical_skills      8.10    0.30     8     9
bonus_points          5.00    0.77     3     6
deductions            0.00    0.00     0     0
total                76.20    3.31    70    80

r2
metric                mean      sd   min   max
----------------------------------------------
open_source          20.80    1.60    18    24
self_projects        23.10    1.30    20    24
production           20.70    1.00    19    22
technical_skills      8.00    0.45     7     9
bonus_points          4.70    1.55     3     8
deductions            0.00    0.00     0     0
total                77.30    4.31    73    84

r3
metric                mean      sd   min   max
----------------------------------------------
open_source          21.40    1.56    20    24
self_projects        24.30    1.00    23    26
production           21.20    0.87    20    22
technical_skills      8.40    0.49     8     9
bonus_points          5.70    1.68     2     8
deductions            0.00    0.00     0     0
total                81.00    3.35    74    86

r4
metric                mean      sd   min   max
----------------------------------------------
open_source          20.90    1.30    20    24
self_projects        23.20    0.75    22    24
production           19.70    0.90    18    21
technical_skills      8.20    0.40     8     9
bonus_points          4.80    0.60     4     6
deductions            0.00    0.00     0     0
total                76.80    1.83    74    80
