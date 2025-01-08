# Pretria: AI-Based Web Application for Pre-Triage Using GPT-3

This repository contains the code for the development of an AI-based web application designed to enhance pre-triage processes in after-hour medical care. The project combines advanced natural language processing capabilities of GPT-3 with user-friendly web technologies to provide an innovative solution to challenges in organized duty centers (ODCs).

The project was created in 2023 as a part of my Thesis for obtaining the Master `Business Engineering, Management Information Systems` at the University of Antwerp. Afterwards, minor updates have been made to the code itself, other than some necessary bug-fixes to keep the prototype allive, which you can visit at[Pretria](https://www.pretria.com). Note that you require an account to access certain functionalities (differential diagnoses, follow-up system, doctor's dashboard, etc.).

If you wish to gain access to the above features, or wish to receive more information about the Thesis project, don't hesistate to contact me at <bloomer.david@outlook.com>.

## Table of Contents

- [Pretria: AI-Based Web Application for Pre-Triage Using GPT-3](#pretria-ai-based-web-application-for-pre-triage-using-gpt-3)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Motivation](#motivation)
  - [Research Objectives](#research-objectives)
  - [Research Methodology](#research-methodology)
    - [1. Problem Identification](#1-problem-identification)
    - [2. Solution Design](#2-solution-design)
    - [3. Evaluation](#3-evaluation)
  - [System Design and Development](#system-design-and-development)
    - [Features](#features)
    - [Technologies Used](#technologies-used)
  - [Evaluation](#evaluation)
    - [Accuracy](#accuracy)
    - [Goal Achievement](#goal-achievement)
    - [Economic and Technical Feasibility](#economic-and-technical-feasibility)
  - [Results](#results)
  - [Limitations and Future Work](#limitations-and-future-work)
    - [Current Limitations](#current-limitations)
    - [Future Enhancements](#future-enhancements)
  - [License](#license)

---

## Overview

This thesis project introduces an AI-powered web application aimed at improving the pre-triage and consultation process in organized duty centers. The application uses OpenAI's GPT-3 to process patient inputs, generate triage questions, predict outcomes, and support healthcare professionals during consultations.

## Motivation

The research addresses significant challenges in Belgium’s after-hour healthcare system, particularly in ODCs, such as:
- Inefficiencies in telephone pre-triage.
- Administrative burdens on general practitioners (GPs).
- Limitations of existing symptom checkers (e.g., lack of follow-up systems, risk aversion, and absence of flexible patient input).

These issues often result in suboptimal patient outcomes and increased workloads for healthcare professionals. This project aims to bridge these gaps by leveraging cutting-edge AI technology.

## Research Objectives

The project sought to answer three main research questions:
1. **How can an AI-based pre-triage system using GPT-3 be implemented, and how can it support follow-up systems?**
2. **What are the current challenges in the pre-triage and consultation processes in ODCs in Belgium?**
3. **How can large language models like GPT-3 be utilized for structured multi-class classification tasks in healthcare?**

---

## Research Methodology

The research methodology followed the **Design Science Research (DSR) Framework**, which emphasizes the design and evaluation of innovative artifacts in response to identified problems. The following steps were carried out:

### 1. Problem Identification
- Conducted **literature reviews** to analyze existing triage systems, symptom checkers, and after-hour care models.
- Performed **expert interviews** with healthcare professionals, including general practitioners and ODC staff, to understand practical challenges.
- Analyzed data from **iCAREdata**, a large database of after-hour patient consultations, to identify inefficiencies and anomalies in triage processes.

### 2. Solution Design
- Designed a modular web application using UML diagrams, sequence diagrams, and entity-relationship models.
- Incorporated GPT-3 for dynamic question generation, differential diagnosis prediction, and triage outcome determination.
- Emphasized user-centered design principles, creating intuitive interfaces for both patients and medical staff.

### 3. Evaluation
- Conducted **simulation studies** using 45 standardized patient vignettes to assess diagnostic and triage accuracy.
- Performed **qualitative evaluations** with healthcare experts to validate the application's effectiveness and feasibility.
- Analyzed economic viability and technical scalability through cost analysis and prototyping.

---

## System Design and Development

### Features
1. **Pre-Triage System**: Automates symptom assessment and assigns urgency labels based on patient input.
2. **Follow-Up System**: Links pre-triage data to consultations, ensuring continuity of care.
3. **Dynamic Question Generation**: Generates relevant follow-up questions using GPT-3 based on patient input.
4. **Digital Dashboard**: Provides practitioners with a comprehensive overview of patient data and a digital waiting room.

### Technologies Used
- **Front-End**: React.js and Bootstrap CSS.
- **Back-End**: Django framework with RESTful APIs.
- **AI Model**: GPT-3 via OpenAI API.
- **Database**: PostgreSQL.

---

## Evaluation

### Accuracy
- **Diagnostic Accuracy**: GPT-3 listed the correct diagnosis in its top 3 predictions for 100% of cases and ranked it first in 84.4% of cases.
- **Triage Accuracy**: The correct urgency label was predicted in 73% of cases.

### Goal Achievement
- Expert evaluations confirmed the system effectively addressed key challenges in ODCs, such as improving triage accuracy and reducing administrative burdens.

### Economic and Technical Feasibility
- The application was deemed cost-effective and scalable for integration into existing healthcare infrastructures.

---

## Results

1. **Improved Pre-Triage Accuracy**: Demonstrated higher accuracy in assigning urgency labels compared to human receptionists, with reduced rates of under-triage and over-triage.
2. **Effective Use of GPT-3**: Leveraged in-context learning to generate high-quality triage questions and differential diagnoses.
3. **Enhanced Workflow**: Streamlined the patient journey by linking pre-triage data to consultation outcomes, reducing redundant administrative tasks for GPs.

---

## Limitations and Future Work

### Current Limitations
- **Potential Bias**: GPT-3’s training data may include biases that affect predictions.
- **Data Sources**: Simulated patient vignettes limit real-world applicability.
- **Language Support**: The system primarily supports English, with limited testing in Dutch.

### Future Enhancements
- Integrate GPT-4 or similar advanced models for improved accuracy and multilingual capabilities.
- Conduct longitudinal studies with real-world patient data to validate effectiveness.
- Expand the system to include predictive analytics for healthcare resource allocation.

---

## License
By contributing to this project, you agree that your contributions will be licensed under the AGPL v3 and may be used in commercially licensed versions of this software.

This project is licensed under the [GNU Affero General Public License v3](LICENSE.txt).

For commercial licensing options, please contact [bloomer.david@outlook.com](mailto:bloomer.david@outlook.com).
 