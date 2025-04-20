# cervical-cancer-answer-engine

Run me:

```
python3 -m venv venv
source venv/bin/activate
python3 answer_engine_src/generate_remote_files.py
streamlit run app.py
```

## Remote Deploy 

To remote deploy the streamlit app using the streamlit community cloud.

1. Initialize the repo as a separate repo of this instance. Maybe just fork it.
2. Add openai secrets to the secrets during deploy.
3. Upload the remote files to gdrive.
4. Modify the `constants.GDRIVE_FILE_ID` value with the id of your uploaded `pklz` file id. 

