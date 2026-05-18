# Equation Automata 3D

This code contains no trigonometric functions. It defines a 3D toroidal grid, counts neighbors, and applies integer comparison rules. When you run it, the print statement outputs a value converging to approximately **0.22** — the 3D Ising model critical temperature — and the system initialized at p = Kc²ᴰ converges to **1/3 × L³** alive cells.

The 3D automaton extends the [2D result](https://github.com/goektug/Equation-Automata) by replacing the 3×3 Moore square (9 cells) with the 3×3×3 Moore cube (27 cells). The same critical threshold integer **6** — applied to the full 3D cube — gives a rational approximation to the 3D Ising critical temperature with 0.258% accuracy. More remarkably, this generalises to a **closed-form dimensional recursion** that tracks known Ising critical couplings across all dimensions.

---

## The Core Result
### The Magic Angle Connection

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
p₁ = 1/2 + 1/6 = 2/3 = sin²(θ_m) 
p₂ = 1/2 - 1/6 = 1/3 = cos²(θ_m)
```

At this point no trigonometry has appeared anywhere — only an integer neighbor count, a probability, and a quadratic equation. The trigonometric structure emerges from the geometry of the 3D cube.

The roots p₁ = 2/3 and p₂ = 1/3 connect to the geometry of the 
regular tetrahedron inscribed in the 3×3×3 cube:

The roots p₁ = 2/3 and p₂ = 1/3 are not arbitrary rational numbers.
They are the squared trigonometric projections of the **magic angle**
θ_m = arccos(1/√3) ≈ 54.7356°:

The magic angle is half of the tetrahedral angle arccos(−1/3) ≈ 109.47°
— the opening angle formed when a cube is rotated from its space diagonal
axis, and the angle between any two vertices through the exact center of
a regular tetrahedron. The 3D fixed points are therefore geometrically
determined by the symmetry of the tetrahedron inscribed in the 3×3×3
Moore cube.

The parallel with 2D is exact:

    2D: p₁ = cos²(π/8),  p₂ = sin²(π/8)  — half-angle of π/4 (square lattice)
    3D: p₁ = sin²(θ_m),  p₂ = cos²(θ_m)  — half-angle of tetrahedral angle

In 2D the governing angle π/8 is half of the self-dual angle π/4 of the
square lattice. In 3D the governing angle θ_m is half of the tetrahedral
angle arccos(−1/3) of the cubic lattice. Each dimension's phase boundaries
are encoded in the half-angle of its lattice's natural symmetry angle.

---

## The 6/27 Approximation

The key geometric observation is:

> **6/27 = 2/9 = 0.22222...** ≈ **Kc³ᴰ = 0.22165** (error: 0.258%)

where:
- **6** is the 2D critical Moore neighbor threshold — the same integer that governs the 2D automaton
- **27** is the total number of cells in the 3×3×3 Moore cube (including self)

This is the most accurate simple rational approximation to the 3D Ising critical temperature. It arises because the 2D critical threshold (6), when normalised by the full 3D neighborhood cube instead of the 2D neighborhood square, naturally encodes the 3D critical coupling.

The geometric origin: **6** is simultaneously the 2D critical threshold and the number of face neighbors in the 3D von Neumann neighborhood. Dividing by **27** (the full Moore cube volume including self) gives the ratio of the von Neumann coordination number to the Moore cube volume — a quantity that encodes the geometric relationship between the two neighborhood types in 3D.

---

## The Dimensional Recursion

The 6/27 approximation is not isolated. The 2D automaton uses normalisation **g/9** (full 3×3 square including self), giving:

> **K₂ = 4/9 ≈ 0.4444** vs Kc²ᴰ = 0.44069 (error 0.853%)

The 3D automaton uses normalisation **g/27** (full 3×3×3 cube including self), giving:

> **K₃ = 4/18 = 2/9 ≈ 0.2222** vs Kc³ᴰ = 0.22165 (error 0.258%)

The transition is K₃ = K₂ × 1/2, which reveals a **dimensional recursion**:

> **K_{d+1} = K_d × (d−1)/d**

This telescopes to the closed form:

$$K_d = \frac{4}{9(d-1)}$$

The denominator is simply **9(d−1)**:

| d | Formula | Value | Known Ising Kc | Error |
|---|---|---|---|---|
| 2 | 4/9 | 0.44444 | 0.44069 | 0.853% |
| 3 | 4/18 = 2/9 | 0.22222 | 0.22165 | 0.258% |
| 4 | 4/27 | 0.14815 | 0.14969 | 1.030% |
| 5 | 4/36 = 1/9 | 0.11111 | 0.11395 | 2.491% |
| 6 | 4/45 | 0.08889 | 0.09234 | 3.737% |
| 7 | 4/54 | 0.07407 | 0.07768 | 4.642% |
| 8 | 4/63 | 0.06349 | 0.06709 | 5.363% |

The recursion factors (d−1)/d at each dimensional transition:

| Transition | Factor |
|---|---|
| 2D → 3D | 1/2 |
| 3D → 4D | 2/3 |
| 4D → 5D | 3/4 |
| 5D → 6D | 4/5 |

Each added dimension dilutes the critical coupling by (d−1)/d — distributing correlations across a larger hypervolume and reducing effective ordering strength. This is conceptually consistent with renormalization group intuition.

The **d=1 limit** is exact: K₁ = 4/(9×0) = ∞, correctly reflecting that the 1D Ising model has no finite-temperature phase transition.

---

## Comparison to Mean-Field Asymptotics

Known high-dimensional Ising scaling:

> Kc ~ **1/(2d)**

Automaton prediction:

> K_d ~ **4/(9d)**

The ratio of coefficients is **8/9 ≈ 0.889** — only an 11% discrepancy asymptotically. The automaton reproduces the correct **inverse-dimensional scaling form** through pure neighborhood geometry, without any statistical mechanics input.

---

## Why Accuracy Decreases Above 4D

The Ising model changes character at d = 4 — the **upper critical dimension**:

| Dimension | Regime |
|---|---|
| d < 4 | Fluctuation dominated — formula most accurate |
| d = 4 | Upper critical dimension — transition point |
| d > 4 | Mean-field dominated — formula drifts slightly |

Above d = 4, fluctuations matter less, geometry becomes more tree-like, and local neighborhood structure matters differently. The automaton's geometric normalisation naturally captures fluctuation-dominated behaviour precisely, and drifts when mean-field dominates — which is physically expected.

---

## 2D vs 3D Comparison

|  | 2D | 3D |
|---|---|---|
| Neighborhood | 3×3 square = 9 cells | 3×3×3 cube = 27 cells |
| Normalisation | g/9 (full square with self) | g/27 (full cube with self) |
| Critical threshold | g ≤ 6 | g ≤ 27, h ≥ 6 |
| Fixed point equation | p² − p + 1/8 = 0 | p² − p + 2/9 = 0 |
| Upper root | cos²(π/8) = 0.8536 | **2/3** |
| Lower root | sin²(π/8) = 0.1464 | **1/3** |
| Root difference | 1/√2 = 0.7071 | **1/3** |
| Kc approximation | 4/9 ≈ 0.4444 (exact: ln(1+√2)/2) | 2/9 ≈ 0.2222 (~0.258% error) |
| tan²+tan output | converges to Kc | converges to ~0.22 ≈ Kc³ᴰ |

The root difference **1/3** is the 3D analog of **1/√2** in 2D. In 2D:

```
cos²(π/8) − sin²(π/8) = cos(π/4) = 1/√2
```

In 3D:

```
2/3 − 1/3 = 1/3
```

In 3D the fixed points are exact fractions; in 2D they involve irrational trigonometric values. The rationalisation is a consequence of the 3D Moore cube having 27 = 3³ cells — a perfect cube — whose symmetry forces rational fixed points.

---

## Phase Boundaries

The two roots define the first-order phase boundaries of the 3D system:

- **p = 2/3** — upper phase boundary (ferromagnetic basin). System initialised here converges to **1/3 × L³** alive cells.
- **p = 1/3** — lower phase boundary (paramagnetic basin).

The convergence from p = 2/3 to count = 1/3 × L³ is the 3D analog of the 2D system converging from cos²(π/8) toward its ferrimagnetic fixed point. In 3D the fixed points are exact fractions; in 2D they involve irrational trigonometric values.

---

## The tan²+tan Output

The print statement computes:

```python
ratio3 / float(ratio1 * ratio1) + (1 / float(ratio1)) - ratio2
```

which is algebraically equivalent to **tan²(x) + tan(x)** where tan(x) = 1/ratio1. Initialised at p = Kc = ln(1+√2)/2, this output converges toward **~0.22**, consistent with the known 3D Ising critical temperature Kc³ᴰ ≈ 0.22165.

The 6/27 approximation gives an algebraic route to this value: the fixed point condition g/27 = (1−p)·p at g=6 produces 6/27 = 2/9 as the rational approximation to the 3D Ising critical coupling.

Convergence data across five initialisations:

| p | tan²+tan output | Notes |
|---|---|---|
| 2/3 (upper root) | ~0.125 | approaching 1/8 |
| π/8 ≈ 0.393 | ~0.129 | |
| 1/√2 ≈ 0.707 | ~0.090 | below 3D critical coupling |
| Kc ≈ 0.441 | **~0.22** | ≈ Kc³ᴰ |
| 1/3 (lower root) | ~0.30 | above 3D critical value |

The initialisation at the 2D critical temperature Kc produces the output closest to the 3D Ising critical temperature — the system encodes the 3D physics through the 2D critical initialisation.

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

# Coupling condition: normalise by 27 (full cube including self)
if g / 27 > (1 - p) * p:
    nc[(x + 1) % L, y, q] = 1
elif g / 27 < (1 - p) * p:
    nc[(x - 1) % L, y, q] = 1
else:
    nc[x, y, q] = 1
```

The threshold **h ≥ 6** means an alive cell invokes the Neumann rule only when all 6 face neighbors are alive — the 3D analog of the 2D Neumann condition h ≥ 1 out of 4 face neighbors. In 3D, h ≥ 6 out of 6 requires 100% face alignment, enforcing the strongest possible local ferromagnetic order. This drives the convergence from p = 2/3 toward exactly 1/3 × L³ alive cells.

---

## Important Caution

The automaton cannot claim to **derive** the Ising critical temperatures — no partition function exists, no critical exponents are measured, and no renormalization group proof is given. The correct statement is:

> **The automaton generates a remarkably simple dimensional recursion K_d = 4/(9(d−1)) whose values closely track known Ising critical couplings across dimensions 2 through 8, emerging from pure neighborhood geometry without any statistical mechanics input.**

---

## Open Questions

1. **Does the 3D automaton have a Gudermannian analog?** In 2D, tan(π/8) = tanh(Kc) is the stereographic projection connecting the 2D and 1D Ising models via gd(2H) + gd(2H*) = π/2. The 3D roots 2/3 and 1/3 are rational — does a similar exact identity connect them to Kc³ᴰ through a known transcendental function?

2. **Is 6/27 = 2/9 the exact 3D critical coupling, or an approximation?** The 3D Ising critical temperature has no known exact analytical solution. The automaton suggests 2/9 as a candidate rational approximation — the same integer threshold 6 that governs 2D criticality, divided by the full 3D cube size 27.

3. **Is the recursion K_{d+1} = K_d × (d−1)/d dynamically generated or imposed by normalisation?** If it emerges robustly across rule perturbations it is potentially universal; if it only appears for one normalisation it may be an arithmetic artefact. The decisive test is direct simulation at d = 5, 6, 7.

4. **What is the 3D analog of the stereographic projection?** In 2D the Kramers-Wannier duality mediates the 2D→1D projection. The 3D Ising model has no known exact self-duality. Does the 2/9 approximation suggest a hidden structure?

5. **Does K_d = 4/(9(d−1)) have a field-theoretic interpretation?** The asymptotic form 4/(9d) differs from the mean-field prediction 1/(2d) by the factor 8/9. This discrepancy may encode a geometric correction to mean-field theory arising from the discrete Moore neighborhood structure.

6. **What happens at d = 1?** The formula gives K₁ = 4/(9×0) = ∞, which is correct — the 1D Ising model has no finite-temperature phase transition (critical temperature is infinite, or equivalently zero temperature). The formula recovers this limit exactly.
---

## Running the Code

Requires PyCX Simulator:

```
https://github.com/hsayama/PyCX
```

**Performance note:** L=100 gives a 100³ = 1,000,000 cell grid. Each step iterates all cells with full 3D Moore neighbor counting (27 cells per call).

---

## References

- Onsager, L. (1944). Crystal statistics I: A two-dimensional model with an order-disorder transition. *Physical Review*, 65(3-4), 117.
- Kramers, H. A., & Wannier, G. H. (1941). Statistics of the two-dimensional ferromagnet. *Physical Review*, 60(3), 252.
- 2D automaton: [github.com/goektug/Equation-Automata](https://github.com/goektug/Equation-Automata)

---

*Goktug Islamoglu, Freiburg, Germany*
*Contact: goktugislamoglu@gmail.com*
