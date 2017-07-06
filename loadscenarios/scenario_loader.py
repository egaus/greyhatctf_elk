#! /usr/bin/env python
import json
from datetime import datetime, timedelta
import os
import argparse
import sys
import tarfile
import time
from glob import glob
from elasticsearch import Elasticsearch

def get_files(path, extension):
    files = []
    for myfile in os.listdir(path):
        if myfile.endswith(extension):
            match = os.path.join(path, myfile)
            files.append(match)

    return files

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fixes dates on json format bro logs relative to some time period')

    parser.add_argument('-i', '--logs_input', help='Path where logs will be modified.', required=True)
    parser.add_argument('-o', '--logs_output', help='Path where logs will be dropped.', required=True)
    parser.add_argument('-hr', '--hours', help='Number hours from curent time to adjust logs to.', required=True)

    args = parser.parse_args()

    input_path = args.logs_input
    output_path = args.logs_output
    hours = int(args.hours)
    temp_path = './tmp'

    while True:
        time.sleep(3)

        # Check for tar.gz files
        if os.path.exists(input_path):
            zipfiles = get_files(input_path, ".tar.gz")
            print "found {} files".format(len(zipfiles))
            for zipfile in zipfiles:
                if not os.path.exists(temp_path):
                    os.makedirs(temp_path)
                tar = tarfile.open(zipfile, "r:gz")
                tar.extractall(temp_path)
                tar.close()

                if not os.path.exists(args.logs_output):
                    os.makedirs(args.logs_output)
                else:
                    log_files_to_delete = glob(os.path.join("./logs", "*.log"))
                    [os.remove(x) for x in log_files_to_delete]

                files = get_files(temp_path, ".log")
                d = datetime.today() - timedelta(hours=hours)
                new_start_time = int(d.strftime('%s'))

                if len(files) > 0:
                    try:
                        es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
                        es.indices.delete('logstash-*', ignore=400)
                    except Exception, e:
                        print "Could not connect to elasticsearch"

                for log_file in files:
                    print log_file
                    with open(log_file) as mylog:
                        logs = mylog.readlines()

                    orig_start_time = json.loads(logs[0]).get('ts', 0)
                    os.remove(log_file)

                    with open(os.path.join(output_path, os.path.basename(log_file)), 'wb') as write_log:
                        for log in logs:
                            log_dictionary = json.loads(log)
                            event_time = log_dictionary.get('ts', -1)
                            if event_time > -1:
                                log_dictionary['ts'] = float(event_time) - orig_start_time + new_start_time
                            write_log.write(json.dumps(log_dictionary) + '\n')
                os.remove(zipfile)
                os.rmdir(temp_path)
        else:
            print "Supplied log_input directory did not exist."
            time.sleep(10)





