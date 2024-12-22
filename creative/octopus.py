import random

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

        def gen_suckers(points, normals):
            suckers = []
            for i, (point, normal) in enumerate(zip(points, normals)):
                if point[0] > 4.5:
                    continue
                max_radius = max(0.075, point[0] * -1 * 0.02)
                if point[0] > 2:
                    shifted_sucker = point
                elif 0 < point[0] <= 2:
                    shifted_sucker = point + (normal / 2.5)
                else:
                    shifted_sucker = point + (normal / 2)
                circle = Circle(radius=max_radius)
                inner_circle = Circle(radius=max_radius * 0.25)
                circle.move_to(shifted_sucker)
                inner_circle.move_to(shifted_sucker)
                suckers.append(circle)
                suckers.append(inner_circle)
            return suckers

        def gen_connecting_lines(normal_lines):
            connecting_lines = []
            for i, line in enumerate(normal_lines[:-1]):
                connecting_lines.append(Line(start=line.end, end=normal_lines[i + 1].end, color=WHITE))
            return connecting_lines

        def get_n_points_on_line(line, n):
            return [line.point_from_proportion(i / n) for i in range(n)]

        x_range = [left_limit_x, right_limit_x]
        points = generate_points(tentacle_func, x_range, number_of_points)
        normals = [compute_normals(points, i) for i in range(len(points))]
        bot_normals = [n * -1 for n in normals]
        normal_lines = [Line(start=p, end=p + n, color=RED) for p, n in zip(points, normals)]
        bot_normal_lines = [Line(start=p, end=p + n, color=RED) for p, n in zip(points, bot_normals)]

        bot_connecting_lines = gen_connecting_lines(normal_lines)
        top_connecting_lines = gen_connecting_lines(bot_normal_lines)
        connecting_lines = bot_connecting_lines + top_connecting_lines

        inner_lines = []
        for line in bot_connecting_lines:
            sample = get_n_points_on_line(line, 10)
            sample_normals = [compute_normals(points, i) for i in range(len(points))]
            for point, normal in zip(sample, sample_normals):
                inner_lines.append(Line(start=point, end=point + (normal * (random.random() * -0.45)), color=WHITE))
        for line in top_connecting_lines:
            sample = get_n_points_on_line(line, 10)
            sample_normals = [compute_normals(points, i) for i in range(len(points))]
            for point, normal in zip(sample, sample_normals):
                inner_lines.append(Line(start=point, end=point + (normal * (random.random() * 0.45)), color=WHITE))

        top_suckers = gen_suckers(points, normals)
        bot_suckers = gen_suckers(points, bot_normals)

        draw_dots = VGroup(*[Dot(point=p, color=WHITE) for p in points])
        draw_normals = VGroup(*normal_lines)
        draw_bot_normals = VGroup(*bot_normal_lines)
        draw_connecting_lines = VGroup(*connecting_lines)
        draw_top_suckers = VGroup(*top_suckers)
        draw_bot_suckers = VGroup(*bot_suckers)
        draw_inner_lines = VGroup(*inner_lines)

        self.play(
            FadeIn(draw_connecting_lines), FadeIn(draw_top_suckers), FadeIn(draw_bot_suckers), FadeIn(draw_inner_lines)
        )
        # self.play([FadeIn(draw_dots)])
        # self.play([FadeIn(draw_normals), FadeIn(draw_bot_normals)])
        # self.play([FadeIn(draw_connecting_lines)])
        # self.play([FadeIn(draw_top_suckers), FadeIn(draw_bot_suckers)])

        # self.play(*[FadeOut(draw_normals), FadeOut(draw_bot_normals), FadeOut(draw_dots)])
        self.wait()
