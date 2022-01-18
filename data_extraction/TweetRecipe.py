import logging
logging.basicConfig(level = logging.INFO)
import pandas as pd


logger = logging.getLogger(__name__)

def clean_process(filename="dataSetPositivos.csv"):
    logger.info("Starting cleaning process")
    df = _read_data(filename)
    _save_data(df,filename)

    return df


def _read_data(filename):
    logger.info('Reading file {}'.format(filename))
    return pd.read_csv(filename, encoding="utf-8")



def _save_data(df,filename):
    cleanFilename = 'data_prueba_{}'.format(filename)
    logger.info('Saving data at location: {}'.format(cleanFilename))
    df.to_csv(cleanFilename,encoding='utf-8', index=False)


clean_process()
