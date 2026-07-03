from manim import *
import numpy as np

class BipartiteMorph(Scene):
    def construct(self):
        
        ###################################
        # GRAPH 1: The Bipartite Original #
        ###################################
        
        vertices_1 = list(range(1, 13))
        edges_1 = [
            (1, 2), (2, 3), (3, 4), (4, 1),
            (3, 5), (5, 6),
            (6, 7), (7, 8), (8, 9), (9, 6),
            (4, 10), (10, 11), (11, 12)
        ]

        group_U1 = [1, 3, 6, 8, 10, 12] 
        group_V1 = [2, 4, 5, 7, 9, 11]  

        bipartite_layout = {}
        for i, v in enumerate(group_U1):
            bipartite_layout[v] = np.array([-5, 3 - i * 1.2, 0])
        for i, v in enumerate(group_V1):
            bipartite_layout[v] = np.array([-2, 3 - i * 1.2, 0])

        raw_spatial_layout = {
            1: [-5, 1, 0], 2: [-4, 2, 0], 3: [-3, 1, 0], 4: [-4, 0, 0], 
            5: [-1, 1, 0], 
            6: [1, 1, 0], 7: [2, 2, 0], 8: [3, 1, 0], 9: [2, 0, 0], 
            10: [-4, -1.5, 0], 11: [-2.5, -1.5, 0], 12: [-1, -1.5, 0]   
        }

        spatial_layout_1 = {
            k: np.array([v[0] * 0.6 - 1.5, v[1] * 0.6, 0]) for k, v in raw_spatial_layout.items()
        }

        graph_1 = Graph(
            vertices_1, edges_1,
            layout=bipartite_layout,
            vertex_config={v: {"fill_color": RED} for v in group_U1} |
                          {v: {"fill_color": BLUE} for v in group_V1},
            edge_config={"stroke_width": 3, "stroke_color": WHITE},
            labels=True 
        )


        ##########################################
        # GRAPH 2: The Non-Bipartite (Odd Cycle) #
        ##########################################
        
        vertices_2 = [13, 14, 15, 16, 17]
        edges_2 = [(13, 14), (14, 15), (15, 13), (15, 16), (16, 17)]
        
        group_U2 = [13, 16] 
        group_V2 = [14, 17] 
        group_W2 = [15]     

        tripartite_layout = {
            13: [2, 1, 0], 16: [2, -1, 0], 
            14: [4, 1, 0], 17: [4, -1, 0],  
            15: [6, 0, 0]                   
        }

        spatial_layout_2 = {
            13: [3, 1, 0],
            14: [5, 1, 0],
            15: [4, 2.5, 0], 
            16: [4, -0.5, 0],
            17: [4, -2, 0]
        }

        graph_2 = Graph(
            vertices_2, edges_2,
            layout=tripartite_layout,
            vertex_config={v: {"fill_color": RED} for v in group_U2} |
                          {v: {"fill_color": BLUE} for v in group_V2} |
                          {v: {"fill_color": GREEN} for v in group_W2},
            edge_config={"stroke_width": 3, "stroke_color": WHITE},
            labels=True
        )


        #############################
        # Here starts the animation #
        #############################
        
        self.play(Create(graph_1), Create(graph_2), run_time=3)
        self.wait(1.5)

        self.play(
            graph_1.animate.change_layout(spatial_layout_1),
            graph_2.animate.change_layout(spatial_layout_2), 
            run_time=4
        )
        self.wait(3)

        self.play(
            graph_1.animate.change_layout(bipartite_layout),
            graph_2.animate.change_layout(tripartite_layout), 
            run_time=4
        )
        self.wait(3)