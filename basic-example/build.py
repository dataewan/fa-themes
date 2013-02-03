import FranticAccelerator

env = FranticAccelerator.FaEnv()

env.make_template_loader("templates/")

env.render_config("config.yaml")
