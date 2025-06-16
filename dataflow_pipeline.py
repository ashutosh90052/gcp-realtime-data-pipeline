import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.io.gcp.pubsub import ReadFromPubSub

class ParseJsonDoFn(beam.DoFn):
    def process(self, element):
        record = json.loads(element.decode('utf-8'))
        yield {
            'user_id': record['user_id'],
            'amount': record['amount'],
            'location': record['location'],
            'timestamp': record['timestamp']
        }

def run():
    options = PipelineOptions(
        streaming=True,
        project='realtime-pipeline-463110',
        region='asia-south1',
        job_name='realtime-txn-pipeline',
        temp_location='gs://ashutosh-dataflow-bucket-2025/temp',
        staging_location='gs://ashutosh-dataflow-bucket-2025/staging',
        runner='DataflowRunner'
    )
    options.view_as(StandardOptions).streaming = True

    with beam.Pipeline(options=options) as p:
        (p
         | 'ReadFromPubSub' >> ReadFromPubSub(topic='projects/realtime-pipeline-463110/topics/transactions-topic')
         | 'ParseJson' >> beam.ParDo(ParseJsonDoFn())
         | 'WriteToBigQuery' >> WriteToBigQuery(
                table='realtime_dataset.transactions',
                dataset='realtime_dataset',
                project='realtime-pipeline-463110',
                schema='user_id:STRING, amount:FLOAT, location:STRING, timestamp:TIMESTAMP',
                create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

if __name__ == '__main__':
    run()
