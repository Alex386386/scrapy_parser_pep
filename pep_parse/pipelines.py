import csv
import datetime
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent / 'results'


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        BASE_DIR.mkdir(exist_ok=True)
        filename = BASE_DIR / f'status_summary_{date}.csv'
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Status', 'Count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            rows = [{'Status': status, 'Count': count} for status, count in
                    self.status_counts.items()]
            writer.writerows(rows)

            writer.writerow(
                {'Status': 'Total', 'Count': sum(self.status_counts.values())})
