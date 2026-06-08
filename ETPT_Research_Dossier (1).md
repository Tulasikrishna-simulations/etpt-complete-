# ETPT Haptic Perception Research Program
## A 36-Month Research Dossier

**Principal investigator (current):** S R Tulasi Krishna  
**Affiliation:** Independent researcher · Hospet, Karnataka, India  
**Framework:** Evolutionary Technology Path Theory (ETPT) · arXiv preprint pending  
**Live demonstrator:** [ETPT Haptic Perception Simulator](./etpt_simulator.html)  
**Status:** Pre-experiment · seeking lab partnership & funding

---

## Executive Summary

Most haptic sensory-substitution devices fail to produce spatial perception because they operate below the cortical reclassification threshold ρ_c. The ETPT framework derives this threshold from Shannon channel capacity and predicts ρ_c ≈ 10⁵ bits/cm²/s for human tactile cortex — a value 100–1000× higher than consumer-grade haptic wearables currently achieve. Devices that cross this threshold (BrainPort on tongue, BrainPort 2014 clinical data) produce rapid spatial perception in blind users; devices that don't (Neosensory Buzz, TVSS) produce alerting at best, regardless of training duration.

This program will (1) measure ρ_c in congenitally blind subjects via QUEST adaptive psychophysics with concurrent fMRI, (2) demonstrate cortical reclassification of haptic input as a spatial percept via V1 recruitment, (3) characterize the resulting perceptual category phenomenologically (it is not "vision restored" but a new percept), and (4) translate the result into a body-coverage prototype clearing ρ_c by 2–5× across ≥500 cm² of skin, in partnership with a haptics hardware lab.

The expected outcomes are: a publishable ρ_c value with credible interval (Nature Human Behaviour or Frontiers in Human Neuroscience), validated engineering targets for the haptic-substitution field, and a wearable system suitable for clinical trial in low-vision and blind populations. Budget: $400–600K over 36 months. Risk: tractable — even the negative result (no detectable threshold) is publishable and corrects 50 years of field methodology.

---

## Part I — The Scientific Hypothesis

### I.1 What is predicted

The ETPT framework treats cortical reassignment as a phase transition. Below a critical input density ρ_c, the cortex's existing generative model remains stable: tactile input is parsed as tactile sensation. Above ρ_c, the existing model's free-energy cost exceeds that of forming a new model: the cortex constructs a *spatial* generative model and the percept reclassifies from "tactile" to "spatial."

Quantitatively, the framework derives:

$$\rho_c = \frac{C_v}{A \cdot R \cdot \log_2(1 + \text{SNR})}$$

where C_v is the cortical bandwidth required to support a stable spatial generative model (estimated 10⁴–10⁵ bits/s from baseline V1 activity), A is the stimulated area, R is the update rate, and SNR encodes amplitude resolution per actuator.

The framework further specifies the dynamics of cortical recruitment above threshold via:

$$\frac{dP_i}{dt} = \beta_i (\rho - \rho_c)_+ (P_{\max} - P_i) f_i$$

where the rectified term (·)₊ implements the **subthreshold lock** — the structural prediction that no amount of training produces spatial perception at sub-threshold density. This is the framework's central, falsifiable claim and the field's most overlooked structural feature.

### I.2 What this explains and what it predicts

**Explains:** Why BrainPort (ρ_eff ≈ 28,800 bits/cm²/s on tongue) produces spatial perception in clinical trials while Neosensory Buzz (ρ_eff ≈ 75 bits/cm²/s on wrist) produces alerting only; why TVSS subjects in Bach-y-Rita's 1969 work required hundreds of training hours for marginal results (ρ_eff barely above threshold); why congenital blind subjects out-perform late-blind on sensory substitution tasks (higher plasticity factor f).

**Predicts (testable now):**
1. ρ_c lies in [3 × 10³, 3 × 10⁵] bits/cm²/s with central estimate ~10⁵
2. Sigmoidal psychometric function for spatial-percept emergence with inflection at ρ_c
3. V1 recruitment is detectable on fMRI only above ρ_c
4. Phenomenological descriptors shift from tactile vocabulary to spatial vocabulary above threshold
5. Congenital blind > early blind > late blind > sighted blindfolded in recruitment rate, ordering matches f values
6. The resulting percept is a new perceptual category distinct from both vision and touch

### I.3 Why this is testable now (and wasn't before)

The framework's central prediction has become testable only in the past 36 months because of hardware milestones:
- **VoxeLite (Rogers Group, Northwestern, 2025):** 44–110 nodes/cm² on flexible skin-attachable arrays
- **NTT mid-air ultrasound (2025):** ~10 focal points/cm² with 1000 Hz update
- **Hiraki Lab pneumatic pouches (University of Tsukuba, 2023–):** distributed force rendering with high spatial density potential
- **MRI-compatible haptic delivery (Tsekos et al., Stanford):** enables fMRI co-measurement

Combined, these technologies span the predicted ρ_c range. Five years ago no available hardware could test the prediction; today multiple platforms can.

---

## Part II — Specific Aims

### Aim 1 (months 1–9): Determine ρ_c via QUEST adaptive psychophysics

**Hypothesis:** A sigmoidal psychometric function for spatial-percept reports exists with an inflection at ρ_c ∈ [10⁴, 10⁵] bits/cm²/s.

**Subjects:** n = 30 congenitally blind adults (recruited via blind community organizations); n = 15 sighted controls (blindfolded for training, used to establish baseline). Power analysis: detecting ρ_c population mean within ±15% requires n = 25 per group at α = 0.05, β = 0.20.

**Procedure:** Within-subject QUEST design over 60 trials per subject; stimulus is a spatial pattern (letter, shape) rendered on a forearm haptic array at variable density, with total stimulus energy held constant via amplitude compensation. 2-AFC task: "Did the pattern have spatial structure or feel like undifferentiated buzzing?"

**Hardware:** VoxeLite-class array (110 nodes/cm² × 50 cm²) for primary testing; supplementary higher-density array (300 nodes/cm²) for confirmation of supra-threshold regime.

**Primary outcome:** Posterior estimate of ρ_c per subject; group-level posterior; psychometric slope.

**Secondary outcomes:** Variability across subjects (does ρ_c reflect individual cortex variation, or a true population constant?); difference between congenital and late-blind cohorts.

### Aim 2 (months 6–18): Demonstrate V1 recruitment via fMRI

**Hypothesis:** Above ρ_c, BOLD signal in early visual cortex (V1, V2) is significantly elevated relative to a matched-energy sub-threshold condition; below ρ_c, no significant V1 activation occurs.

**Subjects:** n = 20 from the Aim 1 cohort (subset with clear individual ρ_c estimates).

**Procedure:** Block design, MRI-compatible haptic array delivering high-ρ vs low-ρ (matched energy) vs rest in 20s blocks, 10 blocks/condition. ROI defined anatomically via FreeSurfer V1 parcellation; whole-brain exploratory analysis for additional recruited regions (lateral occipital, intraparietal sulcus).

**Primary outcome:** Effect size of V1 BOLD contrast (high-ρ minus low-ρ), with prediction of statistically significant activation only in the high-ρ condition.

### Aim 3 (months 12–24): Characterize the new perceptual category

**Hypothesis:** Above ρ_c, subjects report the percept in spatial vocabulary not borrowed from vision or touch alone — a distinct perceptual category.

**Procedure:** Structured phenomenological interviews after each training session, conducted in the subject's primary language, transcribed and coded by two blinded raters using a pre-defined vocabulary codebook. Bayesian latent class analysis assigns each subject's report to "tactile percept," "spatial percept," or "new category" classes.

**Primary outcome:** Distribution of subjects across the three categories at each training stage; transition probabilities over time.

**Secondary outcome:** Convergent vocabulary across subjects suggests a stable phenomenological structure for the new percept.

### Aim 4 (months 18–36): Build and field-test a wearable prototype

**Hypothesis:** A wearable haptic system clearing ρ_c by 2–5× across ≥500 cm² of skin enables stable spatial perception of the environment in trained blind users.

**Hardware development path:** In partnership with a haptics hardware lab (Hiraki, Rogers, Neosensory, or comparable), design and build:
- Target spec: 300 nodes/cm², 200 Hz update rate, 16 force levels, 1500 cm² coverage (full back or torso wrap)
- Sensor input: depth camera (Intel RealSense or comparable) + LiDAR (for outdoor) + IMU for self-motion
- Transduction software: depth-as-pressure primary mapping; configurable alternative mappings for comparison studies
- Power, weight, and wearability for ≥4 hours continuous use

**Field trial:** n = 12 trained congenitally blind subjects, 6 months of daily use; outcome measures include navigation accuracy in novel environments, object localization and reach accuracy, and quality-of-life metrics.

---

## Part III — Research Design and Methods

### III.1 Recruitment and ethics

Subject recruitment via partnerships with:
- The National Federation of the Blind (US) or equivalent (Royal National Institute of Blind People in UK; All India Confederation of the Blind)
- University-affiliated low-vision clinics
- Local blind community organizations in study site city

Inclusion: congenitally blind or visually impaired before age 2; otherwise healthy adults aged 18–55. Exclusion: history of neurological disorder, MRI contraindication (Aim 2 only), inability to consent.

IRB approval at host institution required before any subject enrollment. Pre-registration of all studies on OSF before data collection begins.

### III.2 Measurement instruments

**Behavioral:**
- QUEST adaptive procedure (Watson & Pelli 1983)
- 2-AFC reports with confidence rating
- Standardized navigation task in obstacle field
- Reach-and-grasp task with eye-tracking surrogate (head/hand tracking for blind subjects)

**Neural (Aim 2):**
- 3T fMRI (host institution scanner) with MRI-compatible haptic stimulator
- BOLD signal extraction in anatomically-defined ROIs
- Whole-brain GLM with cluster-corrected significance threshold

**Phenomenological (Aim 3):**
- Semi-structured interview protocol (developed in pilot phase)
- Vocabulary coding scheme with inter-rater reliability target κ > 0.80
- Bayesian latent class model (PyMC implementation)

### III.3 Statistical analysis

Pre-registered analysis plan including:
- For Aim 1: hierarchical Bayesian psychometric model with subject and group-level ρ_c parameters
- For Aim 2: GLM-based fMRI analysis with cluster-corrected significance and effect-size reporting
- For Aim 3: Bayesian latent class with model comparison via WAIC
- For Aim 4: mixed-effects models with subject as random effect

All analyses pre-registered on OSF prior to data collection. Both primary outcomes and exploratory secondary outcomes specified. Negative results are pre-registered as publishable.

### III.4 Data management and openness

All de-identified data deposited at OpenNeuro (for fMRI) and OSF (for behavioral/phenomenological) at time of publication. Analysis code on GitHub at time of submission. Pre-registration links live throughout.

---

## Part IV — Timeline and Milestones

```
Year 1 ─────────────────────────────────────────────────────────────────
  Month  1- 3   IRB approval; subject recruitment; OSF pre-registration
  Month  4- 6   Aim 1 pilot (n = 5); refine QUEST parameters; protocol freeze
  Month  7- 9   Aim 1 main cohort (n = 30); analyze; FIRST ρ_c ESTIMATE ★
  Month 10-12   Aim 2 setup; MRI-compatible array commissioning

Year 2 ─────────────────────────────────────────────────────────────────
  Month 13-18   Aim 2 data collection (n = 20); imaging analysis
  Month 13-18   Aim 3 phenomenological interviews (parallel)
  Month 19-21   Manuscript prep — Paper 1: ρ_c determination ★
  Month 22-24   Manuscript prep — Paper 2: cortical recruitment

Year 3 ─────────────────────────────────────────────────────────────────
  Month 25-30   Aim 4 hardware build (in partnership with hardware lab)
  Month 31-33   Field trial subject recruitment and training
  Month 34-36   Field trial completion; manuscript prep
                Paper 3: phenomenological characterization
                Paper 4: working prototype field trial
                ★ Go/no-go decision: clinical trial Phase II
```

### IV.1 Go/no-go criteria

**Month 9 (after Aim 1 first results):**
- Go: ρ_c estimate is in predicted range [3×10³, 3×10⁵] bits/cm²/s with credible interval excluding 0
- No-go: No detectable threshold OR ρ_c far outside predicted range
- No-go outcome is publishable as a falsification of the central prediction and reframes the field

**Month 18 (after Aim 2 fMRI):**
- Go: V1 recruitment effect-size > 0.5 in supra-threshold condition with statistical significance
- No-go: No detectable V1 effect — restricts the framework to behavioral-level claims

**Month 30 (after Aim 4 hardware):**
- Go: Working prototype meets spec; pilot users report clear spatial perception
- Replan: Spec missed; replan with revised hardware partnership

---

## Part V — Budget

### V.1 Three-year total: $440K (modest for clinical-behavioral neuroscience)

| Category | Year 1 | Year 2 | Year 3 | Total |
|---|---|---|---|---|
| Personnel (PI fractional, RA full, postdoc 50%) | $90K | $100K | $100K | $290K |
| Hardware (haptic arrays, MRI-compatible setup) | $40K | $20K | $80K | $140K |
| MRI time (Year 2 primary) | — | $60K | $20K | $80K |
| Subject compensation ($200 × n) | $9K | $9K | $4K | $22K |
| Travel/conferences (3 venues) | $5K | $8K | $10K | $23K |
| Publication, open access fees | $2K | $5K | $8K | $15K |
| Indirect (negotiated with host institution) | — | — | — | (per host) |
| **Subtotal** | **$146K** | **$202K** | **$222K** | **$570K** |

Hardware partnerships may reduce hardware line item significantly (Hiraki lab, Rogers Group, or Neosensory in-kind contribution). MRI time scales to host institution rate.

### V.2 Funding pathway

Plausible funders, ranked by fit:

**Tier 1 (highest fit):**
- **Schmidt Sciences / Schmidt Futures:** funds unconventional researchers; framework fits "AI and cognition" or "cognitive neuroscience" calls
- **Wellcome Trust Discovery Awards:** broad eligibility, supports independent research with institutional sponsor
- **MEXT / JSPS** (if hosted at Tsukuba): direct funding for foreign researchers
- **Emergent Ventures (Mercatus, Tyler Cowen):** specifically funds independent researchers without conventional credentials; fast turnaround, small grants

**Tier 2 (good fit):**
- **NIH R21** (US, requires institutional sponsor): exploratory/developmental research
- **ERC Starting Grant** (EU, requires PhD): unlikely for current author but for future PI
- **DARPA N3** (Next-generation Nonsurgical Neurotechnology): adjacent application

**Tier 3 (specific calls):**
- Apple Vision Pro accessibility research grants
- Tesla / xAI / Meta neural interface partnerships
- Open Philanthropy AI/cognitive science fellowships

### V.3 Phased funding approach

A 36-month full program is unlikely to be funded in a single grant. Phased strategy:

**Phase 1 ($30–80K, 6–9 months):** Emergent Ventures + Schmidt fellowship + matching from host institution. Funds Aim 1 pilot and first ρ_c estimate. **One publishable result.**

**Phase 2 ($150–250K, 18 months):** Wellcome Trust Discovery or NIH R21 (with institutional sponsor secured during Phase 1). Funds Aims 2 and 3. **Two more publications.**

**Phase 3 ($200K+, 12 months):** Industry partnership (Apple, Meta, Neosensory) for hardware development. Funds Aim 4. **Prototype and field trial.**

Each phase produces independently publishable results; failure at any phase yields useful knowledge for the field.

---

## Part VI — Team and Partnerships

### VI.1 Required roles

- **PI (current author):** theoretical framework, experimental design, analysis, writing. Must be hosted at a research institution to be eligible for most funding.
- **Co-PI (psychophysics/cognitive neuroscience):** subject recruitment, IRB, methodology validation, MRI experience. Likely identified through host institution partnership.
- **Hardware partner (PI or commercial):** haptic array development. Critical for Aim 4. Candidates: Hiraki Lab (Tsukuba), Rogers Group (Northwestern), Neosensory.
- **Postdoc / RA:** day-to-day execution, data collection, analysis.

### VI.2 Sought partnerships (priority order)

1. **Hiraki Lab, University of Tsukuba (Japan):** primary fit. Pneumatic pouch hardware is closest to ρ_c-clearing scale-up. Author's original target host institution. Cold-outreach pitch should include the simulator link and the specific ρ_c-clearing engineering requirements derived from Equation 2.

2. **Rogers Research Group, Northwestern (US):** VoxeLite hardware crosses threshold. They have hardware but no theoretical framework guiding next-generation specs. The framework provides exactly that.

3. **Eagleman Lab / Neosensory (Stanford-affiliated):** David Eagleman has written extensively on sensory substitution (*Livewired*); Neosensory sells haptic wristbands but operates well below threshold. The framework specifies the engineering targets that would move them from alerting to perception. Commercial partnership potential.

4. **Bensmaia Lab, University of Chicago:** somatosensory neural prosthetics; experimental psychophysics expertise; could host Aim 1 directly.

5. **Amedi Lab, IDC Herzliya (Israel):** sensory substitution and cross-modal plasticity; direct empirical fit with Aim 2 fMRI work.

### VI.3 What the current author brings

- Theoretical framework with derived predictions (no other team currently working in this space has this)
- Mathematical formalism connecting Shannon channel capacity to cortical reclassification
- Six derived equations covering the dynamics, threshold, accessibility, intelligibility, comfort-trap recovery, and reverse inference
- Working simulator demonstrating live framework behavior across configurations
- Honest assessment of own background: independent researcher, drop year, no laboratory access, no prior peer-reviewed publication, no institutional affiliation. The framework is the credential, not the CV.

This is a clear case where the author's contribution is high-leverage theory and high-leverage simulation/computation; the host institution contributes the experimental apparatus, IRB and clinical infrastructure, and the academic credentials needed for funding eligibility.

---

## Part VII — Risk Analysis and Mitigation

### VII.1 Scientific risks

**Risk: ρ_c is far outside the predicted range.**  
- Likelihood: moderate (15%). The information-theoretic derivation makes assumptions about C_v that could be off by an order of magnitude.
- Impact: framework's quantitative claim falsified; structural claim (threshold exists) may still be valid.
- Mitigation: Aim 1 design measures ρ_c over a 4-decade range of densities; even an extreme value is detectable. A null result (no threshold) is itself publishable.

**Risk: No detectable V1 recruitment despite supra-threshold density.**  
- Likelihood: low (10%). Bach-y-Rita and Amedi labs have shown V1 recruitment with much lower densities; effect should be larger at higher.
- Impact: restricts framework's neural claim, but behavioral threshold and phenomenological claims survive.
- Mitigation: exploratory whole-brain analysis identifies alternative recruited regions; this becomes a substantive finding.

**Risk: Phenomenological reports don't converge to a new category.**  
- Likelihood: moderate (25%). Subjects may use heterogeneous vocabularies.
- Impact: weakens the "new perceptual category" claim; could be reframed as "training of existing tactile-spatial integration."
- Mitigation: latent class analysis is designed to handle heterogeneity; structured codebook reduces idiosyncrasy.

### VII.2 Engineering risks

**Risk: Hardware partnership doesn't materialize.**  
- Likelihood: moderate (30%). Cold outreach has limited yield rates.
- Impact: Aim 4 delayed or replanned with commercial hardware.
- Mitigation: VoxeLite licensing or BrainPort partnership are commercially-accessible alternatives. Aim 4 is timeline-flexible.

**Risk: Pneumatic actuators don't scale to required density without excessive power/weight.**  
- Likelihood: moderate (40%). Real engineering constraint.
- Impact: requires alternative actuator technology (piezoelectric arrays, mid-air ultrasound).
- Mitigation: Aim 4 hardware path is technology-agnostic — the spec is what matters, the implementation can vary.

### VII.3 Translational risks

**Risk: Blind users reject the framing or refuse to engage.**  
- Likelihood: low if framing is right; moderate if framed as "vision restoration."
- Impact: subject recruitment fails.
- Mitigation: community partnership from the outset; framing as "new sense, matched to your cortex" not "fixing blindness"; co-design where possible.

**Risk: IRB delays.**  
- Likelihood: moderate at any institution.
- Impact: timeline slips.
- Mitigation: identify host institutions with fast-track IRBs for behavioral research; structure protocols as minimal-risk where possible.

### VII.4 Career risk to the PI

**Risk: Three years of work with no institutional position at the end.**  
- This is the dominant risk for the current author personally.
- Mitigation: each phase produces independent publications; cumulative record creates eligibility for postdoctoral positions and faculty applications regardless of program completion.

---

## Part VIII — Broader Impact

### VIII.1 Scientific impact

- Quantitative grounding of sensory substitution literature (50 years of work without a clean threshold value)
- Test case for active inference / predictive coding at perceptual category level
- Methodological contribution: information-theoretic derivation of cortical reclassification

### VIII.2 Clinical and accessibility impact

- Engineering targets that move haptic-substitution devices from alerting to perception
- Foundation for clinical trials of next-generation blind-assistive technology
- Open hardware and open data establishing the field's reproducibility baseline

### VIII.3 Commercial impact

- Apple, Meta, Tesla, and similar consumer-tech companies have growing interest in haptic perception. ETPT provides the engineering targets.
- Surgical robotics: haptic feedback above threshold could enable remote surgery with felt anatomical detail
- Scientific instruments: physicists feeling field structures; biologists feeling molecular surfaces

### VIII.4 Methodological impact for cognitive neuroscience

- Pre-registration of behavioral, neural, and phenomenological measures in single program
- Bayesian threshold estimation as model approach
- Open hardware specifications enabling cross-lab replication

---

## Part IX — What This Author Brings, Honestly

I'm an independent researcher in Hospet, Karnataka. I do not have a laptop; I work primarily on a borrowed phone. I am in a drop year. I have no prior peer-reviewed publications. I have no institutional affiliation.

What I have:
- A formalized theoretical framework with six derived equations
- A 20,000-word complete framework paper, ready for arXiv
- Working code for all visualizations
- A live interactive simulator demonstrating the framework's predictions
- The clarity and persistence to have built all of this from a position of no resources
- A specific research program with falsifiable predictions, designed to be runnable today

What I need:
- Institutional affiliation (host PI willing to sponsor)
- Lab access for Aim 1 (psychophysics setup)
- Funding for personal subsistence and travel
- Collaborators with experimental expertise

The asymmetry is deliberate: I bring theory and computation, the partnership brings empirics and credentials. The work is good enough that the partnership is a fair trade.

If you are reading this as a PI or funder considering whether this is worth your time, the test is simple: open the [simulator](./etpt_simulator.html), set it to the "Neosensory Buzz" preset, observe that no amount of training advances the subject's perception (subthreshold lock), then switch to "ETPT proposed target" and watch the percept emerge over 30 simulated hours. If this prediction is correct, every haptic device currently being sold to blind users is operating in the wrong regime and the field has been pointing in approximately the right direction but with the wrong engineering specs for fifty years. That is what I am proposing to measure.

---

**Document version:** 1.0 · May 2026  
**Companion artifacts:**
- ETPT_Complete.md — full framework paper (20,478 words)
- etpt_simulator.html — live interactive simulator
- etpt_visualizations.py — Python code for all framework figures
- Code repository: GitHub (pending public release)
- Preprint: arXiv (pending submission)

**Contact:** *to be added when affiliation secured*

