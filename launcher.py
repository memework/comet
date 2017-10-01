import sys

import utils.clark as clark
from comet.bot import Comet
from ruamel.yaml import YAMLError
from comet.logging import setup_logging

# Load configuration file.
try:
    cfg = clark.load('config.yml')
except YAMLError as exc:
    print('Error loading configuration:', exc, file=sys.stderr)
    sys.exit(1) 
except FileNotFoundError:
    print('A `config.yaml` file was not found.', file=sys.stderr)
    sys.exit(1)

# Setup logging.
setup_logging()

# Make a Comet and run it.
comet = Comet(cfg)
try:
    comet.load_extension("plugins.core")
except Exception as e:
    print("failed to load core: {}".format(e))
    exit(0)
comet.run(cfg['discord']['token'])
