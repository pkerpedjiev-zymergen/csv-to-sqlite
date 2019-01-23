import csv_to_sqlite as cts
import os
import os.path as op

def test_sample1():
	input_file = 'test/data/sample1.tsv'
	output_file = 'test/output/sample1.sqlite'

	# if the output file exists, remove it so that we don't
	# end up looking at stale results
	if op.exists(output_file):
		os.remove(output_file)

	with open(input_file, 'r') as f:
		# run the conversion
		cts._start([input_file], output_file,
			delimiter='\t', 
			find_types=True,
			drop_tables=True, 
			verbose=True,
			columns=[
				'protein_accession',
				'sequence_md5_digest',
				'sequence_length',
				'analysis',
				'signature_accession',
				'signature_description',
				'start_location',
				'stop_location',
				'score',
				'status',
				'date',
				'interpro_annotations_accession',
				'interpro_annotations_description',
				'go_annotations',
				'pathway_annotations'
			])
	