import sys

import ruamel.yaml as yaml

from comet.bot import Comet
from comet.logging import setup_logging

# Load configuration file.
try:
    with open('config.yml', 'r') as config_file:
        try:
            cfg = yaml.safe_load(config_file.read())
        except yaml.YAMLError as exc:
            print('Error loading configuration:', exc, file=sys.stderr)
            sys.exit(1)
except FileNotFoundError:
    print('A `config.yaml` file was not found.', file=sys.stderr)
    sys.exit(1)

# Setup logging.
setup_logging()

# Make a Comet and run it.
comet = Comet(cfg)
comet.run(cfg['discord']['token'])
