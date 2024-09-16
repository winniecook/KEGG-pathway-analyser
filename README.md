# Metabolic Pathway Analyzer

This project provides a Python-based tool for analyzing and visualizing metabolic pathways using data from the KEGG database. It focuses on creating network visualizations of pathways, specifically demonstrated with the Citrate Cycle (TCA cycle) pathway.

## Features

- Fetches pathway data from KEGG in KGML format
- Parses KGML data to extract reactions and compounds
- Creates a network graph representation of the pathway
- Generates a visual representation of the metabolic pathway
- Outputs pathway data to CSV format

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/winniecook/KEGG-pathway-analyser.git
   cd KEGG-pathway-analyser
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script with Python:

```
metabolic-pathway-analyzer-8.py
```

By default, the script analyzes the Citrate Cycle (TCA cycle) pathway (KEGG ID: hsa00020). To analyze a different pathway, modify the `pathway_id` variable in the `main()` function.

## Output

The script generates the following outputs:

1. `metabolic_pathway.png`: A visualization of the metabolic pathway
2. `pathway_data.csv`: A CSV file containing the reaction data

## Customization

- To analyze a different pathway, change the `pathway_id` in the `main()` function
- Adjust visualization parameters in the `visualize_network()` function as needed

