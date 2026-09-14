import pandas as pd

train_df = pd.read_parquet('KDDTrain.parquet')
test_df = pd.read_parquet('KDDTest.parquet')

train_df = train_df.drop_duplicates()
test_df = test_df.drop_duplicates()

categories = {
    "DoS": ["back", "land", "neptune", "pod", "smurf", "teardrop", "apache2", "udpstorm", "processtable", "mailbomb", "worm"],
    "Probe": ["satan", "ipsweep", "nmap", "portsweep", "mscan", "saint"],
    "R2L": ["guess_passwd", "ftp_write", "imap", "phf", "multihop", "warezmaster", "warezclient", "spy", "xlock", "xsnoop", "snmpguess", "snmpgetattack", "httptunnel", "sendmail", "named"],
    "U2R": ["buffer_overflow", "loadmodule", "perl", "rootkit", "ps", "sqlattack", "xterm"],
    "Normal": ["normal"]
}

def categorising(attack):
    attack = str(attack).strip().lower()
    for cat_name, attack_list in categories.items():
        if attack in attack_list:
            return cat_name
    return "Attack_Other"

target_col = 'label' if 'label' in train_df.columns else 'class'
train_df['target'] = train_df[target_col].apply(categorising)
test_df['target'] = test_df[target_col].apply(categorising)

X_train_raw = train_df.drop(columns=[target_col, 'target'])
X_test_raw = test_df.drop(columns=[target_col, 'target'])

X_train = pd.get_dummies(X_train_raw, drop_first=True)
X_test = pd.get_dummies(X_test_raw, drop_first=True)
X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

X_train['target'] = train_df['target'].values
X_test['target'] = test_df['target'].values

X_train.to_parquet('KDDTrain_clean.parquet', index=False)
X_test.to_parquet('KDDTest_clean.parquet', index=False)
print("💾 Data cleaning complete! Cleaned multi-class files saved successfully.")
