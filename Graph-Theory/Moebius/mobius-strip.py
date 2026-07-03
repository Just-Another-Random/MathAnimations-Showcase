from manim import *
import numpy as np

class MobiusPlot(ThreeDScene):
    def construct(self):
        
        ######################
        # Mobius Strip Logic #
        ######################
        
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-3, 3, 1],
            x_length=8,
            y_length=8,
            z_length=6,
            axis_config={"include_numbers": True, "color": WHITE}
        )
        
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z").set_color(WHITE)
        
        def strip(u, v):
            R = 2.0 # Outer Radius
            r = 0.8 # Inner Radius
            
            x = (R + v * np.cos(u / 2)) * np.cos(u)
            y = (R + v * np.cos(u / 2)) * np.sin(u)
            z = v * np.sin(u / 2)
            
            return axes.c2p(x, y, z)
        
        surface = Surface(
            func = strip,
            u_range=[0, TAU],
            v_range=[-1, 1],
            resolution=(60, 15),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E]
        )
        
        surface.set_shade_in_3d(True)
        
        ##########################
        # Making the K_3,3 graph #
        ##########################
        
        A_coords = [
            (0.10 * TAU, 0.3),
            (0.40 * TAU, 0.3),
            (0.70 * TAU, 0.3)
        ]
        
        B_coords = [
            (0.25 * TAU, -0.3),
            (0.55 * TAU, -0.3),
            (0.85 * TAU, -0.3)
        ]
        
        # These two plot the vertices on to the mobius strip
        
        nodes_A = VGroup(*[Dot3D(point=strip(u, v), color=RED, radius=0.1) for u, v in A_coords])
        nodes_B = VGroup(*[Dot3D(point=strip(u, v), color=GREEN, radius=0.1) for u, v in B_coords])
        
        
        # Here are the 9 edges of the Graph
        
        edge_uv_funcs = [
            
            ##########################################################################################
            # We connect A1 to B1 to A2 to B2 to A3 to B3 using straight lines in the inner band     #
            ##########################################################################################
            
            lambda t: (0.10 * TAU * (1 - t) + 0.25 * TAU * t,  0.3 * (1 - t) - 0.3 * t),  # A1 to B1
            lambda t: (0.25 * TAU * (1 - t) + 0.40 * TAU * t, -0.3 * (1 - t) + 0.3 * t),  # B1 to A2
            lambda t: (0.40 * TAU * (1 - t) + 0.55 * TAU * t,  0.3 * (1 - t) - 0.3 * t),  # A2 to B2
            lambda t: (0.55 * TAU * (1 - t) + 0.70 * TAU * t, -0.3 * (1 - t) + 0.3 * t),  # B2 to A3
            lambda t: (0.70 * TAU * (1 - t) + 0.85 * TAU * t,  0.3 * (1 - t) - 0.3 * t),  # A3 to B3
            
            ####################################################################################
            # B3 to A1 (Wrapped A1 is at 0.1 + 1 = 1.1 TAU, v flips from 0.3 to -0.3)          #
            # This creates a perfectly straight line entirely along the lower track.           #
            ####################################################################################
            
            lambda t: (0.85 * TAU * (1 - t) + 1.10 * TAU * t, -0.3),                      
            
            ####################################################################################
            # The 3 Cross Chords (Routed forward for maximum visual clarity)                   #
            ####################################################################################
            
            # A1 to B2 (Direct on front, arching UP over A2 for clearance)
            lambda t: (0.10 * TAU * (1 - t) + 0.55 * TAU * t, 0.3 * (1 - t) - 0.3 * t + 0.65 * np.sin(PI * t)), 
            
            # A2 to B3 (Direct on front, arching DOWN under B2 for clearance)
            lambda t: (0.40 * TAU * (1 - t) + 0.85 * TAU * t, 0.3 * (1 - t) - 0.3 * t - 0.65 * np.sin(PI * t)),
            
            # A3 to B1 (Wrapped B1 is at 0.25 + 1 = 1.25 TAU, v flips from -0.3 to 0.3)
            # This creates a perfectly straight line entirely along the upper track!
            lambda t: (0.70 * TAU * (1 - t) + 1.25 * TAU * t, 0.3)
        ]
        
        edges = VGroup(*[
            ParametricFunction(
                lambda t, f=func: strip(*f(t)),
                t_range=[0, 1],
                color=YELLOW,
                stroke_width=4
            ) for func in edge_uv_funcs
        ])
        
        
        # This one was a test
        '''
        # This function makes the edges "hug" on the mobius strip
        
        def get_surface_edge(coord1, coord2):
            u1, v1 = coord1
            u2, v2 = coord2
            
            edge = ParametricFunction(
                lambda t: strip(u1 + t * (u2 - u1), v1 + t * (v2 - v1)),
                t_range=[0, 1],
                color=YELLOW,
                stroke_width=4
            )
            return edge
        
        edge1 = get_surface_edge(A_coords[0], B_coords[1])
        edge2 = get_surface_edge(A_coords[1], B_coords[2])
        edge3 = get_surface_edge(A_coords[2], B_coords[0])
        
        edges = VGroup(edge1, edge2, edge3)
        '''
        
        #######################
        # Plotting everything #
        #######################
        
        self.set_camera_orientation(phi=60 * DEGREES, theta=0 * DEGREES)
        
        self.play(Create(surface))
        
        self.play(Create(nodes_A), Create(nodes_B))
        self.play(Create(edges), run_time=4)
        self.wait(2)
        
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(10*PI)
        self.stop_ambient_camera_rotation()
        self.wait(1)