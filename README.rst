
Json2df
-------

|PyPI version|

json2df is a library batch processing a lists of json data (multiple
instances of same structured json data) into Pandas DataFrame

.. |PyPI version| image:: https://badge.fury.io/py/json2df.svg
   :target: https://badge.fury.io/py/json2df

installation
~~~~~~~~~~~~

``$ pip install json2df``

usage example
~~~~~~~~~~~~~

https://github.com/shichaoji/json2df

e.g. when you scrape some users info data from a website, usually some
fields contains json data format

.. code:: python

    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/shichaoji/json2df/master/sample.csv')
    df.shape




.. parsed-literal::

    (100, 5)



.. code:: python

    df.head(3)




.. raw:: html

    <div>
       <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>mock_id</th>
          <th>location</th>
          <th>primary_currency</th>
          <th>status</th>
          <th>timezone</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>0</td>
          <td>{u'administrative_area': None, u'city': u'Sing...</td>
          <td>{u'code': u'USD', u'name': u'US Dollar', u'cou...</td>
          <td>{u'payment_verified': False, u'identity_verifi...</td>
          <td>{u'country': u'SG', u'offset': 8, u'id': 210, ...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>1</td>
          <td>{u'administrative_area': None, u'city': u'Bris...</td>
          <td>{u'code': u'USD', u'name': u'US Dollar', u'cou...</td>
          <td>{u'payment_verified': False, u'identity_verifi...</td>
          <td>{u'country': u'UK', u'offset': 1, u'id': 262, ...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>2</td>
          <td>{u'administrative_area': None, u'city': u'Ambo...</td>
          <td>{u'code': u'USD', u'name': u'US Dollar', u'cou...</td>
          <td>{u'payment_verified': False, u'identity_verifi...</td>
          <td>{u'country': u'MG', u'offset': 3, u'id': 295, ...</td>
        </tr>
      </tbody>
    </table>
    </div>



e.g. we want to extract and expend all columns from json/dict format to key-value DataFrame
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


use json2df to convert all columns into a DataFrame, the example exlude col "mock_id"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    from json2df import df2df

.. code:: ipython3

    df_new = df2df(df, split_sign='||', exclude_cols=['mock_id'])
    df_new.head(3)


.. parsed-literal::

    (100, 39)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>location||country||highres_flag_url</th>
          <th>location||country||code</th>
          <th>location||country||name</th>
          <th>location||country||seo_url</th>
          <th>location||country||flag_url_cdn</th>
          <th>location||country||highres_flag_url_cdn</th>
          <th>location||country||phone_code</th>
          <th>location||country||language_code</th>
          <th>location||country||demonym</th>
          <th>location||country||language_id</th>
          <th>...</th>
          <th>status||identity_verified</th>
          <th>status||email_verified</th>
          <th>status||deposit_made</th>
          <th>status||phone_verified</th>
          <th>status||facebook_connected</th>
          <th>status||profile_complete</th>
          <th>timezone||country</th>
          <th>timezone||offset</th>
          <th>timezone||id</th>
          <th>timezone||timezone</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>/img/flags/highres_png/singapore.png</td>
          <td>sg</td>
          <td>Singapore</td>
          <td>None</td>
          <td>//cdn2.f-cdn.com/img/flags/png/sg.png</td>
          <td>//cdn6.f-cdn.com/img/flags/highres_png/singapo...</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>...</td>
          <td>False</td>
          <td>True</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>SG</td>
          <td>8.0</td>
          <td>210</td>
          <td>Asia/Singapore</td>
        </tr>
        <tr>
          <th>1</th>
          <td>/img/flags/highres_png/united-kingdom.png</td>
          <td>gb</td>
          <td>United Kingdom</td>
          <td>None</td>
          <td>//cdn6.f-cdn.com/img/flags/png/gb.png</td>
          <td>//cdn5.f-cdn.com/img/flags/highres_png/united-...</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>...</td>
          <td>False</td>
          <td>True</td>
          <td>True</td>
          <td>False</td>
          <td>False</td>
          <td>True</td>
          <td>UK</td>
          <td>1.0</td>
          <td>262</td>
          <td>Europe/London</td>
        </tr>
        <tr>
          <th>2</th>
          <td>/img/flags/highres_png/madagascar.png</td>
          <td>mg</td>
          <td>Madagascar</td>
          <td>None</td>
          <td>//cdn3.f-cdn.com/img/flags/png/mg.png</td>
          <td>//cdn3.f-cdn.com/img/flags/highres_png/madagas...</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>...</td>
          <td>False</td>
          <td>True</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>True</td>
          <td>MG</td>
          <td>3.0</td>
          <td>295</td>
          <td>Indian/Antananarivo</td>
        </tr>
      </tbody>
    </table>
    <p>3 rows × 39 columns</p>
    </div>



.. code:: ipython3

    df_new.head(3).transpose()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>0</th>
          <th>1</th>
          <th>2</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>location||country||highres_flag_url</th>
          <td>/img/flags/highres_png/singapore.png</td>
          <td>/img/flags/highres_png/united-kingdom.png</td>
          <td>/img/flags/highres_png/madagascar.png</td>
        </tr>
        <tr>
          <th>location||country||code</th>
          <td>sg</td>
          <td>gb</td>
          <td>mg</td>
        </tr>
        <tr>
          <th>location||country||name</th>
          <td>Singapore</td>
          <td>United Kingdom</td>
          <td>Madagascar</td>
        </tr>
        <tr>
          <th>location||country||seo_url</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||country||flag_url_cdn</th>
          <td>//cdn2.f-cdn.com/img/flags/png/sg.png</td>
          <td>//cdn6.f-cdn.com/img/flags/png/gb.png</td>
          <td>//cdn3.f-cdn.com/img/flags/png/mg.png</td>
        </tr>
        <tr>
          <th>location||country||highres_flag_url_cdn</th>
          <td>//cdn6.f-cdn.com/img/flags/highres_png/singapo...</td>
          <td>//cdn5.f-cdn.com/img/flags/highres_png/united-...</td>
          <td>//cdn3.f-cdn.com/img/flags/highres_png/madagas...</td>
        </tr>
        <tr>
          <th>location||country||phone_code</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||country||language_code</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||country||demonym</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||country||language_id</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||country||person</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||country||iso3</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||country||sanction</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||country||flag_url</th>
          <td>/img/flags/png/sg.png</td>
          <td>/img/flags/png/gb.png</td>
          <td>/img/flags/png/mg.png</td>
        </tr>
        <tr>
          <th>location||country||flag_class</th>
          <td>singapore</td>
          <td>united-kingdom</td>
          <td>madagascar</td>
        </tr>
        <tr>
          <th>location||country||region_id</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||administrative_area</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||city</th>
          <td>Singapore</td>
          <td>Bristol</td>
          <td>Ambohidratrimo</td>
        </tr>
        <tr>
          <th>location||vicinity</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||longitude</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||full_address</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>location||latitude</th>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>primary_currency||code</th>
          <td>USD</td>
          <td>USD</td>
          <td>USD</td>
        </tr>
        <tr>
          <th>primary_currency||name</th>
          <td>US Dollar</td>
          <td>US Dollar</td>
          <td>US Dollar</td>
        </tr>
        <tr>
          <th>primary_currency||country</th>
          <td>US</td>
          <td>US</td>
          <td>US</td>
        </tr>
        <tr>
          <th>primary_currency||sign</th>
          <td>$</td>
          <td>$</td>
          <td>$</td>
        </tr>
        <tr>
          <th>primary_currency||exchange_rate</th>
          <td>1.0</td>
          <td>1.0</td>
          <td>1.0</td>
        </tr>
        <tr>
          <th>primary_currency||id</th>
          <td>1</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>status||payment_verified</th>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
        <tr>
          <th>status||identity_verified</th>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
        <tr>
          <th>status||email_verified</th>
          <td>True</td>
          <td>True</td>
          <td>True</td>
        </tr>
        <tr>
          <th>status||deposit_made</th>
          <td>False</td>
          <td>True</td>
          <td>False</td>
        </tr>
        <tr>
          <th>status||phone_verified</th>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
        <tr>
          <th>status||facebook_connected</th>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
        <tr>
          <th>status||profile_complete</th>
          <td>False</td>
          <td>True</td>
          <td>True</td>
        </tr>
        <tr>
          <th>timezone||country</th>
          <td>SG</td>
          <td>UK</td>
          <td>MG</td>
        </tr>
        <tr>
          <th>timezone||offset</th>
          <td>8.0</td>
          <td>1.0</td>
          <td>3.0</td>
        </tr>
        <tr>
          <th>timezone||id</th>
          <td>210</td>
          <td>262</td>
          <td>295</td>
        </tr>
        <tr>
          <th>timezone||timezone</th>
          <td>Asia/Singapore</td>
          <td>Europe/London</td>
          <td>Indian/Antananarivo</td>
        </tr>
      </tbody>
    </table>
    </div>

