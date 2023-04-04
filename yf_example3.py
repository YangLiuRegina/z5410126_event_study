import yfinance as yf
import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    yf_example2.yf_prc_to_csv('QAN.AX',os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv'),start=f'{year}-01-01',end=f'{year}-12-31')

if __name__ == "__main__":
    qan_prc_to_csv(2020)