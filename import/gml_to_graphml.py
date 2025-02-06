import networkx as nx # type: ignore

class GraphConverter:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.graph = None

    def load_graph(self) -> None:
        """Loads the graph from a GML file."""
        self.graph = nx.read_gml(self.input_file)
        print(f"Loaded graph from {self.input_file}")

    def convert_to_graphml(self) -> None:
        """Converts the loaded graph to GraphML format."""
        if self.graph is None:
            raise ValueError("Graph not loaded. Call load_graph() first.")
        
        nx.write_graphml(self.graph, self.output_file)
        print(f"Converted {self.input_file} to {self.output_file}")

    def run(self) -> None:
        """Executes the graph conversion process."""
        self.load_graph()
        self.convert_to_graphml()


if __name__ == "__main__":
    converter = GraphConverter("import/simple.gml", "simple.graphml")
    converter.run()