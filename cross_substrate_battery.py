"""
ETPT Cross-Substrate Task Battery
=================================
Tests the ETPT-unique prediction: the rank-order of human-vs-Claude agreement
across visual task types should correlate (Spearman rho) with the rank-order
of the architecture-derived competence-overlap vector.

This file does three things:
  1. Defines a concrete, scorable task battery (10 dimensions x N items each)
  2. Provides the scoring + Spearman machinery
  3. Runs a SIMULATED pilot using ETPT's own predictions as the data-generating
     process, so you can see the analysis pipeline end-to-end before collecting
     real human + model responses.

To run for real: replace `simulate_responses()` with
  - human_answers: collected from a human panel (n>=20)
  - claude_answers: collected via the vision API on the same images
and feed both into `agreement_by_dimension()`.

Author: S R Tulasi Krishna
"""
import numpy as np
from scipy.stats import spearmanr, pearsonr

# ----------------------------------------------------------------------
# 1. THE TEN DIMENSIONS + architecture-derived competence priors
#    (same vectors as intelligibility_vision.py — kept consistent)
# ----------------------------------------------------------------------
DIMS = [
    "object_id", "scene_semantics", "text_reading", "counting",
    "spatial_metric", "motion_temporal", "depth_3d", "color_discrim",
    "local_detail", "global_gist",
]
human  = np.array([0.90,0.85,0.55,0.80,0.90,0.95,0.90,0.85,0.60,0.90])
claude = np.array([0.88,0.92,0.85,0.30,0.35,0.10,0.40,0.65,0.55,0.88])

overlap = human * claude
overlap_norm = overlap / overlap.max()

# ----------------------------------------------------------------------
# 2. THE TASK BATTERY
#    Each dimension gets concrete item TEMPLATES with an objective ground
#    truth, so human and model answers can both be scored against truth,
#    and agreement = (both correct) or (both wrong in the same way).
# ----------------------------------------------------------------------
BATTERY = {
    "object_id": [
        "Name the primary object in the image.",
        "Is there an animal present? (yes/no)",
        "Name all distinct object categories visible.",
    ],
    "scene_semantics": [
        "In one sentence, what is happening in this scene?",
        "What is the mood/emotional tone of this image?",
        "What is the likely location/setting?",
    ],
    "text_reading": [
        "Transcribe all text visible in the image.",
        "What does the largest text say?",
        "Read the smallest legible text in the image.",
    ],
    "counting": [
        "Exactly how many people are in the image?",
        "Count the number of distinct circular objects.",
        "How many windows are visible on the building?",
    ],
    "spatial_metric": [
        "Which object is closer to the left edge: A or B?",
        "Is the lamp to the left or right of the chair?",
        "Order the three objects from nearest to farthest from the camera.",
    ],
    "motion_temporal": [
        "Which direction is the subject moving?",
        "Is the object accelerating, decelerating, or steady?",
        "What happened immediately before this frame?",
    ],
    "depth_3d": [
        "Which of the two marked objects is in front?",
        "Estimate relative depth ordering of all foreground objects.",
        "Is the surface receding toward or away from the viewer?",
    ],
    "color_discrim": [
        "Name the exact color of the marked region.",
        "Which of these two near-identical shades is darker?",
        "Is the lighting warm or cool toned?",
    ],
    "local_detail": [
        "Describe the texture of the marked surface.",
        "What fine detail appears in the top-right 5% of the image?",
        "Is there a small flaw/mark on the object?",
    ],
    "global_gist": [
        "Indoor or outdoor?",
        "Natural or man-made environment?",
        "Daytime or nighttime?",
    ],
}

# ----------------------------------------------------------------------
# 3. SCORING
#    agreement_rate[d] = fraction of items in dimension d where human and
#    Claude give the SAME answer (regardless of correctness — we measure
#    agreement, which is what the intelligibility tensor predicts).
# ----------------------------------------------------------------------
def agreement_by_dimension(human_answers, claude_answers):
    """
    human_answers, claude_answers: dict[dim] -> list[str] (parallel, per item)
    returns: np.array of agreement rate per dimension (order = DIMS)
    """
    rates = []
    for d in DIMS:
        h = human_answers[d]; c = claude_answers[d]
        same = sum(1 for a, b in zip(h, c) if _match(a, b))
        rates.append(same / len(h))
    return np.array(rates)

def _match(a, b):
    """Lenient string match for categorical/short answers."""
    return a.strip().lower() == b.strip().lower()

# ----------------------------------------------------------------------
# 4. SIMULATED PILOT
#    Data-generating process: agreement on dimension d is drawn around the
#    ETPT-predicted overlap_norm[d]. This is the OUTCOME ETPT predicts; the
#    real experiment tests whether nature actually behaves this way.
# ----------------------------------------------------------------------
def simulate_responses(n_items_per_dim=12, noise=0.10, seed=11):
    rng = np.random.default_rng(seed)
    human_answers, claude_answers = {}, {}
    for di, d in enumerate(DIMS):
        p_agree = np.clip(overlap_norm[di] + rng.normal(0, noise), 0.02, 0.99)
        h, c = [], []
        for _ in range(n_items_per_dim):
            truth = rng.integers(0, 4)  # 4-way categorical toy answer
            h_ans = truth  # assume human ~ ground truth for this toy model
            # Claude agrees with prob p_agree, else picks a different answer
            if rng.random() < p_agree:
                c_ans = truth
            else:
                c_ans = (truth + rng.integers(1, 4)) % 4
            h.append(str(h_ans)); c.append(str(c_ans))
        human_answers[d] = h; claude_answers[d] = c
    return human_answers, claude_answers

# ----------------------------------------------------------------------
# 5. RUN
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("="*66)
    print("ETPT CROSS-SUBSTRATE BATTERY  —  simulated pilot")
    print("="*66)
    print(f"\n{sum(len(v) for v in BATTERY.values())} item templates across "
          f"{len(DIMS)} dimensions (scale up to ~12 items/dim for real run)\n")

    h_ans, c_ans = simulate_responses(n_items_per_dim=12)
    measured = agreement_by_dimension(h_ans, c_ans)

    print(f"{'dimension':16s} {'predicted':>10s} {'measured':>10s}")
    print("-"*40)
    order = np.argsort(-overlap_norm)
    for di in order:
        print(f"{DIMS[di]:16s} {overlap_norm[di]:>10.3f} {measured[di]:>10.3f}")

    rho, p_rho = spearmanr(overlap_norm, measured)
    r, p_r = pearsonr(overlap_norm, measured)

    print("\n" + "="*66)
    print("THE TEST")
    print("="*66)
    print(f"Spearman rho (rank agreement)  = {rho:.3f}   (p = {p_rho:.4f})")
    print(f"Pearson  r   (linear agreement) = {r:.3f}   (p = {p_r:.4f})")
    print(f"""
INTERPRETATION
  rho > 0.6, p < 0.05  -> ETPT's tensor predicted the GEOMETRY of agreement,
                          not just the direction. Beats "architectures differ."
  rho ~ 0              -> ETPT added nothing beyond generic inductive-bias talk.

This simulated run uses ETPT's own prediction as the data generator, so a high
rho here only confirms the PIPELINE works. The real result comes from feeding in
measured human-panel + vision-API answers on a shared image set.
""")

    # Also report which dimension is the LARGEST engineerable gap
    gap = human - claude
    g_order = np.argsort(-gap)
    print("ENGINEERABLE GAP RANKING  (human competence minus Claude competence)")
    print("-"*60)
    print("  -> this is the prescriptive output: which missing channel to")
    print("     engineer into the model first, ranked by deficit size.\n")
    for di in g_order:
        if gap[di] > 0:
            bar = "#" * int(gap[di] * 40)
            print(f"  {DIMS[di]:16s}  gap={gap[di]:+.2f}  {bar}")
