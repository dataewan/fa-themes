import FranticAccelerator

# Create the environment to do the rendering
env = FranticAccelerator.FaEnv()

# Set the template directory
env.set_template_dir("templates/")

# Read the config.
env.read_config("config.yaml")
# Output it without making changes to the config.
env.output_config()
