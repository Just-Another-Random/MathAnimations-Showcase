from manim import *
import numpy as np

class GraphTours(Scene):
    def construct(self):
        
        ###############
        # Graph Setup #
        ###############
        
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [
            (1,2), (1,3), (1,7), (1,8),
            (2,6), (2,7), (2,8),
            (3,4), (3,5), (3,7),
            (4,5), (4,6), (4,8),
            (5,6), (5,8),
            (6,7)
        ]

        node_order = [5, 6, 7, 1, 2, 3, 4]
        layout = {}
        radius = 3.0 
        
        for i, node in enumerate(node_order):
            angle = np.pi / 2 + i * (2 * np.pi / 7)
            layout[node] = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
        layout[8] = np.array([0, 0.7, 0]) 

        v_config = {"radius": 0.4, "color": GRAY_C, "fill_opacity": 1}
        e_config = {"color": WHITE, "stroke_width": 2.5}

        #####################
        # Paint both Graphs #
        #####################
        
        graph_euler = Graph(vertices, edges, layout=layout, labels=True, vertex_config=v_config, edge_config=e_config)
        graph_hamilton = Graph(vertices, edges, layout=layout, labels=True, vertex_config=v_config, edge_config=e_config)

        for g in [graph_euler, graph_hamilton]:
            for edge in g.edges.values():
                edge.set_z_index(0)
            
            for v in g.vertices:
                g.vertices[v].set_z_index(1)
                g._labels[v].set_color(BLACK).set_z_index(3)

        graph_euler.scale(0.7).shift(LEFT * 3.5)
        graph_hamilton.scale(0.7).shift(RIGHT * 3.5)

        title_euler = Text("Euler Tour (All Edges)", font_size=24).next_to(graph_euler, UP)
        title_hamilton = Text("Hamiltonian Tour (All Nodes)", font_size=24).next_to(graph_hamilton, UP)

        self.play(
            Create(graph_euler), Create(graph_hamilton),
            Write(title_euler), Write(title_hamilton),
            run_time=3
        )
        self.wait(1)

        ####################
        # Define the Paths #
        ####################
        
        euler_path = [1,2,8,4,5,3,4,6,2,7,3,1,8,5,6,7,1]
        hamilton_path = [1,2,8,4,5,6,7,3,1]

        def get_edge(g, u, v):
            # reverses the direction of an edge if needed
            if (u, v) in g.edges: return g.edges[(u, v)]
            if (v, u) in g.edges: return g.edges[(v, u)]

        #######################
        # Text Trackers Setup #
        #######################
        
        # Create groups of individual numbers for the paths
        euler_text_group = VGroup(*[Text(str(n), font_size=24, color=RED) for n in euler_path])
        euler_text_group.arrange(RIGHT, buff=0.05).next_to(graph_euler, DOWN, buff=0.5)

        hamilton_text_group = VGroup(*[Text(str(n), font_size=24, color=BLUE) for n in hamilton_path])
        hamilton_text_group.arrange(RIGHT, buff=0.1).next_to(graph_hamilton, DOWN, buff=0.5)

        ########################
        # Euler Tour Animation #
        ########################
        
        # Create the painting dot at the starting node
        euler_dot = Dot(graph_euler.vertices[euler_path[0]].get_center(), color=RED, radius=0.15, z_index=2)
        self.add(euler_dot)

        # Reveal the first number in the sequence
        self.play(Write(euler_text_group[0]), run_time=0.4)

        # Loop through the path
        for i in range(len(euler_path) - 1):
            u = euler_path[i]
            v = euler_path[i+1]
            edge = get_edge(graph_euler, u, v)

            # Move dot, color edge, and reveal the next number
            self.play(
                euler_dot.animate.move_to(graph_euler.vertices[v].get_center()),
                edge.animate.set_color(RED),
                Write(euler_text_group[i+1]),
                run_time=0.4
            )

        self.wait(1)

        ##############################
        # Hamiltonian Tour Animation #
        ##############################
        
        # Create the painting dot at the starting node
        hamilton_dot = Dot(graph_hamilton.vertices[hamilton_path[0]].get_center(), color=BLUE, radius=0.15, z_index=2)
        self.add(hamilton_dot)

        # Reveal the first number in the sequence and color first point
        self.play(Write(hamilton_text_group[0]), run_time=0.4)
        graph_hamilton.vertices[hamilton_path[0]].set_color(BLUE)
        graph_hamilton._labels[hamilton_path[0]].set_color(BLACK)

        # Loop through the path
        for i in range(len(hamilton_path) - 1):
            u = hamilton_path[i]
            v = hamilton_path[i+1]
            edge = get_edge(graph_hamilton, u, v)

            # Move dot, color vertex, and reveal the next number
            self.play(
                hamilton_dot.animate.move_to(graph_hamilton.vertices[v].get_center()),
                edge.animate.set_color(BLUE),
                graph_hamilton.vertices[v].animate.set_color(BLUE),
                graph_hamilton._labels[v].animate.set_color(BLACK), # <--- The Magic Fix
                Write(hamilton_text_group[i+1]),
                run_time=0.6
            )

        self.wait(2)