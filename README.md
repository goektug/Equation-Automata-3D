# Equation Automata 3D
 
This code contains no trigonometric functions. It defines a 3D toroidal grid, counts neighbors, and applies integer comparison rules. When you run it, the print statement outputs a value converging to approximately **0.22** — close to the 3D Ising model critical temperature — and the system initialized at p = 2/3 converges to **1/3 × L³** alive cells.
 
The 3D automaton extends the [2D result](https://github.com/goektug/Equation-Automata) by replacing the 3×3 Moore square (9 cells) with the 3×3×3 Moore cube (27 cells). The same critical threshold integer **6** — applied to the full 3D cube — gives a rational approximation to the 3D Ising critical temperature. More remarkably, this extends to a **closed-form dimensional recursion** that tracks known Ising critical couplings across all dimensions.
 
---
 
## The Core Result
 
The automaton rule is:
 
```python
if g / 27 > (1 - p) * p:
```
 
where `g` is the 3D Moore neighbor count (max 26) and `p` is the initial cell density. Setting `g = 6` and solving the equality:
 
```
p² - p + 6/27 = 0
p² - p + 2/9  = 0
```
 
The discriminant is exactly **1/9**, giving roots:
 
```
p₁ = 1/2 + 1/6 = 2/3
p₂ = 1/2 - 1/6 = 1/3
```
 
These are exact rational numbers — far cleaner than the 2D roots cos²(π/8) and sin²(π/8).
 
At this point no trigonometry has appeared anywhere — only an integer neighbor count, a probability, and a quadratic equation.
 
---
 
## The Dimensional Recursion
 
The key observation is that **6/27 = 2/9** approximates the 3D Ising critical temperature. But this is not an isolated numerical coincidence. The 2D automaton uses normalization **g/9** (full 3×3 square including self), giving:
 
> **K₂ = 4/9 ≈ 0.4444** vs Kc²ᴰ = 0.44069 (error 0.853%)
 
The 3D automaton uses normalization **g/27** (full 3×3×3 cube including self), giving:
 
> **K₃ = 4/18 = 2/9 ≈ 0.2222** vs Kc³ᴰ = 0.22165 (error 0.258%)
 
The transition from K₂ to K₃ is:
 
> **K₃ = K₂ × 1/2**
 
This reveals a **dimensional recursion**:
 
> **K_{d+1} = K_d × (d−1)/d**
 
with the factor (d−1)/d at each step. This telescopes exactly:
 
$$K_d = \frac{4}{9(d-1)}$$
 
---
 
## The Complete Dimensional Sequence
 
| d | Formula | Value | Known Ising Kc | Error |
|---|---|---|---|---|
| 2 | 4/9 | 0.44444 | 0.44069 | 0.853% |
| 3 | 4/18 = 2/9 | 0.22222 | 0.22165 | 0.258% |
| 4 | 4/27 | 0.14815 | 0.14969 | 1.030% |
| 5 | 4/36 = 1/9 | 0.11111 | 0.11395 | 2.491% |
| 6 | 4/45 | 0.08889 | 0.09234 | 3.737% |
| 7 | 4/54 | 0.07407 | 0.07768 | 4.642% |
| 8 | 4/63 | 0.06349 | 0.06709 | 5.363% |
 
The denominator pattern is simply **9(d−1)**:
 
| d | Denominator |
|---|---|
| 2 | 9×1 = 9 |
| 3 | 9×2 = 18 |
| 4 | 9×3 = 27 |
| 5 | 9×4 = 36 |
| 6 | 9×5 = 45 |
 
The recursion factors (d−1)/d are:
 
| Transition | Factor |
|---|---|
| 2D → 3D | 1/2 |
| 3D → 4D | 2/3 |
| 4D → 5D | 3/4 |
| 5D → 6D | 4/5 |
 
Each added dimension dilutes the critical coupling by a factor of (d−1)/d — distributing correlations across a larger hypervolume and reducing effective ordering strength. This is conceptually consistent with renormalization group intuition.
 
---
 
## Why Accuracy Decreases Above 4D
 
The Ising model changes character at d = 4 — the **upper critical dimension**:
 
| Dimension | Regime |
|---|---|
| d < 4 | Fluctuation dominated — formula most accurate |
| d = 4 | Upper critical dimension — transition point |
| d > 4 | Mean-field dominated — formula drifts slightly |
 
Above d = 4, fluctuations matter less, geometry becomes more tree-like, and local neighborhood structure matters differently. The automaton's geometric normalization naturally captures fluctuation-dominated behavior precisely, and drifts when mean-field dominates — which is physically expected.
 
---
 
## Comparison to Mean-Field Asymptotics
 
Known high-dimensional Ising scaling:
 
> Kc ~ **1/(2d)**
 
Automaton prediction:
 
> Kd ~ **4/(9d)** = **(4/9)/d**
 
The ratio of coefficients is **8/9 ≈ 0.889** — only an 11% discrepancy asymptotically. The automaton reproduces the correct **inverse-dimensional scaling form** through pure neighborhood geometry, without any statistical mechanics input.
 
---
 
## 2D vs 3D Comparison
 
|  | 2D | 3D |
|---|---|---|
| Neighborhood | 3×3 square = 9 cells | 3×3×3 cube = 27 cells |
| Normalization | g/9 (full square) | g/27 (full cube) |
| Critical threshold | g ≤ 6 | g ≤ 27, h ≥ 6 |
| Fixed point equation | p² − p + 1/8 = 0 | p² − p + 2/9 = 0 |
| Upper root | cos²(π/8) = 0.8536 | **2/3** |
| Lower root | sin²(π/8) = 0.1464 | **1/3** |
| Root difference | 1/√2 | **1/3** |
| Kc approximation | 4/9 ≈ 0.4444 | 2/9 ≈ 0.2222 |
| tan²+tan output | converges to ~Kc | converges to ~0.22 ≈ Kc³ᴰ |
 
The root difference **1/3** is the 3D analog of **1/√2** in 2D. In 2D:
 
```
cos²(π/8) − sin²(π/8) = cos(π/4) = 1/√2
```
 
In 3D:
 
```
2/3 − 1/3 = 1/3
```
 
---
 
## Phase Boundaries
 
The two roots define the first-order phase boundaries of the 3D system:
 
- **p = 2/3** — upper phase boundary (ferromagnetic basin). System initialized here converges to **1/3 × L³** alive cells.
- **p = 1/3** — lower phase boundary (paramagnetic basin).
The convergence from p = 2/3 to count = 1/3 × L³ is the 3D analog of the 2D system converging from cos²(π/8) toward its ferrimagnetic fixed point. In 3D the fixed points are exact fractions; in 2D they involve irrational trigonometric values.
 
---
 
## The tan²+tan Output
 
The print statement computes:
 
```python
ratio3 / float(ratio1 * ratio1) + (1 / float(ratio1)) - ratio2
```
 
which is algebraically equivalent to **tan²(x) + tan(x)** where tan(x) = 1/ratio1. Initialized at p = Kc = ln(1+√2)/2, this output converges toward **~0.22**, consistent with the known 3D Ising critical temperature Kc³ᴰ ≈ 0.22165.
 
Convergence data across five initializations:
 
| p | tan²+tan output | Notes |
|---|---|---|
| 2/3 (upper root) | ~0.125 | approaching 1/8 |
| π/8 ≈ 0.393 | ~0.129 | |
| 1/√2 ≈ 0.707 | ~0.090 | below 3D critical coupling |
| Kc ≈ 0.441 | **~0.22** | ≈ Kc³ᴰ |
| 1/3 (lower root) | ~0.30 | above 3D critical value |
 
---
 
## Parameter Configuration
 
The critical parameter changes from 2D to 3D:
 
```python
# Dead cell rule
if c[x, y, q] == 0:
    nc[x, y, q] = 0 if g <= 27 else 1
 
# Neumann condition: all 6 face neighbors must be alive
if h >= 6:
    nc[x, y, q] = 1 if g <= 27 else 0
 
# Coupling condition: normalize by 27 (full cube including self)
if g / 27 > (1 - p) * p:
    nc[(x + 1) % L, y, q] = 1
elif g / 27 < (1 - p) * p:
    nc[(x - 1) % L, y, q] = 1
else:
    nc[x, y, q] = 1
```
 
The threshold **h ≥ 6** means an alive cell invokes the Neumann rule only when all 6 face neighbors are alive — the strongest possible local ferromagnetic order in 3D.
 
---
 
## Important Caution
 
The automaton cannot claim to **derive** the Ising critical temperatures — no partition function exists, no critical exponents are measured, and no renormalization group proof is given. The correct statement is:
 
> **The automaton generates a remarkably simple dimensional recursion K_d = 4/(9(d−1)) whose values closely track known Ising critical couplings across dimensions 2 through 8.**
 
The recursion emerges from pure neighborhood geometry — the ratio of the 2D critical threshold (6) to the volume of the d-dimensional Moore hypercube (3ᵈ) — without any statistical mechanics input.
 
---
 
## Open Questions
 
1. **Is the recursion K_{d+1} = K_d × (d−1)/d dynamically generated by the automaton, or imposed by the normalization?** If it emerges robustly across rule perturbations it is potentially universal; if it only appears for one normalization it may be an arithmetic artifact. The decisive test is direct simulation at d = 5, 6, 7.
2. **What is the 3D analog of the Gudermannian stereographic projection?** In 2D, tan(π/8) = tanh(Kc) connects the 2D and 1D Ising models through an exact identity. The 3D roots 2/3 and 1/3 are rational — does an analogous exact identity exist connecting them to Kc³ᴰ?
3. **Does the formula K_d = 4/(9(d−1)) have a field-theoretic interpretation?** The asymptotic form 4/(9d) differs from the mean-field prediction 1/(2d) by the factor 8/9. This discrepancy may encode a geometric correction to mean-field theory arising from the discrete Moore neighborhood structure.
4. **What happens at d = 1?** The formula gives K₁ = 4/(9×0) = ∞, which is correct — the 1D Ising model has no finite-temperature phase transition (critical temperature is infinite, or equivalently zero temperature). The formula recovers this limit exactly.
---
 
## Running the Code
 
Requires PyCX Simulator:
 
```
https://github.com/hsayama/PyCX
```
 
**Performance note:** L=100 gives a 100³ = 1,000,000 cell grid. Use L=30 for fast testing (27,000 cells) and L=100 for production results. Each step iterates all cells with full 3D Moore neighbor counting (27 cells per call).
 
---
 
## References
 
- Onsager, L. (1944). Crystal statistics I: A two-dimensional model with an order-disorder transition. *Physical Review*, 65(3-4), 117.
- Kramers, H. A., & Wannier, G. H. (1941). Statistics of the two-dimensional ferromagnet. *Physical Review*, 60(3), 252.
- 2D automaton: [github.com/goektug/Equation-Automata](https://github.com/goektug/Equation-Automata)
---
 
*Goktug Islamoglu, Freiburg, Germany*
*Contact: goktugislamoglu@gmail.com*
