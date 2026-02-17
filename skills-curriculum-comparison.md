# Skills vs. Unified Robotics Curriculum — Comparison

This table maps each skill from [skills.md](skills.md) to the corresponding area(s) in the [unified robotics curriculum](unified-robotics-curriculum.md), noting which pillar, specialization, or foundation covers it and any gaps.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Directly covered by curriculum coursework |
| ⚠️ | Partially covered or covered as a subtopic |
| ❌ | Not explicitly covered in curriculum |

---

## 1. Software Skills

| # | Skill | Cov. | Curriculum Section | Notes |
|---|-------|------|--------------------|-------|
| 1.1 | Localization | ✅ | Pillar 2: Sensing & Perception — Robot Perception; Spec 3.2: SLAM & Localization | Core topic in probabilistic robotics and SLAM courses (CMU 16-833, UMich ROB 530) |
| 1.2 | Writing algorithms for localization | ✅ | Pillar 2: Robot Perception; Pillar 3: Probabilistic Robotics | Bayesian filtering, particle filters, EKF covered across all 10 programs |
| 1.3 | Training using a simulation | ✅ | Pillar 5: Robot Systems Integration (Gazebo, MuJoCo, Isaac Sim); Spec 3.3: Robot Learning; Spec 3.8: Simulation | Sim-to-real transfer, reinforcement learning in simulation covered in robot learning courses |
| 1.4 | State machines | ⚠️ | Pillar 3: Planning & AI; Pillar 5: Robot Systems Integration | Covered as a subtopic in planning/AI and ROS-based systems courses; not a standalone course |
| 1.5 | Behavior trees | ⚠️ | Pillar 3: Planning & AI | Emerging topic in task planning courses; less formalized than state machines in curricula |
| 1.6 | Using state machines and behavior trees to switch between custom controllers | ⚠️ | Pillar 3: Planning & AI; Pillar 4: Control Systems | Covered at the intersection of planning and control integration; appears in capstone/systems courses |
| 1.7 | Creating digital environments | ✅ | Pillar 5: Simulation environments (Gazebo, Isaac Sim, MuJoCo); Spec 3.8: Simulation & Computational Methods | Simulation environment creation covered in systems integration and sim-to-real courses |
| 1.8 | Programming environment and IRL mapping | ✅ | Pillar 2: SLAM & Perception; Pillar 5: ROS/simulation | Digital twin creation and real-world mapping covered in perception and systems courses |
| 1.9 | Writing custom algorithms | ✅ | All Pillars | Fundamental to every course — algorithm design pervades the entire curriculum |
| 1.10 | Computer vision (OpenCV) | ✅ | Pillar 2: Computer Vision | Core pillar course at all 10 universities; OpenCV is a standard tool |
| 1.11 | Having speed and torque version of controls | ✅ | Pillar 4: Feedback Control Systems; Pillar 5: Mechatronics | Motor control (speed/torque modes) covered in control and mechatronics courses |
| 1.12 | Sensor filtering | ✅ | Pillar 2: Robot Perception; Pillar 4: Optimal Control & Estimation; Foundation 1.2: Signals & Systems | Kalman filtering, particle filters, signal processing covered extensively |
| 1.13 | OpenCV prediction | ✅ | Pillar 2: Computer Vision; Spec 3.3: Deep Learning | Object detection, tracking, and prediction using vision libraries covered in CV and deep learning courses |

---

## 2. Hardware Skills

| # | Skill | Cov. | Curriculum Section | Notes |
|---|-------|------|--------------------|-------|
| 2.1 | Depth and RGB Camera | ✅ | Pillar 2: Sensor Systems & Instrumentation; Pillar 2: Computer Vision | Camera models, calibration, stereo vision, depth estimation are core perception topics |
| 2.2 | Generate collision voxels | ⚠️ | Pillar 3: Motion Planning; Spec 3.8: Robot Dynamics & Simulation | Voxel-based collision representation is a subtopic in motion planning and simulation courses |
| 2.3 | ROS visualization | ✅ | Pillar 5: Robot Operating System (ROS) — RViz | ROS visualization tools (RViz) explicitly covered in systems integration courses |
| 2.4 | IRL sensors into digital representations | ✅ | Pillar 2: Sensor Systems & Instrumentation; Pillar 5: ROS | Sensor interfacing, data acquisition, and digital representation are core systems topics |

---

## 3. Electrical Skills

| # | Skill | Cov. | Curriculum Section | Notes |
|---|-------|------|--------------------|-------|
| 3.1 | Electrical FW (firmware) | ⚠️ | Pillar 5: Electronics for Robotics; Pillar 5: Mechatronics | Embedded firmware covered in mechatronics and electronics courses but not always deeply; more EE-focused programs (MIT 2.678, CMU 16-220) go deeper |

---

## 4. Software Tools

| # | Tool | Cov. | Curriculum Section | Notes |
|---|------|------|--------------------|-------|
| 4.1 | Jetson (NVIDIA) | ⚠️ | Pillar 5: Robot Systems Integration | Used in lab settings at several programs but not a formal course topic; appears in capstone/project courses |
| 4.2 | Simulink | ✅ | Pillar 4: Control Systems; Foundation 1.2: Signals & Systems | Standard tool in control systems courses (MIT 2.004, UMich ROB 301, GT ECE 6550) |
| 4.3 | Gazebo | ✅ | Pillar 5: Simulation environments | Explicitly listed as a key simulation tool in systems integration courses |
| 4.4 | Isaac Sim | ✅ | Pillar 5: Simulation environments; Spec 3.3: Robot Learning | Explicitly listed; used for sim-to-real in robot learning courses |
| 4.5 | ROS | ✅ | Pillar 5: Robot Operating System (ROS) | Core tool across all 10 programs; dedicated coverage in systems courses |
| 4.6 | OpenCV | ✅ | Pillar 2: Computer Vision | Standard library used in all computer vision courses |
| 4.7 | PyTorch (algorithms and training) | ✅ | Spec 3.3: Deep Learning, Reinforcement Learning; Pillar 2: Deep learning for perception | Primary framework for deep learning and robot learning courses |
| 4.8 | RViz | ✅ | Pillar 5: Robot Operating System (ROS) | Standard ROS visualization tool covered in systems integration courses |

---

## 5. Communication Systems

| # | Skill | Cov. | Curriculum Section | Notes |
|---|-------|------|--------------------|-------|
| 5.1 | CAN bus | ⚠️ | Pillar 5: Mechatronics; Pillar 5: Electronics for Robotics | Covered as a subtopic in mechatronics and embedded systems courses; not a standalone course |
| 5.2 | RS232 | ⚠️ | Pillar 5: Mechatronics — Sensor interfacing (UART) | RS232/UART covered as part of serial communication in mechatronics labs |
| 5.3 | EtherCAT | ❌ | — | Industrial fieldbus protocol; not typically covered in academic robotics curricula. More common in industrial automation and industry training |
| 5.4 | Drivers | ⚠️ | Pillar 5: Electronics for Robotics; Foundation 1.3: Computer Systems | Motor drivers covered in electronics courses; software drivers touched in computer systems courses |

---

## 6. Engineering Skills

| # | Skill | Cov. | Curriculum Section | Notes |
|---|-------|------|--------------------|-------|
| 6.1 | Simulating solid systems | ✅ | Spec 3.8: Robot Dynamics & Simulation; Spec 3.8: Computational Design | Rigid body simulation, FEA covered in dynamics and computational courses |
| 6.2 | Simulating hydraulic systems | ❌ | — | Not typically part of robotics curricula; more common in ME fluid mechanics / fluid power courses. Some mechatronics courses may touch on hydraulic actuators |
| 6.3 | System modeling and control | ✅ | Pillar 4: Control Systems (all 4 courses); Foundation 1.2: Signals & Systems | Central to the entire control systems pillar; covered at all 10 universities |
| 6.4 | Differential equations | ✅ | Foundation 1.1: Differential Equations | Prerequisite course required at all 10 programs |
| 6.5 | Linear algebra | ✅ | Foundation 1.1: Linear Algebra | Prerequisite course required at all 10 programs |
| 6.6 | Dynamics | ✅ | Pillar 1: Dynamics of Mechanical Systems; Foundation 1.2: Statics & Dynamics | Core prerequisite and pillar topic at all 10 programs |
| 6.7 | Mechanics | ✅ | Pillar 1: Robot Mechanics; Foundation 1.2: Classical Mechanics, Statics & Dynamics | Foundational topic spanning physics prerequisites and robotics core |
| 6.8 | Fatigue | ❌ | — | Materials science / mechanical engineering topic; not covered in robotics-specific curricula. Would be in a traditional ME materials course (e.g., MIT 2.002) |

---

## Summary

| Category | Total Skills | ✅ Covered | ⚠️ Partial | ❌ Not Covered |
|----------|-------------|-----------|------------|---------------|
| 1. Software Skills | 13 | 10 | 3 | 0 |
| 2. Hardware Skills | 4 | 3 | 1 | 0 |
| 3. Electrical Skills | 1 | 0 | 1 | 0 |
| 4. Software Tools | 8 | 7 | 1 | 0 |
| 5. Communication Systems | 4 | 0 | 3 | 1 |
| 6. Engineering Skills | 8 | 6 | 0 | 2 |
| **Total** | **38** | **26 (68%)** | **9 (24%)** | **3 (8%)** |

### Key Gaps in the Curriculum

The three skills **not covered** by the unified robotics curriculum are:

1. **EtherCAT (5.3)** — Industrial real-time fieldbus protocol used in automation. Academic programs focus on general communication protocols (UART, SPI, I2C) rather than industrial-specific standards.
2. **Simulating hydraulic systems (6.2)** — Covered in traditional Mechanical Engineering fluid power courses, not in robotics-specific curricula. Relevant for heavy-duty industrial and construction robots.
3. **Fatigue (6.8)** — A materials science / structural engineering topic covered in ME materials courses (e.g., MIT 2.002 Mechanics and Materials II) but outside the scope of robotics programs.

### Skills Well-Aligned with Curriculum

The strongest alignment is in:
- **Computer vision, localization, and perception** — Core pillar at all universities
- **Control systems and system modeling** — Universal coverage
- **ROS, Gazebo, simulation tools** — Explicit curriculum content
- **Math foundations (linear algebra, diff. eq., dynamics)** — Required prerequisites everywhere
