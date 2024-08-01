import pandas as pd
from RecBole.run_recbole import run


# data = pd.read_csv('listening_events.tsv.bz2', sep='\t', compression='bz2')
# data.columns = ['user_id:token', 'track_id:token', 'time:token']
# data = data.sample(frac=0.1, random_state=42)
# data.to_csv('formatted_listening_events.inter', index=False)

# data = pd.read_csv('tracks.tsv.bz2', sep='\t', compression='bz2')
# data.columns = ['track_id:token','artist:token_seq','track:token_seq']
# data.to_csv('tracks.item', index=False)


# data = pd.read_csv('users.tsv.bz2', sep='\t', compression='bz2')
# data.columns = ['user_id:token','gender:token','country:token','age_on_2013_10_31:token']
# data.to_csv('user.user', index=False)



run(model='SASRec',dataset='LFM', config_file_list=['SASRec_config.yaml'])