"""Original conceptual diagrams, saved as vector PDF and high-resolution PNG."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'figs'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'savefig.facecolor': 'white', 'text.color': '#203746'})

def save(fig, name):
    fig.savefig(OUT / f'{name}.png', dpi=190, bbox_inches='tight')
    fig.savefig(OUT / f'{name}.pdf', bbox_inches='tight')
    plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 4.9))
ax.set(xlim=(0, 10), ylim=(0, 6)); ax.axis('off')
boxes = [(0.4, 3.4, 'Physical question', 'Observable · regime · precision'),
         (5.6, 3.4, 'Representation', 'State · field · distribution'),
         (5.6, .6, 'Learning and calculation', 'Data · laws · objective'),
         (.4, .6, 'Independent evidence', 'Limits · baselines · measurements')]
for x, y, title, body in boxes:
    ax.add_patch(FancyBboxPatch((x, y), 4, 1.5, boxstyle='round,pad=.12',
                               facecolor='#edf5f4', edgecolor='#157a83', linewidth=1.5))
    ax.text(x+2, y+1.02, title, ha='center', weight='bold', fontsize=12)
    ax.text(x+2, y+.48, body, ha='center', fontsize=9.7)
for a, b in [((4.55, 4.15), (5.4, 4.15)), ((7.6, 3.2), (7.6, 2.3)),
             ((5.4, 1.35), (4.55, 1.35)), ((2.4, 2.3), (2.4, 3.2))]:
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=18,
                                 color='#157a83', linewidth=1.6))
ax.text(5, 5.55, 'Learning belongs inside a scientific cycle', ha='center',
        fontsize=16, weight='bold')
ax.text(5, 2.75, 'Physical assumptions guide every stage', ha='center',
        fontsize=10, color='#65737b')
save(fig, 'learning-cycle')

fig, ax = plt.subplots(figsize=(9, 4.2))
ax.set(xlim=(0, 10), ylim=(0, 5)); ax.axis('off')
rows = [(3.6, 'I · Foundations', 'Probability → inference → networks → optimization → validation'),
        (2.6, 'II · Quantum matter', 'States → neural ansätze → VMC → dynamics → fermions & open systems'),
        (1.6, 'III · Physical models', 'Generative models → symmetry → operators → PDEs → simulation'),
        (.6, 'IV · Discovery', 'Inverse problems → experiments → equations → frontiers → projects')]
for y, title, desc in rows:
    ax.add_patch(FancyBboxPatch((.15, y-.15), 9.7, .82, boxstyle='round,pad=.08',
                               facecolor='#f0f5f7', edgecolor='#9ab4bd'))
    ax.text(.4, y+.31, title, va='center', fontsize=11.5, weight='bold')
    ax.text(.4, y-.005, desc, va='center', fontsize=9.4)
ax.text(5, 4.7, 'One language, four connected routes', ha='center', fontsize=16, weight='bold')
save(fig, 'curriculum')
