# kegg_pathway_analyzer.py

import requests
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

def fetch_kgml_data(pathway_id):
    url = f"http://rest.kegg.jp/get/{pathway_id}/kgml"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_kgml_data(kgml_content):
    root = ET.fromstring(kgml_content)
    reactions = []
    for reaction in root.findall(".//reaction"):
        reaction_name = reaction.get('name')
        substrates = [substrate.get('name') for substrate in reaction.findall("substrate")]
        products = [product.get('name') for product in reaction.findall("product")]
        reactions.append(f"{reaction_name}: {' + '.join(substrates)} -> {' + '.join(products)}")
    return reactions

def create_network(reactions):
    G = nx.DiGraph()
    for reaction in reactions:
        parts = reaction.split(': ')
        if len(parts) == 2:
            reaction_name, equation = parts
            if '->' in equation:
                substrates, products = equation.split('->')
                for substrate in substrates.split('+'):
                    for product in products.split('+'):
                        G.add_edge(substrate.strip(), product.strip(), reaction=reaction_name)
    return G

def visualize_network(G):
    plt.figure(figsize=(16, 12))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=3000, font_size=6, font_weight='bold', 
            arrows=True, arrowsize=10, edge_color='gray')
    
    edge_labels = nx.get_edge_attributes(G, 'reaction')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=5)
    
    plt.title("Metabolic Pathway Network")
    plt.savefig("metabolic_pathway.png", dpi=300, bbox_inches='tight')
    plt.close()

def main():
    pathway_id = "hsa00020"  # Citrate cycle (TCA cycle) pathway for human
    
    try:
        kgml_content = fetch_kgml_data(pathway_id)
        reactions = parse_kgml_data(kgml_content)
        
        print(f"Number of reactions found: {len(reactions)}")
        print("First few reactions:")
        for reaction in reactions[:5]:
            print(reaction)
        
        df = pd.DataFrame(reactions, columns=['Reaction'])
        df.to_csv('pathway_data.csv', index=False)
        print("Pathway data saved to 'pathway_data.csv'")
        
        G = create_network(reactions)
        visualize_network(G)
        
        print(f"Number of metabolites: {G.number_of_nodes()}")
        print(f"Number of reactions: {G.number_of_edges()}")
        
    except requests.RequestException as e:
        print(f"Error fetching pathway data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
