# CWAS-rsfMRI

The main goal of the `cwas-rsfmri` pipeline is to provide a easy and semi-flexible workflow to perform Connectome Wide Association Study (CWAS) on fmri connectivity matrix.
This app follows a BIDS-App workflow.

## 📌 Documentation
###  Website with full documentation
To run this pipeline, see the full documentation here : https://brainhack-school2025.github.io/elkhantour_project/ 

### Quick start
First you need to clone the repository
```
git clone https://github.com/brainhack-school2025/elkhantour_project.git
```

Then install the package

```
pip install -e .
```

### Week 2 project overview slides 🔧
This project is developed as part of BrainHack School 2025 in Montreal. The Week 2 project overview slides are available [here](https://docs.google.com/presentation/d/1BFQEd32ZGSvIpQaBQh5KjRjrZ0RL78illSvqR80Dr_E/edit?usp=sharing).

### Week 4 final presentation 🚀
The Week 4 project overview slides are available [here](https://docs.google.com/presentation/d/1AT7jvhL63toRHIYBsFZYHyxpPp-cLphSkeC5kAkJMak/edit?usp=sharing).

## 📚 Background 
The reproducibility crisis in neuroimaging has affected many research domains, and psychiatric research is no exception <sup>[1](https://doi.org/10.1016/j.bpsc.2022.12.006)</sup>. 

To address this issue, initiatives such as the ENIGMA consortium (Enhancing NeuroImaging Genetics through Meta-Analyses) were launched <sup>[2](https://doi.org/10.1007/s11682-013-9269-5)</sup>. ENIGMA is a consortium comprising numerous research sites and organized into several Disease Working Groups that focus on most major psychiatric conditions. It promotes a collaborative framework: while data remain at local sites, analyses follow standardized protocols, enabling large-scale meta-analyses across cohorts.

This approach has proven successful for structural and diffusion MRI, thanks to the development of open and reproducible protocols (https://enigma.ini.usc.edu/protocols/). In this context, Waller et al., 2020 developed HALFpipe <sup>[3](https://doi.org/10.1002/hbm.25829)</sup>, an open-source software that facilitates the preprocessing and extraction of connectivity matrices from functional MRI data. However, no standard tools has yet been proposed by ENIGMA for statistical analyses of functional connectivity matrices.

## 🎯 Objectives
This project aims to support the broader collaborative effort by developing a dedicated library for conducting Connectome-Wide Association Studies (CWAS) based on connectivity matrices from BIDS-formatted data.

### Objectives for BrainHack school
Learn how to : 
1. Write scripts in python following the BIDS-app workflow 
2. Build a GitHub repository with automated tests with GitHub Actions
3. Develop a sustainable and easy-to-use python package
4. Produce interactive plots and interactive website ✨
 
<img title="Workflow of the pipeline" alt="Alt text" src="workflow.svg">

## 🧰 Tools used in Brain Hack School
This project uses the following tools and standards to ensure reproducibility, openness, and long-term usability:
- **Python scripts** : To write functions and be able to test them
- **Git & GitHub**: 
   - Enables version control and promotes open-source, collaborative development of the library.
   - Implements automated testing and continuous integration to maintain code quality during development (Git Actions).
- **BIDS Ecosystem**: Ensures compatibility with the BIDS standard, following the workflow of a BIDS App ([4](https://doi.org/10.1371/journal.pcbi.1005209)).
- **Python Packaging with uv**: Distributes the tool as an installable open-source Python library for easy integration and reuse.
- Interactive documentation : Provides runnable examples directly on the website for users to test and explore.
   - **Jupyter Notebooks**
   - **Plots with Plotly**
   - **Website with MyST**

## 🧠 Data 
To test each the integration of the pipeline, toy data will be generated.

The data have been generated randomly using `numpy`. 

## 🗓️ Deliverables in Week 4
*Code development:*
- Python scripts with functions to perform the CWAS
- A GitHub repository that automatically test the integration from users using Github Actions
- A python package ready to be used

*Documentation:*
- [A website](https://brainhack-school2025.github.io/elkhantour_project/) 
   - documentation to run and install the Library
   - interactive notebooks & plots


## 📖 References
1. 	Botvinik-Nezer R, Wager TD. Reproducibility in neuroimaging analysis: Challenges and solutions. Biol Psychiatry Cogn Neurosci Neuroimaging. 2023;8: 780–788.
2. 	Thompson PM, Stein JL, Medland SE, Hibar DP, Vasquez AA, Renteria ME, et al. The ENIGMA Consortium: large-scale collaborative analyses of neuroimaging and genetic data. Brain Imaging Behav. 2014;8: 153–182.
3. 	Waller L, Erk S, Pozzi E, Toenders YJ, Haswell CC, Büttner M, et al. ENIGMA HALFpipe: Interactive, reproducible, and efficient analysis for resting-state and task-based fMRI data. Hum Brain Mapp. 2022;43: 2727–2742.
4. 	Gorgolewski KJ, Alfaro-Almagro F, Auer T, Bellec P, Capotă M, Chakravarty MM, et al. BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging data analysis methods. PLoS Comput Biol. 2017;13: e1005209.

## ✨ Aknowledgements
This library will be based on previous published code by Dr. Clara A. Moreau & Dr. Sebastian Urchs.

The original version of the scripts can be found here : https://github.com/claramoreau9/NeuropsychiatricCNVs_Connectivity

Thanks to Sara & Cleo for their help to create the Myst website! 