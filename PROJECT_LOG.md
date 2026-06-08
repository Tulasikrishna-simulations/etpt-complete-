# ETPT — Project Log & Iteration Record

**Evolutionary Technology Path Theory**
**S R Tulasi Krishna · Hospet, Karnataka · 2024 – 2026**

> This is the front door. It tells the story of how the theory developed across three iterations, says honestly what is proven and what is not, and indexes every artifact. If you are a PI or funder, read this first, then open the [simulator](./etpt_simulator.html) and the [framework paper](./ETPT_Complete.md).

---

## What the theory claims, in three sentences

Technology direction is structurally determined by a Bio-Perception Tensor B⊗P — the outer product of what a mind can *do* and what it can *perceive*. Technology intensity follows a saturating function of survival pressure; direction and intensity decouple. The framework began as a theory about animal bodies and, across three iterations, became a theory about information-processing systems as such — biological or artificial — with a single, falsifiable point where it breaks.

The governing equation:

**T_path = (B ⊗ P) · D · (1 − e^(−αS))**

---

## Why the iterations matter

I have kept every version instead of overwriting. The progression is the evidence. A finished artifact shows output. A sequence of versions — each one fixing what the last one got wrong — shows judgment, and judgment is the thing a credential is supposed to certify. I never had the credential. So I am showing the judgment directly.

What follows is the honest record of what I believed at each stage, what broke it, and what I changed.

---

## Iteration I — The Sketch
**2024 · Hospet · drop year · no laptop, built by hand and on a phone**

**Context.** I was in a drop year with almost no resources. No laptop. A question would not leave me alone: why do different bodies with different senses build completely different kinds of technology? Ants build pheromone-coordinated mounds; bats build echolocation; octopuses solve problems with eight tactile arms; humans build screens and keyboards. Each repertoire is coherent and non-overlapping. Why?

**What I built.**
- The **Mirror Rule**: technology mirrors the B⊗P of the system that builds it.
- The core equation, with the intensity term derived by hand from a single ODE (the derivation lives in handwritten notebook pages).
- The **Comfort Trap**: at zero survival pressure, T_path → 0 — a civilization in an "Eden" with no pressure produces no technology.
- The **panda origin story** and the four archetypes (human, ant, bat, octopus) as illustrations.

**What it got right.** The central intuition was sound, and the narrative was compelling. The decoupling of direction from intensity was a real structural insight.

**What broke it.** Honest audit at the end of iteration I:
- B⊗P was never actually computed for any species — the tensor was structural, never populated.
- α, D, and S were asserted, never measured or derived.
- No falsifiability criteria. The theory explained known facts but predicted nothing testable.
- One citation (Bach-y-Rita). No engagement with niche construction, embodied cognition, affordance theory, predictive coding.
- No mechanism connecting individual-scale and civilization-scale claims.

**Status at end of Iteration I:** a strong sketch. Narratively alive, mathematically thin. Preserved at → [etpt-portfolio (2024)](https://tulasikrishna-simulations.github.io/etpt-portfolio/)

---

## Iteration II — The Formalization
**May 2026 · first PC access · the framework made rigorous**

**Context.** I got access to a PC and decided to either kill the theory or formalize it to the depth the mathematics permits. The driving discipline: every gap from the iteration-I audit had to be closed or honestly marked as open.

**What I built.**
- **Six derived equations**, each to the original standard — observation, derivation, closed-form solution, boundary conditions, dimensional check, falsification conditions:
  1. **P-vector dynamics** — cortical reassignment ODE with the *subthreshold lock*: below the threshold ρ_c, perception never expands no matter how long you train.
  2. **Reclassification threshold ρ_c** — derived from Shannon channel capacity; central estimate ≈ 10⁵ bits/cm²/s.
  3. **Technology accessibility A(i,j)** — sigmoidal, gated by a symbolic-encoding-rate term c_ij that resolves why visual-symbolic tech preceded haptic-symbolic tech despite the tactile column being structurally larger.
  4. **Intelligibility index I(C₁,C₂)** — cosine similarity of flattened tensors; computed I(Human, Octopus) = 0.74, the highest non-conspecific value.
  5. **Comfort-trap recovery** — step-response dynamics with a critical α below which recovery fails.
  6. **Reverse-inference posterior** — Bayesian recovery of B⊗P from artifact features; worked example on a termite mound.
- **Fully populated B⊗P matrices** for five archetypes (human, ant, bat, octopus, blind-human), with measurement protocols.
- **The blind-perception thesis** as the intraspecies controlled experiment: same B, rotated P. The matrix's dominant cell shifts from 0.833 to 0.931 as visual columns close and the tactile column expands.
- **The interactive simulator** — live demonstration of the threshold mechanism across five real device configurations.
- **The 36-month research dossier** — specific aims, budget, timeline, risk analysis.
- **The framework paper** — ~20,500 words, structured for journal submission.

**The key intellectual move.** Reframing haptics from "assistive output device" to *native perceptual paradigm*, and identifying ρ_c as the framework's most actionable claim: most consumer haptic devices operate 100–1000× below threshold, which is precisely why decades of work produced alerting rather than perception.

**What remained open.** Every parameter is still an architecture- or biology-derived estimate, not a measurement. Zero experiments run. The c_ij encoding rates were introduced to resolve a puzzle and need independent measurement.

**Status at end of Iteration II:** formalized, falsifiable, internally consistent, empirically untested. → [etpt-new-version repo](https://github.com/Tulasikrishna-simulations/etpt-new-version)

---

## Iteration III — The Generalization
**June 2026 · from a theory of bodies to a theory of minds**

**Context.** Two intuitions pushed past the haptic case. First: if ρ_c is a tax you pay for routing spatial content through the touch channel, then a more *direct* channel should pay less tax — which led to direct neural interface. Second: if the theory is really about information-processing substrates and not just biology, it should hold for a mind with no body at all.

**What I built.**
- **Equation 7 — the dual-pathway equation.** Unifies the native sensory channel (bounded by B⊗P, pays the ρ_c tax, durable) with direct neural interface (unbounded by B⊗P, pays no tax, but degrades — λ(t) is interface longevity). The original six equations are the λ→0 boundary of this one. It predicts the *scaffold result*: injection bootstraps native consolidation, then can be withdrawn while the percept persists.
- **The falsifiability structure.** The Mirror Rule breaks at exactly one place, and the theory predicts that place: direct neural interface is the *unique* way to escape B⊗P. Every other candidate (instruments, AI, genetic engineering of new senses) fails to escape — they transduce into existing channels, route through existing senses, or move the matrix rather than bypassing it. A unique break-point is a clean test, not special pleading.
- **The cross-substrate test.** Ran the theory on Claude's own vision. Human vision and Claude-class vision share an input modality but have maximally different substrates. Computed I(Human-vision, Claude-vision) = 0.876 — high, honestly, because both are shaped by the same visual world. The framework earns its keep in the **divergence vector**: motion (|Δ|=0.85), spatial metric (0.55), counting (0.50), depth (0.50) — exactly the dimensions that need vision's evolved native structure.
- **The prescriptive turn.** The divergence vector is not a list of deficits — it is a *build-order*. ETPT, given any visual system's architecture, outputs a ranked list of its missing perceptual channels and the structural reason each is missing. That structural reason constrains the engineering fix. This is what the theory is *for*: not a taxonomy of who is good at what, but a build-order generator for any mind.

**The key intellectual moves.**
1. The break-point as a demarcation criterion — the theory states precisely how it could die.
2. Transfer from biology to information-processing systems generally — the same law and the same break-point appear in a transformer (activation steering is the AI analog of the cortical electrode).
3. The shift from descriptive to prescriptive — locate the zero-cell, build the channel that fills it.

**Honest status — stated plainly.**
- The cross-substrate work is **post-hoc consistency, not prediction**. The strong test (does the agreement *geometry* match the overlap vector?) is specified and runnable but not yet run on real data.
- The generalization of B from "biological capability" to "action affordance" is a **real theoretical commitment, held as provisional**.
- Competence values are **architecture-derived priors to be replaced by measurement**.
- No claim here is a report of Claude's private internals — it is reasoning about the architecture class, falsifiable against published model behavior.

**Status at end of Iteration III:** a theory of information-processing systems with a unique falsifiable break-point and a prescriptive output, supported by post-hoc consistency across two maximally different substrates, awaiting its first real experiment.

---

## The throughline

Each iteration did not merely add — it changed the *kind* of theory this is.

| | Iteration I | Iteration II | Iteration III |
|---|---|---|---|
| **Kind of theory** | Narrative sketch | Formal, falsifiable | General + prescriptive |
| **Scope** | Animal bodies | Animal bodies + blind humans | Any information-processing mind |
| **Equations** | 1 (by hand) | 6 (derived) | 7 (unified) |
| **Falsifiability** | None | Per-equation | Single unique break-point |
| **Purpose** | Explain | Predict | Predict + prescribe (build-order) |
| **Tested** | No | No | Post-hoc consistency; experiment specified |

---

## Complete artifact index

| Artifact | What it is | Status |
|---|---|---|
| [`ETPT_Complete.md`](./ETPT_Complete.md) | Full framework paper, ~20,500 words, 7 equations, archetypes, protocols | Ready for arXiv |
| [`etpt_simulator.html`](./etpt_simulator.html) | Interactive simulator — threshold mechanism, 5 device presets, matrix rotation, phenomenology | Working |
| [`index.html`](./index.html) | Iteration III site — the canonical front door with full lineage | Deploy via Pages |
| [`ETPT_Research_Dossier.md`](./ETPT_Research_Dossier.md) | 36-month program: aims, budget, timeline, risk, partnerships | Submittable |
| [`intelligibility_vision.py`](./intelligibility_vision.py) | Cross-substrate intelligibility computation (I = 0.876, divergence vector) | Runs |
| [`cross_substrate_battery.py`](./cross_substrate_battery.py) | Task battery + agreement test + engineerable-gap ranking | Runs (pilot simulated) |
| [`etpt_visualizations.py`](./etpt_visualizations.py) | Publication figures for all framework equations | Runs |
| `viz1–viz6 .png` | Pre-rendered framework figures | Done |
| [Iteration I (2024)](https://tulasikrishna-simulations.github.io/etpt-portfolio/) | The origin: hostel, no laptop, the sketch | Preserved |

---

## Honest status summary

**Proven (mathematically):** Seven internally consistent equations with dimensional checks, boundary conditions, and stated falsification criteria. The framework hangs together.

**Supported (by existing literature):** Cross-modal cortical recruitment in blind humans (Sadato, Pascual-Leone, Amedi); sensory-substitution threshold behavior (Bach-y-Rita, BrainPort); direct cortical form-vision (Beauchamp & Yoshor); blind-community convergent technology (Tenji, Soundscape, flash sonar).

**Consistent (post-hoc):** The cross-substrate application to Claude's vision. Compatible with the theory; not yet a prediction confirmed against measured data.

**Untested (the honest gap):** Every parameter is an estimate. No experiment has been run. ρ_c has never been measured. The agreement-geometry prediction has never been checked on real human + model data.

The framework's strength is structural integration and falsifiability. Its weakness is empirical: it is a program of measurement that has not yet measured. That is the next step, and it is named precisely.

---

## What happens next — in order

1. **Post the framework paper to arXiv.** Establishes priority and a citable record. Highest-priority single action.
2. **Run the cross-substrate experiment.** It needs no lab — a shared image set, a small human panel, and vision-API calls. Likely the fastest publishable result. Pipeline is already built (`cross_substrate_battery.py`).
3. **Apply to Emergent Ventures.** The personal statement is written. The funding path fits an independent researcher with unconventional credentials.
4. **Three cold emails** — Hiraki (Tsukuba), Eagleman (Stanford/Neosensory), Rogers Group (Northwestern). Each carries the simulator link and one specific prediction.
5. **Pre-register the threshold experiment (Aim 1) on OSF.** Locks the design to your name.

The work is built. What it needs now is not more building — it is a public timestamp and one person with lab access who answers an email. Everything in this index exists to make that happen.

---

*Built across a drop year and the year after, from Hospet, Karnataka. The first version had no laptop. The work just kept demanding to be finished.*

*— S R Tulasi Krishna, June 2026*
