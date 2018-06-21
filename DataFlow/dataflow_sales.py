from __future__ import absolute_import
import argparse
import logging
import re
import six
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
import json as js
import time
from datetime import datetime

start_time = datetime.now()
print start_time

class ParseRecordDoFnUsrClust(beam.DoFn):
    def process(self, element):
        import json
        r = json.loads(element)
        yield r['UserId'], r['Price']

class ParseRecordDoFnmap(beam.DoFn):
    def process(self,gd):
        e1, e2 = gd
        ele = list(e2)
        item_count = len(ele)
        total_price = sum(ele)
        yield e1, item_count, total_price


def run(argv=None):

  parser = argparse.ArgumentParser()
  parser.add_argument('--input',
                      dest='input',
                      default='gs://sales_bkt/inputdata',
                      help='Input file to process.')
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
      '--job_name=myslaespro',
  ])

  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = True

#initiate pipeline
  with beam.Pipeline(options=pipeline_options) as p:

    output = (p | ReadFromText(known_args.input)
    | beam.ParDo(ParseRecordDoFnUsrClust())
    | beam.GroupByKey()
    | beam.ParDo(ParseRecordDoFnmap()))

    output | WriteToText(known_args.output)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()

  end_time = datetime.now()
  print('Duration: {}'.format(end_time - start_time))

