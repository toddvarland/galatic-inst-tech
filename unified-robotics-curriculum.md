# Unified Robotics Curriculum

> Consolidated from the curricula of the top 10 U.S. robotics programs: MIT, Carnegie Mellon, Stanford, University of Michigan, Georgia Tech, UC Berkeley, University of Pennsylvania, University of Washington, Johns Hopkins, and UT Austin.

This curriculum synthesizes the common themes, core requirements, and specialized offerings across all ten programs into a single coherent framework. Courses are organized into **foundational prerequisites**, **core robotics pillars**, **advanced specializations**, and **integrative experiences**.

---

## Program Structure Overview

| Level | Credits / Courses | Components |
|-------|-------------------|------------|
| **Undergraduate Minor** | 15–18 credits (5–6 courses) | 1 intro robotics + 4–5 electives across pillars |
| **B.S. in Robotics** | 120+ credits | Math + CS foundations, robotics core, electives, capstone |
| **M.S. in Robotics** | 30–36 credits (10–12 courses) | Core pillars + depth electives + thesis or capstone |
| **Ph.D. in Robotics** | 33–36 course credits + dissertation | Breadth across pillars + depth in specialty + original research |

---

## Part 1: Mathematical & Scientific Foundations

These prerequisite courses appear across virtually every program and provide the mathematical maturity required for robotics coursework.

### 1.1 Mathematics

| Course | Description | Offered At |
|--------|-------------|------------|
| **Calculus I & II** | Limits, derivatives, integrals, series, multivariable calculus | All 10 programs (prerequisite) |
| **Linear Algebra** | Vectors, matrices, eigenvalues, SVD, least squares | All 10 programs — MIT 18.06, CMU 21-241, UMich MATH 214/217 |
| **Differential Equations** | ODEs, systems of ODEs, Laplace transforms | All 10 programs — MIT 18.03, Stanford MATH 53 |
| **Probability & Statistics** | Random variables, distributions, Bayes' theorem, estimation | All 10 programs — CMU 36-225, MIT 6.3700, Berkeley EECS 126 |
| **Optimization** | Convex optimization, linear/nonlinear programming, gradient methods | UPenn ESE 6050, Stanford EE 364A, Berkeley EECS 127, GT ECE 6553 |
| **Numerical Methods** | Numerical linear algebra, differential equation solvers, interpolation | MIT 2.086, CMU 16-211, UW AMATH 301 |

### 1.2 Physics & Engineering Science

| Course | Description | Offered At |
|--------|-------------|------------|
| **Classical Mechanics** | Newtonian mechanics, energy, momentum | All programs (Physics I prerequisite) |
| **Electromagnetism** | Circuits, fields, electromagnetic waves | All programs (Physics II prerequisite) |
| **Statics & Dynamics** | Rigid body equilibrium, kinematics, kinetics | MIT 2.003, UMich ME 240, GT ME 2202, UPenn MEAM 2110 |
| **Signals & Systems** | Fourier analysis, frequency response, filtering, LTI systems | MIT 6.3000, Stanford EE 102A, Berkeley EE 120, GT ECE 2026 |

### 1.3 Computer Science Foundations

| Course | Description | Offered At |
|--------|-------------|------------|
| **Programming (Python/C++)** | Data structures, algorithms, OOP | All programs — CMU 15-122, MIT 6.100A, Stanford CS 106B |
| **Data Structures & Algorithms** | Complexity analysis, graphs, search, sorting | All programs — CMU 15-122/15-251, MIT 6.1210, Berkeley CS 61B |
| **Computer Systems** | Memory, OS basics, embedded programming | CMU 15-213, MIT 6.1910, Stanford CS 107 |
| **Software Engineering** | Version control, testing, system design, ROS | CMU 16-220, MIT 2.12, UMich ROB 320, JHU EN.530.707 |

---

## Part 2: Core Robotics Pillars

All ten programs organize their robotics curricula around four to five central pillars. Courses below represent the consensus core — the knowledge areas that every robotics student should master.

### Pillar 1: Robot Mechanics — Kinematics & Dynamics

> *How robots are physically designed, how they move, and how forces act on them.*

#### Core Courses

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| **Introduction to Robotics** | Forward/inverse kinematics, Jacobians, homogeneous transforms, trajectory planning, sensors & actuators, feedback control | MIT 2.12/2.120, CMU 16-311, Stanford CS 223A / ME 320, UMich ROB 101/201, GT ME 4451, Berkeley EECS C106A, UPenn MEAM 5200, UW EE 347, JHU EN.530.646, UT Austin ME 397 |
| **Robot Kinematics & Dynamics** | Denavit-Hartenberg parameters, manipulator dynamics, Lagrangian mechanics, Newton-Euler formulation | CMU 16-384, Stanford ME 320, UMich ROB 311, UPenn MEAM 6200, JHU EN.530.646 |
| **Dynamics of Mechanical Systems** | Multi-body dynamics, Lagrange's equations, rigid body motion, vibrations | MIT 2.003/2.032, GT ME 6441, UPenn MEAM 5350, UT Austin ME 383Q |
| **Mechanism Design** | Linkages, gears, cams, degrees of freedom, workspace analysis | MIT 2.72, CMU 16-384, UT Austin ME 350R/380R, JHU EN.530.646 |

#### Key Topics Covered
- Rotation matrices, quaternions, Euler angles
- Forward and inverse kinematics
- Velocity kinematics and Jacobians
- Manipulator dynamics (Lagrangian and Newton-Euler)
- Workspace analysis and singularities
- Denavit-Hartenberg convention
- Degrees of freedom and constraint analysis

---

### Pillar 2: Sensing & Perception

> *How robots perceive and interpret the world through sensors and computational methods.*

#### Core Courses

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| **Computer Vision** | Image formation, feature detection, stereo vision, object recognition, segmentation | CMU 16-385/16-720, Stanford CS 231A, Berkeley CS 280, GT CS 6476, UPenn CIS 5810, UW CSE 455, JHU EN.601.461 |
| **Robot Perception** | Sensor fusion, state estimation, filtering, SLAM fundamentals | CMU 16-833, Stanford CS 237A, UMich ROB 530, Berkeley EECS C106B, JHU EN.601.463 |
| **Sensor Systems & Instrumentation** | Sensor types (LIDAR, IMU, encoders, cameras), signal conditioning, data acquisition | MIT 2.671, CMU 16-220, UMich ROB 220, GT BMED 3500, UPenn MEAM 5100, UT Austin ECE 382N |
| **Machine Perception** | 3D vision, depth estimation, point clouds, visual SLAM, multi-modal perception | UPenn CIS 5800, Stanford CS 231A, CMU 16-820, JHU EN.601.661 |

#### Key Topics Covered
- Camera models and calibration
- Feature detection and matching (SIFT, ORB)
- Stereo vision and structure from motion
- Object detection, recognition, and segmentation
- Point cloud processing (PCL)
- Sensor fusion (Kalman filters, particle filters)
- Simultaneous Localization and Mapping (SLAM)
- Deep learning for perception (CNNs, transformers)

---

### Pillar 3: Planning, Decision-Making & AI

> *How robots reason about goals, plan actions, and make decisions in complex environments.*

#### Core Courses

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| **Artificial Intelligence** | Search, logic, probabilistic reasoning, constraint satisfaction, game theory | MIT 6.4100, CMU 15-281, Stanford CS 221, GT CS 6601, Berkeley CS 188, UW CSE 473 |
| **Motion Planning** | Configuration space, sampling-based planners (RRT, PRM), trajectory optimization, graph search | CMU 16-782, Stanford CS 237B, UMich ROB 511, UPenn MEAM 5170, JHU EN.601.463, UT Austin ME 397 |
| **Robot Learning** | Imitation learning, reinforcement learning, sim-to-real transfer, policy optimization | CMU 16-831, Stanford CS 237B, Berkeley CS 285, UW CSE 599, UT Austin CS 391R, GT CS 7648 |
| **Probabilistic Robotics** | Bayesian filtering, hidden Markov models, Markov decision processes, POMDPs | CMU 16-831, Stanford CS 237A, UW CSE 571, Berkeley EECS C106B |

#### Key Topics Covered
- Graph search (A*, Dijkstra's, D*)
- Sampling-based planning (RRT, RRT*, PRM)
- Trajectory optimization
- Task and motion planning (TAMP)
- Markov Decision Processes (MDPs) and POMDPs
- Reinforcement learning (Q-learning, policy gradient, actor-critic)
- Imitation learning and learning from demonstration
- Multi-agent planning and coordination

---

### Pillar 4: Control Systems

> *How robots execute planned motions accurately and respond to disturbances.*

#### Core Courses

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| **Feedback Control Systems** | Transfer functions, root locus, Bode plots, PID control, stability analysis | MIT 2.004/2.14, CMU 16-299, Stanford EE 102B, UMich ROB 301, GT ECE 6550, Berkeley EE C128, UPenn ESE 5050, UW EE 447, JHU EN.530.343 |
| **Modern / State-Space Control** | State-space representation, controllability, observability, state feedback, LQR | MIT 2.151, Stanford EE 263, UMich EECS 560, GT AE 6530, UPenn ESE 5000, Berkeley EE 221A, UW EE 547 |
| **Nonlinear Control** | Lyapunov stability, sliding mode control, feedback linearization, adaptive control | MIT 2.152, Stanford AA 203, GT ECE 6552, Berkeley ME 237, UPenn MEAM 5170 |
| **Optimal Control & Estimation** | LQR/LQG, dynamic programming, Kalman filtering, MPC | CMU 16-745, Stanford AA 203, GT ECE 6553, Berkeley EE 221A, JHU EN.530.678, UT Austin ASE 381P |

#### Key Topics Covered
- PID control design and tuning
- Transfer functions and frequency domain analysis
- State-space modeling and design
- Linear Quadratic Regulator (LQR)
- Kalman filtering and Extended Kalman Filter (EKF)
- Model Predictive Control (MPC)
- Lyapunov stability theory
- Adaptive and robust control

---

### Pillar 5: Robot Systems Integration

> *How hardware and software components are integrated into functioning robotic systems.*

#### Core Courses

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| **Mechatronics** | Integration of mechanical, electrical, and software systems; sensors, actuators, microcontrollers | MIT 2.737, CMU 16-778, UMich ME 461, GT ME 6405, UPenn MEAM 5100, UW ME 471, UT Austin ECE 370N |
| **Robotics: Science & Systems** | Full-stack robotics: perception, planning, control on physical robots; ROS | MIT 6.4200/2.124, CMU 16-311, UMich ROB 550, Berkeley EECS C106A/B |
| **Electronics for Robotics** | Circuit design, motor drivers, power systems, embedded microcontrollers | MIT 2.678/2.679, CMU 16-220, UMich ROB 220, UPenn MEAM 5100 |
| **Robot Operating System (ROS)** | ROS/ROS 2 framework, nodes, topics, services, sensor integration, simulation | MIT 2.12, CMU 16-311, UMich ROB 550, JHU EN.530.707, UT Austin RBT 350 |

#### Key Topics Covered
- Microcontroller programming (Arduino, ARM, ESP32)
- Motor control (DC, stepper, servo, brushless)
- Sensor interfacing (I2C, SPI, UART)
- Power electronics and battery management
- ROS/ROS 2 architecture and tools
- Simulation environments (Gazebo, MuJoCo, Isaac Sim)
- PCB design and fabrication
- System integration and debugging

---

## Part 3: Advanced Specializations

After completing core pillars, students specialize in one or more of the following areas. These reflect the research strengths and advanced course offerings across the ten programs.

### 3.1 Manipulation & Grasping

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| Mechanics of Manipulation | Contact mechanics, grasp analysis, force closure, friction | CMU 16-741, MIT 2.12, Stanford CS 237B |
| AI for Manipulation | Learning-based grasping, dexterous manipulation, tool use | CMU 16-740, Stanford CS 237B, UT Austin CS 395T |
| Dexterous Manipulation | Multi-fingered hands, tactile sensing, in-hand manipulation | CMU 16-848, Berkeley EECS C106B |
| Haptics & Tactile Sensing | Force/torque sensing, tactile arrays, teleoperation feedback | CMU 16-855, UT Austin ME 397, JHU EN.601.220 |

### 3.2 Autonomous Navigation & Mobile Robots

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| Mobile Robots | Wheeled, legged, and aerial locomotion; path planning; obstacle avoidance | CMU 16-761, GT CS 3630, UW CSE 478, UT Austin CS 393R |
| SLAM & Localization | Visual SLAM, lidar SLAM, graph-based SLAM, loop closure | CMU 16-833, UMich ROB 530, JHU EN.601.463 |
| Autonomous Vehicles | Self-driving systems, sensor fusion, behavior planning, safety | Stanford CS 237A, UMich ROB 535, UPenn ESE 6150, UT Austin ASE 479W |
| Aerial Robotics | Quadrotor dynamics, flight control, aerial manipulation, swarm coordination | UPenn MEAM 5430/5460, UT Austin ASE 479W, CMU 16-665 |

### 3.3 Robot Learning & AI

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| Deep Learning | Neural networks, CNNs, RNNs, transformers, generative models | Stanford CS 231N, GT CS 7643, CMU 16-884, Berkeley CS 182, UPenn ESE 5460 |
| Reinforcement Learning | Policy optimization, value functions, model-based RL, multi-agent RL | CMU 16-745, Stanford CS 234, Berkeley CS 285, UT Austin CS 394R, GT CS 7640 |
| Imitation Learning | Learning from demonstration, behavioral cloning, DAgger, inverse RL | CMU 16-831, Stanford CS 237B, GT CS 7648, UT Austin CS 391R |
| Robot Foundation Models | Vision-language-action models, large-scale pretraining for robotics | CMU 16-785, Stanford CS 237B (evolving topics) |

### 3.4 Human-Robot Interaction (HRI)

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| Human-Robot Interaction | Shared autonomy, trust, communication, social norms | GT CS 7633, JHU EN.601.467, UT Austin ECE 382V, CMU 16-887 |
| Assistive Robotics | Prosthetics, exoskeletons, rehabilitation robots, accessibility | MIT 2.183/2.78, UPenn BE 5210, UT Austin ME 350D, JHU EN.530.612 |
| Teleoperation | Remote control, haptic feedback, time delay compensation, supervisory control | UT Austin ME 397, JHU EN.530.707 |
| Social Robotics | Emotion recognition, natural language interaction, embodied agents | GT CS 8803, UW CSE 599 |

### 3.5 Medical & Surgical Robotics

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| Medical Robotics | Surgical systems (da Vinci), image-guided surgery, safety | JHU EN.530.610, GT BMED 4739, UT Austin ME 397 |
| Medical Device Design | FDA regulations, biocompatibility, clinical workflow integration | MIT 2.75, JHU EN.530.612, UT Austin ME 397 |
| Medical Image Processing | Segmentation, registration, 3D reconstruction for surgical planning | CMU 16-725, GT BMED/ECE 4783, JHU EN.601.661 |
| Rehabilitation Engineering | Exoskeletons, neural interfaces, motor recovery, biomechanics | UT Austin ME 385J, UPenn BE 5210, JHU EN.530.612 |

### 3.6 Multi-Robot Systems & Swarms

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| Multi-Robot Planning | Coordination, task allocation, communication, formation control | CMU 16-891, UPenn MEAM 6240, GT ECE 6563 |
| Distributed Robotics | Consensus algorithms, swarm intelligence, coverage, cooperative mapping | UPenn MEAM 6240, GT ECE 6563, UT Austin SWARM Lab |
| Multi-Agent Systems | Game theory, mechanism design, cooperative/competitive strategies | GT CS 8803, UT Austin ASE 389, Stanford AA 228 |

### 3.7 Bio-Inspired & Soft Robotics

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| Bio-Inspired Robotics | Locomotion from nature, compliant mechanisms, animal mechanics | MIT 2.74/2.740, CMU 16-742, UW ME 586 |
| Soft Robotics | Continuum mechanics, pneumatic actuators, flexible materials, soft grippers | MIT 2.075, JHU EN.530.646 (special topics) |
| Biomechanics & Neural Control | Musculoskeletal modeling, motor control, neural circuits | MIT 2.183/2.184, UT Austin ME 385J, UPenn BE 5210 |

### 3.8 Simulation, Dynamics & Computational Methods

| Course | Description | Representative Offerings |
|--------|-------------|--------------------------|
| Robot Dynamics & Simulation | Contact dynamics, rigid body simulation, physics engines | CMU 16-715, Stanford ME 320, UMich ROB 511 |
| Computational Design & Fabrication | Generative design, topology optimization, 3D printing for robots | MIT 2.0911, Stanford ME 328 |
| Physics-Based Deep Learning | Neural ODEs, differentiable simulation, physics-informed networks | MIT 2.C01, Stanford CS 238, Berkeley ME 294 |

---

## Part 4: Integrative & Capstone Experiences

All ten programs emphasize hands-on, project-based learning. The following represent culminating educational experiences.

### 4.1 Capstone Projects

| Experience | Description | Representative Offerings |
|------------|-------------|--------------------------|
| **Robotics Capstone** | Team-based design, build, and test of a complete robotic system | CMU 16-474, UMich ROB 450, GT 8741 Capstone, JHU Senior Design |
| **Robotics Systems Engineering** | Systems-level integration: requirements, architecture, V&V, documentation | CMU 16-450, GT 7785 Intro to Robotics Research |
| **Design-Build-Test Projects** | Semester-long projects involving real hardware and software integration | MIT 2.12, Berkeley EECS C106A/B, UPenn ROBO 5980 |

### 4.2 Research Experiences

| Experience | Description | Representative Offerings |
|------------|-------------|--------------------------|
| **Directed Research** | Faculty-supervised research in a robotics lab | CMU 16-997, UMich ROB 590, GT 8750/8751, UT Austin (portfolio seminars) |
| **Master's Thesis** | Original research contributing to the field; public defense | CMU MSR Thesis, UMich MS Thesis, UPenn ROBO 9990 |
| **Doctoral Dissertation** | Significant original contribution; peer-reviewed publications expected | All 10 programs |
| **Undergraduate Research** | Early research exposure in faculty labs; often for credit | MIT 2.URG, CMU 16-597, UMich ROB 490, JHU Research |

### 4.3 Professional Development

| Experience | Description | Representative Offerings |
|------------|-------------|--------------------------|
| **Robotics Seminars** | Weekly research talks by faculty, students, and industry guests | GT 7741/7742/7743, UT Austin Robotics Seminar, CMU RI Seminar |
| **Ethics in Robotics** | Responsible AI, safety, societal impact, regulation | CMU 16-735, MIT 2.900, UT Austin RBT 350, UPenn CIS 5230 |
| **Industry Internship** | Applied robotics experience in a company setting | CMU 16-990 Practicum, GT Robotics Internship, MIT 2.989 |
| **Teaching Experience** | Serving as TA for robotics courses; required for some PhD programs | CMU (2 semesters), GT (varies), MIT 2.978 |

---

## Part 5: Recommended Course Sequences

### 5.1 Undergraduate Path (4 Years)

| Year | Fall | Spring |
|------|------|--------|
| **1** | Calculus I, Physics I, Intro Programming | Calculus II, Physics II, Data Structures |
| **2** | Linear Algebra, Dynamics, Intro to Robotics | Diff. Equations, Signals & Systems, Computer Vision |
| **3** | Feedback Control, Probability & Statistics, Mechatronics | Motion Planning, Machine Learning, Robot Systems Lab |
| **4** | Robotics Elective I, Robotics Elective II, Capstone I | Robotics Elective III, Capstone II, Undergraduate Thesis |

### 5.2 Master's Path (2 Years)

| Semester | Courses |
|----------|---------|
| **Fall 1** | Robot Kinematics & Dynamics, Modern Control, Computer Vision |
| **Spring 1** | Motion Planning, Robot Learning, Perception & State Estimation |
| **Fall 2** | Specialization Elective I, Specialization Elective II, Thesis/Capstone Research |
| **Spring 2** | Specialization Elective III, Thesis/Capstone Completion |

### 5.3 Ph.D. Path (5–6 Years)

| Phase | Duration | Activities |
|-------|----------|------------|
| **Coursework** | Years 1–2 | Breadth across all pillars (4–6 core courses) + depth in specialty (2–3 advanced courses) |
| **Qualifying Exam** | End of Year 2 | Written and/or oral exam demonstrating mastery of fundamentals |
| **Thesis Proposal** | Year 3 | Define research question, literature review, preliminary results |
| **Dissertation Research** | Years 3–5 | Original research contributions, peer-reviewed publications |
| **Teaching** | 2 semesters | Teaching assistant for robotics courses |
| **Defense** | Year 5–6 | Public defense of doctoral dissertation |

---

## Part 6: Cross-Reference — Courses by University

The following table maps the five core pillars to representative course numbers at each university.

| Pillar | MIT | CMU | Stanford | UMich | Georgia Tech | UC Berkeley | UPenn | UW | JHU | UT Austin |
|--------|-----|-----|----------|-------|--------------|-------------|-------|-----|-----|-----------|
| **Intro Robotics** | 2.12 | 16-311 | CS 223A | ROB 101/201 | ME 4451 | EECS C106A | MEAM 5200 | EE 347 | EN.530.646 | ME 397 |
| **Kinematics/Dynamics** | 2.003 | 16-384 | ME 320 | ROB 311 | ME 6441 | ME 232 | MEAM 5350 | ME 564 | EN.530.646 | ME 383Q |
| **Control** | 2.004 | 16-299 | EE 102B | ROB 301 | ECE 6550 | EE C128 | ESE 5050 | EE 447 | EN.530.343 | ASE 381P |
| **Vision/Perception** | 6.8301 | 16-385 | CS 231A | ROB 530 | CS 6476 | CS 280 | CIS 5810 | CSE 455 | EN.601.461 | CS 381V |
| **Planning/AI** | 6.4100 | 16-782 | CS 221 | ROB 511 | CS 6601 | CS 188 | CIS 5210 | CSE 473 | EN.601.463 | CS 393R |
| **ML/Robot Learning** | 6.8610 | 16-831 | CS 229 | ROB 498 | CS 7648 | CS 285 | ESE 6500 | CSE 599 | EN.601.482 | CS 391R |
| **Mechatronics** | 2.737 | 16-778 | ME 328 | ME 461 | ME 6405 | — | MEAM 5100 | ME 471 | EN.530.420 | ECE 370N |
| **Capstone** | 2.12 proj. | 16-474 | — | ROB 450 | 8741 | C106B proj. | ROBO 5980 | ME 592 | Senior Design | — |

---

## Appendix: Source Programs & Degree Offerings

| University | Undergraduate | Master's | Doctoral | Key Lab/Institute |
|------------|--------------|----------|----------|-------------------|
| **MIT** | EECS 6-2/6-3, MechE Course 2 (robotics courses, no standalone degree) | SM in ME or EECS (robotics focus) | PhD in ME or EECS | CSAIL |
| **CMU** | B.S. in Robotics, Minor, Additional Major | M.S. in Robotics (MSR), M.S. in Robotic Systems Development (MRSD), M.S. in Computer Vision (MSCV) | PhD in Robotics | Robotics Institute |
| **Stanford** | CS/ME/EE (robotics courses, no standalone degree) | MS in CS (AI specialization) or ME | PhD in CS, ME, or EE | Stanford AI Lab (SAIL) |
| **UMich** | B.S.E. in Robotics | M.S. in Robotics | PhD in Robotics | Michigan Robotics Institute |
| **Georgia Tech** | Minor in Robotics | M.S. in Robotics | PhD in Robotics | IRIM |
| **UC Berkeley** | EECS/ME (robotics courses, no standalone degree) | MS in EECS or ME (robotics focus) | PhD in EECS or ME | BAIR Lab |
| **UPenn** | No formal robotics minor — research opportunities + accelerated MSE | MSE in Robotics | PhD through CIS, ESE, or MEAM | GRASP Lab |
| **UW** | CSE/EE/ME courses (no standalone degree) | MS in CSE, EE, or ME (robotics focus) | PhD in CSE, EE, or ME | Paul G. Allen School Robotics Labs |
| **JHU** | Minor in Robotics, Combined BS/MSE | MSE in Robotics (6 specialization tracks) | PhD through CS, ME, ECE, or BME | LCSR |
| **UT Austin** | Minor in Robotics, Honors Undergrad Program | Graduate Portfolio "Certification of Expertise" (via CS, ME, ECE, or ASE degree) | PhD in home department + Portfolio | Texas Robotics |

---

*Last updated: February 2026. Course offerings and requirements are subject to change; consult each university's official catalog for current information.*
