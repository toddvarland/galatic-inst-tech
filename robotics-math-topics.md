# Pure Mathematics Topics in the Unified Robotics Curriculum

> Extracted from [unified-robotics-curriculum.md](unified-robotics-curriculum.md). This lists every distinct mathematics topic that appears across the curriculum — both as standalone prerequisite coursework and as mathematical tools embedded within robotics courses.

---

## 1. Calculus

| Topic | Where It Appears |
|-------|-----------------|
| Limits & continuity | Foundation 1.1 — Calculus I |
| Single-variable differentiation | Foundation 1.1 — Calculus I |
| Single-variable integration | Foundation 1.1 — Calculus I |
| Infinite series & convergence | Foundation 1.1 — Calculus II |
| Multivariable calculus (partial derivatives, gradients) | Foundation 1.1 — Calculus II; Pillar 4 (control); Optimization |
| Vector calculus (div, curl, flux, line/surface integrals) | Foundation 1.1 — Calculus II; Foundation 1.2 — Electromagnetism |
| Calculus of variations | Pillar 1 — Lagrangian mechanics; Pillar 4 — Optimal control |

---

## 2. Linear Algebra

| Topic | Where It Appears |
|-------|-----------------|
| Vectors, vector spaces, subspaces | Foundation 1.1; all pillars |
| Matrix operations & matrix algebra | Foundation 1.1; Pillar 1 — Kinematics |
| Systems of linear equations | Foundation 1.1; Pillar 4 — State-space control |
| Eigenvalues & eigenvectors | Foundation 1.1; Pillar 4 — Stability analysis |
| Singular Value Decomposition (SVD) | Foundation 1.1; Pillar 2 — Computer vision |
| Least squares & pseudo-inverses | Foundation 1.1; Pillar 1 — Inverse kinematics; Pillar 4 — Estimation |
| Rotation matrices | Pillar 1 — Robot kinematics |
| Homogeneous transformations (SE(3)) | Pillar 1 — Forward/inverse kinematics |
| Jacobian matrices | Pillar 1 — Velocity kinematics; Pillar 4 — Linearization |
| Positive definite / semidefinite matrices | Pillar 4 — LQR, Lyapunov; Optimization |
| Matrix exponentials | Pillar 1 — Rigid body motion; Pillar 4 — State-space |
| Rank, nullspace, range | Pillar 1 — Singularity analysis; Foundation 1.1 |
| Inner products & norms | Foundation 1.1; Pillar 3 — Planning cost functions |
| Linear transformations | Foundation 1.1; Pillar 1 — Coordinate transforms |

---

## 3. Differential Equations

| Topic | Where It Appears |
|-------|-----------------|
| First-order ODEs | Foundation 1.1; Pillar 4 — Control systems |
| Higher-order linear ODEs | Foundation 1.1; Pillar 1 — Dynamics |
| Systems of ODEs | Foundation 1.1; Pillar 4 — State-space control |
| Laplace transforms | Foundation 1.1; Pillar 4 — Transfer functions |
| Stability of equilibria | Pillar 4 — Lyapunov stability, nonlinear control |
| Phase portraits & qualitative analysis | Pillar 4 — Nonlinear control |
| Numerical ODE solvers (Euler, Runge-Kutta) | Foundation 1.1 — Numerical methods; Spec 3.8 — Simulation |
| Neural ODEs | Spec 3.8 — Physics-based deep learning |

---

## 4. Probability & Statistics

| Topic | Where It Appears |
|-------|-----------------|
| Probability axioms & combinatorics | Foundation 1.1 |
| Random variables (discrete & continuous) | Foundation 1.1; Pillar 2 — Perception |
| Probability distributions (Gaussian, uniform, Poisson, etc.) | Foundation 1.1; Pillar 2 — Sensor models |
| Joint, marginal, and conditional probability | Foundation 1.1; Pillar 3 — Probabilistic robotics |
| Bayes' theorem & Bayesian inference | Foundation 1.1; Pillar 2 — SLAM; Pillar 3 — Probabilistic robotics |
| Expectation, variance, covariance | Foundation 1.1; Pillar 4 — Kalman filtering |
| Covariance matrices | Pillar 2 — Sensor fusion; Pillar 4 — EKF |
| Maximum likelihood estimation (MLE) | Pillar 2 — Perception; Spec 3.3 — Deep learning |
| Maximum a posteriori estimation (MAP) | Pillar 2 — SLAM |
| Gaussian processes | Spec 3.3 — Robot learning |
| Markov chains & stochastic processes | Pillar 3 — MDPs, POMDPs |
| Hidden Markov Models (HMMs) | Pillar 3 — Probabilistic robotics |
| Statistical hypothesis testing | Foundation 1.1 |
| Monte Carlo methods | Pillar 2 — Particle filters; Pillar 3 — Sampling-based planning |

---

## 5. Optimization

| Topic | Where It Appears |
|-------|-----------------|
| Unconstrained optimization (gradient descent, Newton's method) | Foundation 1.1; Spec 3.3 — Deep learning |
| Constrained optimization (Lagrange multipliers, KKT conditions) | Foundation 1.1; Pillar 3 — Trajectory optimization |
| Convex optimization | Foundation 1.1 — Optimization; Pillar 4 — LQR; Stanford EE 364A |
| Linear programming | Foundation 1.1 — Optimization |
| Quadratic programming | Pillar 4 — MPC; Pillar 3 — Trajectory optimization |
| Nonlinear programming | Foundation 1.1; Pillar 3 — Motion planning |
| Dynamic programming | Pillar 3 — MDPs; Pillar 4 — Optimal control |
| Gradient methods (SGD, Adam) | Spec 3.3 — Deep learning, reinforcement learning |
| Semidefinite programming | Pillar 4 — Robust control (advanced) |

---

## 6. Geometry & Topology

| Topic | Where It Appears |
|-------|-----------------|
| Euclidean geometry (distances, angles, planes) | Pillar 1 — Kinematics; Pillar 2 — Vision |
| Rotation representations: Euler angles | Pillar 1 — Robot kinematics |
| Rotation representations: quaternions | Pillar 1 — Robot kinematics |
| Rotation representations: axis-angle | Pillar 1 — Robot kinematics |
| Lie groups SO(3), SE(3) | Pillar 1 — Rigid body motion |
| Lie algebra so(3), se(3) | Pillar 1 — Velocity kinematics |
| Configuration space (C-space) | Pillar 3 — Motion planning |
| Workspace analysis | Pillar 1 — Mechanism design |
| Degrees of freedom & constraint analysis | Pillar 1 — Mechanism design |
| Projective geometry | Pillar 2 — Camera models, epipolar geometry |
| Manifolds (basic concepts) | Pillar 1 — Configuration spaces; Pillar 3 — Planning |
| Convex sets & convex hulls | Pillar 3 — Collision detection; Optimization |
| Voronoi diagrams & Delaunay triangulation | Pillar 3 — Motion planning |

---

## 7. Graph Theory & Discrete Mathematics

| Topic | Where It Appears |
|-------|-----------------|
| Graphs (vertices, edges, directed/undirected) | Pillar 3 — Planning; Foundation 1.3 — Algorithms |
| Graph search: BFS, DFS | Foundation 1.3 — Data structures & algorithms |
| Shortest path: Dijkstra's, A*, D* | Pillar 3 — Motion planning |
| Trees and tree search | Pillar 3 — RRT, behavior trees |
| Graph-based SLAM (pose graphs) | Pillar 2 — SLAM; Spec 3.2 |
| Combinatorics | Foundation 1.1 — Probability; Pillar 3 — Task planning |
| Logic (propositional, first-order) | Pillar 3 — AI |
| Complexity analysis (Big-O) | Foundation 1.3 — Algorithms |

---

## 8. Fourier Analysis & Signal Processing

| Topic | Where It Appears |
|-------|-----------------|
| Fourier series | Foundation 1.2 — Signals & systems |
| Fourier transform (continuous & discrete / FFT) | Foundation 1.2; Pillar 2 — Image processing |
| Frequency domain analysis (Bode plots, Nyquist) | Pillar 4 — Feedback control |
| Z-transform | Foundation 1.2 — Discrete-time systems |
| Laplace transform | Foundation 1.1 — Diff. Eq.; Pillar 4 — Transfer functions |
| Convolution | Foundation 1.2; Pillar 2 — Computer vision (CNNs) |
| Sampling theorem (Nyquist–Shannon) | Foundation 1.2 — Signals & systems |
| Filtering (low-pass, band-pass, Kalman) | Foundation 1.2; Pillar 2 — Sensor filtering; Pillar 4 — Estimation |

---

## 9. Numerical Methods

| Topic | Where It Appears |
|-------|-----------------|
| Numerical linear algebra (LU, QR, Cholesky decomposition) | Foundation 1.1 — Numerical methods |
| Numerical integration (quadrature) | Foundation 1.1; Spec 3.8 — Simulation |
| Numerical ODE solvers (Euler, RK4, adaptive step) | Foundation 1.1; Spec 3.8 — Robot dynamics & simulation |
| Root finding (Newton-Raphson, bisection) | Foundation 1.1; Pillar 1 — Inverse kinematics |
| Interpolation & splines | Foundation 1.1; Pillar 1 — Trajectory planning |
| Finite element methods (FEA) | Spec 3.8 — Computational design |
| Numerical stability & conditioning | Foundation 1.1 — Numerical methods |

---

## Summary by Curriculum Area

| Math Domain | Prerequisite (Part 1) | Core Pillars (Part 2) | Specializations (Part 3) |
|-------------|:---------------------:|:---------------------:|:------------------------:|
| Calculus | ● | ● | ● |
| Linear Algebra | ● | ● | ● |
| Differential Equations | ● | ● | ● |
| Probability & Statistics | ● | ● | ● |
| Optimization | ● | ● | ● |
| Geometry & Topology | | ● | ● |
| Graph Theory & Discrete Math | ● | ● | |
| Fourier Analysis & Signals | ● | ● | |
| Numerical Methods | ● | | ● |

---

*Derived from the unified robotics curriculum consolidating MIT, CMU, Stanford, UMich, Georgia Tech, UC Berkeley, UPenn, UW, JHU, and UT Austin.*
