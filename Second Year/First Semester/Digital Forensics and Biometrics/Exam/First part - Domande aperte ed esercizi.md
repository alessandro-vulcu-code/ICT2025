# First part · Domande aperte ed esercizi

Tracce in inglese, con formulazione uniformata e ordinate per argomento delle [lezioni della First part](../First%20part/). Le fonti sono indicate sotto ogni traccia. Gli esercizi ripetuti in più documenti compaiono una sola volta.

- [Domande aperte d’esame](#domande-aperte-desame)
- [Esercizi dei materiali del corso](#esercizi-dei-materiali-del-corso)
- [Esercizi e domande di allenamento](#esercizi-e-domande-di-allenamento)

## Domande aperte d’esame

### Acquisizione e conservazione delle evidenze digitali · Lezioni 1–2

**1. Digital evidence handling.** What are the different phases in the acquisition and handling of digital evidence? Who are the main actors involved in each phase and what are their roles? Describe the process in as much detail as possible.

*Fonti* · [Febbraio 2024, domanda 1](DFB_OpenQuestions_Feb2024) · [Telegram, primo parziale, A.1](Questions%20from%20Telegram.txt).

### Intrusion detection systems · Lezioni 5–6

**2. Intrusion detection systems (IDS).** Explain what IDSs are and what they are used for. Describe the different types and how they work, discussing their advantages and disadvantages. Discuss the main triggers on which IDSs are based.

*Fonte* · [Gennaio 2024, domanda 1](DFB_OpenQuestions_Jan2024).

### Camera forensics · Lezioni 9–10

**3. Acquisition-based footprints.** Give an overview of the acquisition-based footprints of digital cameras. How can these traces be used to authenticate an image by associating it with a particular camera or camera model?

*Fonte* · [Febbraio 2024, domanda 2](DFB_OpenQuestions_Feb2024).

**4. Camera ballistics and PRNU.** What is photo-response non-uniformity (PRNU), how does it arise, and how can it be estimated from images? Describe a strategy for matching a questioned image to a specific camera and discuss its limitations.

*Fonte* · [Dicembre 2023, domanda 1.1, p. 1](DFB_Pre_term_exam_Dec2023.pdf#page=1).

### Anomaly detection · Lezione 13

**5. Anomaly detection.** Describe the anomaly detection problem. Discuss different types of anomalies, learning conditions, performance metrics, and machine learning and deep learning strategies, including their advantages and disadvantages.

*Fonte* · [Dicembre 2023, domanda 1.2, p. 1](DFB_Pre_term_exam_Dec2023.pdf#page=1).

**6. WDAD and Local Outlier Factor.** Define anomaly detection. Explain the Well-Defined Anomaly Distribution (WDAD) assumption and describe the Local Outlier Factor (LOF).

*Fonte* · [Telegram, secondo parziale, domanda 1](Questions%20from%20Telegram.txt). Domanda ricostruita dal resoconto. Anomaly detection e WDAD compaiono nella lezione 13, mentre LOF è trattato nella dispensa degli esercizi.

## Esercizi dei materiali del corso

### Dempster–Shafer · Lezione 6

**A.5 / 1.1 · Diagnosing a system failure.** A system failure could be caused by terminal A, B, or C. John and Paul assess evidence from HIDS and NIDS. Use the following masses to combine their opinions under Dempster–Shafer theory. Describe each step and present a table of values.

| Hypothesis | John | Paul |
|---|---:|---:|
| A | 0.80 | 0 |
| B | 0.10 | 0 |
| C | 0 | 0.90 |
| A or B | 0 | 0.05 |
| Uncertainty | 0.10 | 0.05 |

*Fonti* · [Esercizio A.5, p. 2](exercise_solved.pdf#page=2) · [Esercizio 1.1, p. 1](exercise_notes.pdf#page=1).

**A.6 / 1.2 · Combining three IDS sensors.** A network is monitored by three IDS sensors with the masses below. Using Dempster–Shafer theory, how strongly does the combined evidence support the hypothesis that the network is under attack?

| Decision | Sensor A | Sensor B | Sensor C |
|---|---:|---:|---:|
| Attack | 0.30 | 0.35 | 0.35 |
| Safe | 0.20 | 0.25 | 0.10 |
| Uncertainty | 0.50 | 0.40 | 0.55 |

*Fonti* · [Esercizio A.6, p. 1](exercise_solved.pdf#page=1) · [Esercizio 1.2, p. 2](exercise_notes.pdf#page=2).

**1.3 · Suspicious package.** Two guards monitor a warehouse. Guard A assigns 0.70 to a package containing illegal items and 0.10 to harmless contents. Guard B assigns 0.50 to harmless contents and 0.40 to dangerous contents. What do they decide after combining their assessments using Dempster–Shafer theory? Should they inspect the package?

*Fonte* · [Esercizio 1.3, pp. 3–4](exercise_notes.pdf#page=3).

**1.4 · City power outage.** An electrical engineer assigns 0.50 to transformer failure, 0.30 to power overload, and 0.20 to uncertainty. A security expert assigns 0.40 to sabotage, 0.40 to natural or technical causes, and 0.20 to uncertainty. A weather analyst assigns 0.60 to a storm, 0.30 to causes unrelated to weather, and 0.10 to uncertainty. Define the possible hypotheses, combine the evidence, and comment on the result.

*Fonte* · [Esercizio 1.4, pp. 4–5](exercise_notes.pdf#page=4).

**1.5 · Declining bird population.** An ornithologist assigns 0.60 to disease, 0.30 to food shortage due to habitat destruction, and 0.10 to uncertainty. An environmental scientist assigns 0.50 to habitat destruction, 0.40 to pollution, and 0.10 to uncertainty among human-related causes. Define the possible hypotheses, combine the evidence, and comment on the result.

*Fonte* · [Esercizio 1.5, p. 6](exercise_notes.pdf#page=6).

### Local Outlier Factor · Lezione 13

**2.1.** Given the two-dimensional feature space below, compute the LOF score for point **6** using the second-nearest-neighbor distance ($k=2$).

![Feature space for exercise 2.1, with point 6 marked in red](Pics/First%20part/lof-2-1.png)

*Fonte* · [Esercizio 2.1, p. 8](exercise_notes.pdf#page=8).

**2.2.** Given the two-dimensional feature space below, compute the LOF score for point **6** using the second-nearest-neighbor distance ($k=2$).

![Feature space for exercise 2.2, with point 6 marked in red](Pics/First%20part/lof-2-2.png)

*Fonte* · [Esercizio 2.2, p. 10](exercise_notes.pdf#page=10).

**2.3.** Given the two-dimensional feature space below, compute the LOF score for point **5** using the second-nearest-neighbor distance ($k=2$).

![Feature space for exercise 2.3, with point 5 marked in red](Pics/First%20part/lof-2-3.png)

*Fonte* · [Esercizio 2.3, p. 11](exercise_notes.pdf#page=11).

**2.4.** Given the two-dimensional feature space below, compute the LOF score for point **5** using the second-nearest-neighbor distance ($k=2$).

![Feature space for exercise 2.4, with point 5 marked in red](Pics/First%20part/lof-2-4.png)

*Fonte* · [Esercizio 2.4, p. 12](exercise_notes.pdf#page=12).

**2.5.** Given the two-dimensional feature space below, compute the LOF score for point **5** using the second-nearest-neighbor distance ($k=2$).

![Feature space for exercise 2.5, with point 5 marked in red](Pics/First%20part/lof-2-5.png)

*Fonte* · [Esercizio 2.5, pp. 13–14](exercise_notes.pdf#page=14).

### Isolation Forest · Lezione 13

Il [resoconto Telegram del primo parziale](Questions%20from%20Telegram.txt) segnala un esercizio «IF» senza riportarne la traccia. Le tre tracce qui sotto provengono dalla dispensa del corso.

**3.1.** Construct two isolation trees that classify point **5** as anomalous, given an expected depth of **1.7**. Compute the anomaly score.

![Feature space for exercise 3.1, with point 5 marked in red](Pics/First%20part/isolation-forest-3-1.png)

*Fonte* · [Esercizio 3.1, p. 15](exercise_notes.pdf#page=15).

**3.2.** Construct two isolation trees that classify point **5** as anomalous, given an expected depth of **1.7**. Compute the anomaly score.

![Feature space for exercise 3.2, with point 5 marked in red](Pics/First%20part/lof-2-5.png)

*Fonte* · [Esercizio 3.2, p. 18](exercise_notes.pdf#page=18).

**3.3.** Construct two isolation trees that classify point **6** as anomalous, given an expected depth of **1.7**. Compute the anomaly score.

![Feature space for exercise 3.3, with point 6 marked in red](Pics/First%20part/isolation-forest-3-3.png)

*Fonte* · [Esercizio 3.3, p. 20](exercise_notes.pdf#page=20).

## Esercizi e domande di allenamento

**OPEN-02 · Live acquisition.** An authorized responder arrives at a hospital. A running workstation supports an ongoing service, and relevant data exist only in volatile memory. The service cannot be interrupted. Explain which acquisition strategy you would choose, what you would document, how you would verify the exported files after transfer, and what belongs in the chain of custody.

*Fonte* · [Quiz self-made, OPEN-02, indicato come AI made](Self%20made/Quiz%20primo%20midterm%20-%20Digital%20Forensics%20and%20Biometrics.md#open-question).

**OPEN-06 · Combining two IDS sensors.** The frame of discernment is $\Theta=\{A,S\}$, where $A$ means attack and $S$ means safe. Combine the assessments below using Dempster’s normalized rule. Show the conflict and unnormalized masses, compute the final masses, and give the belief and plausibility of attack. Explain what the mass on $\Theta$ represents.

| Focal set | Sensor 1 | Sensor 2 |
|---|---:|---:|
| $\{A\}$ | 0.45 | 0.35 |
| $\{S\}$ | 0.15 | 0.30 |
| $\Theta$ | 0.40 | 0.35 |

*Fonte* · [Quiz self-made, OPEN-06, indicato come AI made](Self%20made/Quiz%20primo%20midterm%20-%20Digital%20Forensics%20and%20Biometrics.md#open-question-1).

### Esercizi con dati adattati dalle domande a scelta multipla

**Q013 · Comparing classifiers.** SVM classifiers identify which Android app generated a stream of packet lengths. All were trained on the same dataset of 1,000 vectors. Compare the four configurations below and justify which you would choose, considering both accuracy and the number of support vectors.

| Configuration | Support vectors | Accuracy |
|---|---:|---:|
| A | 10 | 92% |
| B | 30 | 97% |
| C | 900 | 99.5% |
| D | 100 | 97% |

*Fonte* · [Dicembre 2023, quiz, domanda 13, p. 6](DFB_Pre_term_exam_Dec2023.pdf#page=6). La traccia menziona cinque classificatori e fornisce dati per quattro.

**AI-06-04 · Belief and plausibility.** Let $\Theta=\{A,S\}$, where $A$ means attack and $S$ means safe. Given $m(\{A\})=0.40$, $m(\{S\})=0.35$, and $m(\Theta)=0.25$, compute the belief and plausibility of attack.

*Fonte* · [Quiz self-made, AI-06-04](Self%20made/Quiz%20primo%20midterm%20-%20Digital%20Forensics%20and%20Biometrics.md#evidence-fusion-and-dempstershafer-theory).

**AI-13-09 · Precision and recall.** A detector produces 12 true positives, 3 false positives, and 8 false negatives. Compute its precision and recall.

*Fonte* · [Quiz self-made, AI-13-09](Self%20made/Quiz%20primo%20midterm%20-%20Digital%20Forensics%20and%20Biometrics.md#anomaly-detection).
