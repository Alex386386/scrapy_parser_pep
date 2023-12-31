BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
PEP_SPIDER_NAME = 'pep'
PEP_ALLOWED_DOMAINS = ['peps.python.org']
PEP_START_URLS = ['https://peps.python.org/']

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'encoding': 'utf-8',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}

ITEM_PIPELINES = {'pep_parse.pipelines.PepParsePipeline': 300}
