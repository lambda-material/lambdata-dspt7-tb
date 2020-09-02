
# helper function for dropping columns with nan values. 

def drop_high_nan(df, num_nans):
    '''
    drop columns with preselected number of nans

    df = selected dataframe
    num_nans = the number of nans as a threshold to drop
    '''
    col = df.columns.to_list()
    for col in df:
        if df[col].isnull().sum() > num_nans:
            df = df.drop(col, axis=1)
    return df



def num_nans(df):
    """
    print the number of nans for your dataframe.
    """
    return print(df.isnull().sum())


def train_val_test_spit(x,y,test_size):
    '''
    function will return X_train, X_val, X_test, y_train, y_val, y_test
    inputs from user, x (data without target), y (target vector), and split size.

    invoke: X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_spit(x, y, .2)
    '''
    X_train, X_test, y_train, y_test = train_test_split(x, y,
                test_size=test_size, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train,
                test_size=test_size, random_state=42)
    return X_train, X_val, X_test, y_train, y_val, y_test

