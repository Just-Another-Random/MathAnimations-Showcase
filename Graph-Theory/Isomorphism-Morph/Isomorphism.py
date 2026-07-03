from manim import *
import numpy as np

class Isomorphism(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 1. Define the Prism Graph: (a), (b), and (d)
        # ---------------------------------------------------------
        vertices_prism = [1, 2, 3, 4, 5, 6]
        
        # Triangles: (1,2,3) and (4,5,6). Matching diagonals: 1-4, 2-5, 3-6.
        edges_prism = [
            (1, 2), (2, 3), (3, 1), 
            (4, 5), (5, 6), (6, 4),  
            (1, 4), (2, 5), (3, 6)   
        ]
        
        # Layout (a) - 3D Perspective 
        layout_a = {
            1: [-4.5, -1.0, 0], 2: [-2.5, -1.0, 0], 3: [-3.5,  0.5, 0],
            4: [-3.0, -0.2, 0], 5: [-1.0, -0.2, 0], 6: [-2.0,  1.3, 0]
        }
        
        # Layout (b) - Planar Concentric 
        layout_b = {
            1: [-5.0, -1.0, 0], 2: [-1.0, -1.0, 0], 3: [-3.0,  2.0, 0],
            4: [-3.8, -0.2, 0], 5: [-2.2, -0.2, 0], 6: [-3.0,  0.8, 0]
        }
        
        # Layout (d) - Hexagram (Star of David) + Main Diagonals
        r = 2.0
        layout_d = {
            1: [-3 + r * np.cos(np.pi/2),   r * np.sin(np.pi/2),   0], # Top
            2: [-3 + r * np.cos(7*np.pi/6), r * np.sin(7*np.pi/6), 0], # Bottom Left
            3: [-3 + r * np.cos(11*np.pi/6),r * np.sin(11*np.pi/6),0], # Bottom Right
            4: [-3 + r * np.cos(3*np.pi/2), r * np.sin(3*np.pi/2), 0], # Bottom (Opposite Top)
            5: [-3 + r * np.cos(np.pi/6),   r * np.sin(np.pi/6),   0], # Top Right
            6: [-3 + r * np.cos(5*np.pi/6), r * np.sin(5*np.pi/6), 0]  # Top Left
        }
        
        # ---------------------------------------------------------
        # 2. Define Graph 2: Complete Bipartite K_3,3 (c)
        # ---------------------------------------------------------
        vertices_k33 = [7, 8, 9, 10, 11, 12]
        edges_k33 = [
            (7, 10), (7, 11), (7, 12),
            (8, 10), (8, 11), (8, 12),
            (9, 10), (9, 11), (9, 12)
        ]
        
        # Layout (c) - Standard Vertical Columns
        layout_c = {
            7:  [2.0,  1.5, 0], 8:  [2.0,  0.0, 0], 9:  [2.0, -1.5, 0],
            10: [4.0,  1.5, 0], 11: [4.0,  0.0, 0], 12: [4.0, -1.5, 0]
        }
        
        # ---------------------------------------------------------
        # 3. Create the Visual Objects
        # ---------------------------------------------------------
        graph_prism = Graph(
            vertices_prism, edges_prism, layout=layout_a,
            vertex_config={"radius": 0.15, "color": BLUE},
            edge_config={"stroke_width": 2, "color": WHITE}
        )
        
        graph_k33 = Graph(
            vertices_k33, edges_k33, layout=layout_c,
            vertex_config={"radius": 0.15, "color": RED},
            edge_config={"stroke_width": 2, "color": WHITE}
        )
        
        label_left = Tex(r"(a)").next_to(graph_prism, DOWN, buff=0.5)
        label_right = Tex(r"(c) $K_{3,3}$ (Non-Isomorphic)").scale(0.8).next_to(graph_k33, DOWN, buff=0.5)
        
        # ---------------------------------------------------------
        # 4. Animation Sequence
        # ---------------------------------------------------------
        # Draw initial layouts (a) and (c)
        self.play(Create(graph_prism), Create(graph_k33), Write(label_left), Write(label_right), run_time=2)
        self.wait(1)
        
        # Morph Prism to (b)
        label_b = Tex(r"(b)").move_to(label_left)
        self.play(
            graph_prism.animate.change_layout(layout_b),
            Transform(label_left, label_b),
            run_time=2
        )
        self.wait(1)
        
        # Morph Prism to (d) 
        label_d = Tex(r"(d)").move_to(label_left)
        self.play(
            graph_prism.animate.change_layout(layout_d),
            Transform(label_left, label_d),
            run_time=2
        )
        self.wait(2)