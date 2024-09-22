import matplotlib.pyplot as plt
import networkx as nx

# Erstellen des Graphen
G = nx.DiGraph()

# Hauptthemen als Nodes (Knoten)
main_topics = {
    "Fortschritt": "Wirtschaftlicher & sozialer Fortschritt",
    "GASP": "Gemeinsame Außen- & Sicherheitspolitik (GASP)",
    "Polizei": "Polizeiliche & Justizielle Zusammenarbeit",
    "Zusammenarbeit": "Verstärkte Zusammenarbeit",
    "Visa": "Visa, Asyl, Einwanderung",
    "Beschäftigung": "Beschäftigung",
    "Reformen": "Institutionelle Reformen"
}

# Sub-Themen als Knoten und deren Verbindungen
subpoints = {
    "GASP": ["Gemeinsame Strategien & Aktionen", 
             "Hoher Vertreter für GASP", 
             "Verbindung zur Westeuropäischen Union", 
             "Koordination in internationalen Organisationen"],
    "Polizei": ["Kriminalitätsbekämpfung", 
                "Justizielle Zusammenarbeit"],
    "Zusammenarbeit": ["Flexiblere Zusammenarbeit"],
    "Visa": ["Einheitliche Regelungen", 
             "Schengen-Abkommen"],
    "Beschäftigung": ["Förderung hoher Beschäftigung"],
    "Reformen": ["Gesetzgebungsverfahren", 
                 "Europäisches Parlament", 
                 "Europäische Kommission"]
}

# Hauptpunkte hinzufügen
for key, topic in main_topics.items():
    G.add_node(topic)

# Subpunkte und Verbindungen hinzufügen
for key, sublist in subpoints.items():
    for sub in sublist:
        G.add_node(sub)
        G.add_edge(main_topics[key], sub)

# Position der Nodes festlegen (Spring Layout für bessere Darstellung)
pos = nx.spring_layout(G, k=2, seed=42)

# Zeichnen der Nodes
plt.figure(figsize=(12, 10))

# Zeichnen der Knoten (Main Topics)
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue', 
                       nodelist=main_topics.values(), node_shape="s", alpha=0.9)

# Zeichnen der Knoten (Subpoints)
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='lightgreen', 
                       nodelist=[sub for sublist in subpoints.values() for sub in sublist], node_shape="o", alpha=0.8)

# Zeichnen der Verbindungen
nx.draw_networkx_edges(G, pos, arrows=False, width=2, alpha=0.5)

# Beschriftung der Nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_weight="bold")

# Diagramm anzeigen
plt.title("Vertrag von Amsterdam: Hauptthemen und Unterpunkte", fontsize=15)
plt.axis('off')
plt.tight_layout()
plt.show()