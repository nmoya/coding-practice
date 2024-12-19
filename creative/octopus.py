from manim import *


def debug(data):
    with open("debug.txt", "a") as f:
        f.write(str(data) + "\n")


class TentacleFunction(Scene):
    def construct(self):
        left_limit_x = -10
        right_limit_x = 6
        number_of_points = 40

        def tentacle_func(x):
            amplitude = 1
            decay = 0.2
            frequency = 0.5
            noise_strength = 0
            noise = noise_strength * np.random.uniform(-1, 1)
            return amplitude * np.exp(-decay * x) * np.sin(frequency * x) + noise

        def generate_points(func, x_range, num_points):
            x_values = np.linspace(x_range[0], x_range[1], num_points)
            y_values = [func(x) for x in x_values]

            return [np.array([x, y, 0]) for x, y in zip(x_values, y_values)]

        def compute_normal_vector(Pp, P, Pn):
            PpP = P - Pp
            PnP = Pn - P

            PpP_normalized = PpP / np.linalg.norm(PpP)
            PnP_normalized = PnP / np.linalg.norm(PnP)

            bisector = PpP_normalized + PnP_normalized
            normal_vector = bisector / np.linalg.norm(bisector)

            normal = np.array([-normal_vector[1], normal_vector[0], 0])
            normal *= 1
            return normal

        def compute_normals(points, index):
            if 0 < index < len(points) - 1:
                normal = compute_normal_vector(points[index - 1], points[index], points[index + 1])
                # Make the tentacle thinner as it goes further
                normal *= 1 - (0.025 * index)
                return normal
            elif index == 0:
                return np.array([0, 0, 0])
            else:
                return np.array([0, 0, 0])

        x_range = [left_limit_x, right_limit_x]
        points = generate_points(tentacle_func, x_range, number_of_points)
        normals = [compute_normals(points, i) for i in range(len(points))]
        bot_normals = [n * -1 for n in normals]
        normal_lines = [Line(start=p, end=p + n, color=RED) for p, n in zip(points, normals)]
        bot_normal_lines = [Line(start=p, end=p + n, color=RED) for p, n in zip(points, bot_normals)]

        connecting_lines = []
        for i, line in enumerate(normal_lines[:-1]):
            connecting_lines.append(Line(start=line.end, end=normal_lines[i + 1].end, color=WHITE))
        for i, line in enumerate(bot_normal_lines[:-1]):
            connecting_lines.append(Line(start=line.end, end=bot_normal_lines[i + 1].end, color=WHITE))

        # Draw the tentacle and ellipses
        draw_dots = VGroup(*[Dot(point=p, color=WHITE) for p in points])
        draw_normals = VGroup(*normal_lines)
        draw_bot_normals = VGroup(*bot_normal_lines)
        draw_connecting_lines = VGroup(*connecting_lines)

        self.play([FadeIn(draw_dots)])
        self.play([FadeIn(draw_normals), FadeIn(draw_bot_normals)])
        self.play([FadeIn(draw_connecting_lines)])

        self.play(*[FadeOut(draw_normals), FadeOut(draw_bot_normals), FadeOut(draw_dots)])
        self.wait()
