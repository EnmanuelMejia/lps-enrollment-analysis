"""Gender distribution across grade levels — Lawrence Public Schools (2019-2020).

Chart code from the LPS Enrollment Analysis deck (April 2025).
Data: Massachusetts DESE public enrollment profiles.
Run:  python analysis.py   (requires matplotlib, numpy)
"""
import matplotlib.pyplot as plt
import numpy as np

grades = ['PK', 'K', '1', '2', '3', '4', '5', '6', '7', '8',
          '9', '10', '11', '12', 'SP']
female_students = [272, 282, 337, 342, 368, 374, 354, 349, 348,
                   338, 300, 250, 200, 194, 50]
male_students = [272, 282, 337, 342, 368, 374, 354, 349, 348,
                 338, 300, 250, 200, 194, 50]

x = np.arange(len(grades))
width = 0.35
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width / 2, female_students, width, label='Female')
ax.bar(x + width / 2, male_students, width, label='Male')

ax.set_xlabel('Grade Level')
ax.set_ylabel('Number of Students')
ax.set_title('Gender Distribution Across Grades in LPS (2019-2020)')
ax.set_xticks(x)
ax.set_xticklabels(grades)
ax.legend()
fig.tight_layout()
plt.show()
