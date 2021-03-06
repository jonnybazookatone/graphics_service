GRAPHICS_SECRET_KEY = 'this should be changed'
GRAPHICS_INCLUDE_ARXIV = False
SQLALCHEMY_BINDS = {}
GRAPHICS_ENABLE_UPDATES = False
# Define sets for which to obtain graphics data for graphics database
# The key defines the set and the values are journals (or categories, in the
# case of arXiv)
GRAPHICS_PUBSETS = {
                   'IOP':['ApJ','ApJL','ApJS','AJ'],
                   'Elsevier':['NewA'],
                   'arXiv': ['arXiv', 'acc-phys', 'adap-org', 'alg-geom',
                             'ao-sci', 'astro-ph', 'atom-ph', 'bayes-an',
                             'chao-dyn', 'chem-ph', 'cmp-lg', 'comp-gas',
                             'cond-mat', 'cs', 'dg-ga', 'funct-an', 'gr-qc',
                             'hep-ex', 'hep-lat', 'hep-ph', 'hep-th', 'math',
                             'math-ph', 'mtrl-th', 'nlin', 'nucl-ex', 'nucl-th',
                             'patt-sol', 'physics', 'plasm-ph', 'q-alg', 'q-bio',
                             'quant-ph', 'solv-int', 'supr-con']
                  }
# External graphics sources
GRAPHICS_EXTSOURCES = ['IOP', 'Elsevier']
# Some info for the external site
GRAPHICS_HEADER = {
                  'IOP':'Every image links to the <a href="http://www.astroexplorer.org/" target="_new">IOP "Astronomy Image Explorer"</a> for more detail.',
                  'Elsevier':'Every image links to the article on <a href="http://www.sciencedirect.com" target="_new">ScienceDirect</a>'
                  }
# Define the mapping to help retrieve full text files for a given identifier
GRAPHICS_FULLTEXT_MAPS = {
    'IOP':'/path/to/IOP.map',
    'arXiv':'/path/to/arXiv.map'
}
# Define a file with backdata, if available
GRAPHICS_BACK_DATA_FILE = {
}
# These are the values to be stored as "source" in the graphics database
GRAPHICS_SOURCE_NAMES = {
    'IOP': 'IOP',
    'Elsevier':'Elsevier',
    'arXiv': 'arXiv',
}
# Work directory to store temporary data (e.g. for unpacking TAR files)
GRAPHICS_TMP_DIR = ''
# Base directory of where extracted images will be stored
GRAPHICS_IMAGE_DIR = ''
# Base URL for serving images
GRAPHICS_BASE_URL = ''
# Vertical size for thumbnails
GRAPHICS_THMB_SIZE = '100'
# How do we query Solr
GRAPHICS_SOLR_PATH = 'https://api.adsabs.harvard.edu/v1/search/query'
# This section configures this application to act as a client, for example
# to query solr via adsws
GRAPHICS_API_TOKEN = 'we will provide an api key token for this application'
# Config for logging
GRAPHICS_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s\t%(process)d '
                      '[%(asctime)s]:\t%(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        }
    },
    'handlers': {
        'file': {
            'formatter': 'default',
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/tmp/graphics.log',
        },
        'console': {
            'formatter': 'default',
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
# Define the autodiscovery endpoint
DISCOVERER_PUBLISH_ENDPOINT = '/resources'
# Advertise its own route within DISCOVERER_PUBLISH_ENDPOINT
DISCOVERER_SELF_PUBLISH = False
