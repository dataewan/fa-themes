import FranticAccelerator

# Create the environment to do the rendering
env = FranticAccelerator.FaEnv()

# Set the template directory
env.make_template_loader("templates/")

# Tell it to render the config
env.render_config("config.yaml")
