import subprocess

#os = subprocess.run(['arecord','-f','dat','-d','5','viz.mp3'],shell=True)



import serial
import time
import pyaudio
import wave
import os
from google.cloud import storage


#subprocess.call(['sh', './file.sh'])

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/pi/new/xihaja.json'

storage_client = storage.Client()

dir(storage_client)

"""
Create a new bucket
"""


#bucket_name = "yourtap-audio_filesmm"
#bucket = storage_client.bucket(bucket_name)
#bucket.location = 'US'
#storage_client.create_bucket(bucket)

"""
print bucket details
"""

# vars(bucket)


"""
Accessing sepecific bucket
"""

# my_bucket = storage_client.get_bucket(bucket_name)


"""
upload files
"""

def upload_to_bucket(blob_name, file_path, bucket_name) :
    """
    Create a new bucket
    """


    #bucket_name = "yourtap-audio_filesmm31"
    bucket = storage_client.bucket(bucket_name)
    bucket.location = 'US'
    storage_client.create_bucket(bucket)
    try :
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e : 
        print(e)
        return False

#file_path = r'/home/pi/new/viz.mp3'

#upload_to_bucket('voice1',file_path, bucket_name)




def record(duration, audio_name) :
    #function that records the voice
    cmd = 'arecord -f dat -d %d %s.mp3'% (duration,audio_name)
    os.system(cmd)

    



def send_audio(blob_name, file_path, bucket_name,audio_name, duration)  :
    record(duration, audio_name)
    upload_to_bucket(blob_name, file_path, bucket_name)

#file_path = r'/home/pi/new/audio_name.mp3'
send_audio('oussama',r'/home/pi/new/ouss.mp3',"yourtap-audio_filesp",'ouss',8)  
send_audio('oussama1',r'/home/pi/new/oussa.mp3',"yourtap-audio_filesp",'oussa',4)
    
    
    
    