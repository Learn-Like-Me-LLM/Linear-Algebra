from manim import DOWN

def next_to_updater(mob, target, direction=DOWN):
    def updater(m):
        m.next_to(target, direction)
    return updater