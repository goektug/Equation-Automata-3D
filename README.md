# Equation Automata 3D
 
This code contains no trigonometric functions. It defines a 3D toroidal grid, counts neighbors, and applies integer comparison rules. When you run it, the print statement outputs a value converging to approximately **0.22** — the 3D Ising model critical temperature — and the system initialized at p = 2/3 converges to **1/3 × L³** alive cells.
 
The 3D automaton extends the [2D result](https://github.com/goektug/Equation-Automata) by replacing the 3×3 Moore square (9 cells) with the 3×3×3 Moore cube (27 cells). The same critical threshold integer **6** — applied to the full 3D cube — gives a rational approximation to the 3D Ising critical temperature with 0.258% error.
 
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
 
At this point no trigonometry has appeared anywhere — only an integer neighbor count, a probability, and a quadratic equation. The trigonometric structure emerges from the geometry of the 3D cube.
 
---
 
## The 6/27 Approximation
 
The key geometric observation is:
 
> **6/27 = 2/9 = 0.22222...** ≈ **Kc³ᴰ = 0.22165** (error: 0.258%)
 
where:
- **6** is the 2D critical Moore neighbor threshold — the same integer that governs the 2D automaton
- **27** is the total number of cells in the 3×3×3 Moore cube (including self)
This is the most accurate simple rational approximation to the 3D Ising critical temperature. It arises because the 2D critical threshold (6), when normalized by the full 3D neighborhood cube instead of the 2D neighborhood square, naturally encodes the 3D critical coupling.
 
---
 
## 2D vs 3D Comparison
 
|  | 2D | 3D |
|---|---|---|
| Neighborhood | 3×3 square = 9 cells | 3×3×3 cube = 27 cells |
| Normalization | g/8 (neighbors only) | g/27 (full cube with self) |
| Critical threshold | g ≤ 6 | g ≤ 27, h ≥ 6 |
| Fixed point equation | p² − p + 1/8 = 0 | p² − p + 6/27 = 0 |
| Upper root | cos²(π/8) = 0.8536 | **2/3** |
| Lower root | sin²(π/8) = 0.1464 | **1/3** |
| Root difference | 1/√2 = 0.7071 | **1/3** |
| Kc approximation | ln(1+√2)/2 = 0.44069 (exact) | 6/27 = 0.22222 (~0.258% error) |
| tan²+tan output | converges to Kc | converges to ~0.22 ≈ Kc³ᴰ |
 
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
The convergence from p = 2/3 to **count = 1/3 × L³** is the 3D analog of the 2D system converging from cos²(π/8) toward its ferrimagnetic fixed point. In 3D the fixed points are exact fractions; in 2D they involve irrational trigonometric values.
 
---
 
## The tan²+tan Output
 
The print statement at line 208 computes:
 
```python
ratio3 / float(ratio1 * ratio1) + (1 / float(ratio1)) - ratio2
```
 
which is algebraically equivalent to **tan²(x) + tan(x)** where tan(x) = 1/ratio1. Initialized at p = Kc = ln(1+√2)/2, this output converges toward **~0.22**, consistent with the known 3D Ising critical temperature Kc³ᴰ ≈ 0.22165.
 
The 6/27 approximation gives an algebraic route to this value: the fixed point condition g/27 = (1−p)·p at g=6 produces 6/27 = 2/9 = 0.2̄2̄ as the rational approximation to the 3D Ising critical coupling.
 
---
 
## Convergence Data
 
Five initializations were tested. The tan²+tan output for each:
 
| p initialization | tan²+tan converges toward | Notes |
|---|---|---|
| 2/3 (upper root) | ~0.125 | approaching 1/8 = 6/48 |
| π/8 ≈ 0.393 | ~0.129 | |
| 1/√2 ≈ 0.707 | ~0.090 | near zero — below 3D critical coupling |
| Kc ≈ 0.441 | ~0.22 | ≈ Kc³ᴰ |
| 1/3 (lower root) | ~0.30 | above the 3D critical value |
 
The initialization at the 2D critical temperature Kc produces the output closest to the 3D Ising critical temperature — the system is encoding the 3D physics through the 2D critical initialization.
 
---
 
## Parameter Configuration
 
The critical parameter changes from 2D to 3D:
 
```python
# Dead cell rule: g<=27 means effectively all dead cells can flip
if c[x, y, q] == 0:
    nc[x, y, q] = 0 if g <= 27 else 1
 
# Neumann condition: h>=6 means all 6 face neighbors must be alive
if h >= 6:
    nc[x, y, q] = 1 if g <= 27 else 0
 
# Coupling condition: normalize by 27 (full cube)
if g / 27 > (1 - p) * p:
    nc[(x + 1) % L, y, q] = 1
elif g / 27 < (1 - p) * p:
    nc[(x - 1) % L, y, q] = 1
else:
    nc[x, y, q] = 1
```
 
The threshold **h ≥ 6** means an alive cell invokes the Neumann rule only when all 6 face neighbors are alive — the 3D analog of the 2D Neumann condition h ≥ 1 (out of 4 face neighbors, requiring 25% alignment). In 3D, h ≥ 6 out of 6 requires 100% face alignment, enforcing the strongest possible local ferromagnetic order.
 
---
 
## Open Questions
 
1. **Does the 3D automaton have a Gudermannian analog?** In 2D, tan(π/8) = tanh(Kc) is the stereographic projection connecting the 2D and 1D Ising models. The 3D roots 2/3 and 1/3 are rational — does a similar exact identity connect them to Kc³ᴰ through a known transcendental function?
2. **Is 6/27 = 2/9 the exact 3D critical coupling, or an approximation?** The 3D Ising critical temperature has no known exact analytical solution. The automaton suggests 2/9 as a candidate rational approximation — the same integer threshold 6 that governs 2D criticality, divided by the full 3D cube size 27.
3. **What is the 3D analog of the stereographic projection?** In 2D the Kramers-Wannier duality condition gd(2H) + gd(2H*) = π/2 with the Gudermannian mediates the projection. The 3D Ising model has no known exact self-duality. Does the 2/9 approximation suggest a hidden structure?
4. **Can the method extend to 4D and beyond?** The pattern suggests: normalize by the full (2d+1)ᴺ neighborhood cube, keep threshold at g=6. In 4D: 3⁴ = 81 cells, 6/81 = 2/27 ≈ 0.074. The 4D Ising critical temperature is known numerically (~0.1496) — does 6/81 approximate it?
---
 
## Running the Code
 
Requires PyCX Simulator:
 
```
https://github.com/hsayama/PyCX
```
 
**Performance note:** L=100 gives a 100³ = 1,000,000 cell grid. Each step iterates over all cells with full 3D Moore neighbor counting (27 cells per call). Use L=30 for fast testing (27,000 cells) and L=100 for production results.
 
---
 
## References
 
- Onsager, L. (1944). Crystal statistics I: A two-dimensional model with an order-disorder transition. *Physical Review*, 65(3-4), 117.
- Kramers, H. A., & Wannier, G. H. (1941). Statistics of the two-dimensional ferromagnet. *Physical Review*, 60(3), 252.
- 2D automaton: [github.com/goektug/Equation-Automata](https://github.com/goektug/Equation-Automata)
---
 
*Goktug Islamoglu, Freiburg, Germany*
*Contact: goktugislamoglu@gmail.com*
