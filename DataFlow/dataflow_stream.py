from __future__ import absolute_import

import argparse
import logging
import re
import six

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
import apache_beam.transforms.window as window
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import StandardOptions

import json as js
import time

from datetime import datetime
start_time = datetime.now()

print start_time

#parellel do function
class ParseRecordDoFn(beam.DoFn):
    def process(self, element):
        import json
        r = json.loads(element)
        yield r['ProductID'], r['Price']

def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--output_topic', default='projects/complete-rush-206308/topics/salesstream',
        help=('Output PubSub topic of the form '
              '"projects/<PROJECT>/topic/<TOPIC>".'))
    parser.add_argument(
        '--input_topic', default='projects/complete-rush-206308/topics/salesstream',
        help=('Input PubSub topic of the form '))
    parser.add_argument(
        '--input_subscription', default='projects/complete-rush-206308/subscriptions/salesReceiver',
        help=('Input PubSub subscription of the form '))
    parser.add_argument('--output',
                        dest='output',
                        default='gs://sales_bkt/output/',
                        help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)
    pipeline_args.extend([
        '--runner=DataflowRunner',
        '--project=complete-rush-206308',
        '--staging_location=gs://sales_bkt/stg',
        '--temp_location=gs://sales_bkt/tmp',
        '--job_name=myslaesprostream',
    ])

    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = True
    pipeline_options.view_as(StandardOptions).streaming = True

    with beam.Pipeline(options=pipeline_options) as p:
        output = (p #| beam.io.ReadStringsFromPubSub(subscription=known_args.input_subscription)
        | beam.io.ReadStringsFromPubSub(topic=known_args.input_topic)
        #| beam.FlatMap(parse_record, filtered)
        | beam.ParDo(ParseRecordDoFn())
        | beam.WindowInto(window.FixedWindows(15, 0))
        | beam.CombinePerKey(sum))


        output | beam.io.WriteStringsToPubSub(known_args.output_topic)
        #output | WriteToText(known_args.output)
    print start_time


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()

  end_time = datetime.now()
  print('Duration: {}'.format(end_time - start_time))

