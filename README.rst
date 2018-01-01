
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

e.g. when you scrape some users info data from a website, usually some
fields contains json data format

.. code:: ipython2

    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/shichaoji/json2df/master/sample.csv')
    df.shape
    
    (100, 5)
    df.head(3)





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



e.g. we want to extract the location field and convert into a dataframe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

select location

.. code:: ipython2

    df['location'].head()




.. parsed-literal::

    0    {u'administrative_area': None, u'city': u'Sing...
    1    {u'administrative_area': None, u'city': u'Bris...
    2    {u'administrative_area': None, u'city': u'Ambo...
    3    {u'administrative_area': None, u'city': u'Drob...
    4    {u'administrative_area': None, u'city': u'Torr...
    Name: location, dtype: object



view first row

.. code:: ipython2

    first_row = df['location'].head()[0]
    print type(first_row)
    first_row


.. parsed-literal::

    <type 'str'>




.. parsed-literal::

    "{u'administrative_area': None, u'city': u'Singapore', u'country': {u'highres_flag_url': u'/img/flags/highres_png/singapore.png', u'code': u'sg', u'name': u'Singapore', u'seo_url': None, u'flag_url_cdn': u'//cdn2.f-cdn.com/img/flags/png/sg.png', u'highres_flag_url_cdn': u'//cdn6.f-cdn.com/img/flags/highres_png/singapore.png', u'phone_code': None, u'language_code': None, u'demonym': None, u'language_id': None, u'person': None, u'iso3': None, u'sanction': None, u'flag_url': u'/img/flags/png/sg.png', u'flag_class': u'singapore', u'region_id': None}, u'vicinity': None, u'longitude': None, u'full_address': None, u'latitude': None}"



convert the string representation into a python dictionary

as you can see the json data has inner loop

.. code:: ipython2

    import ast
    ast.literal_eval(first_row)




.. parsed-literal::

    {u'administrative_area': None,
     u'city': u'Singapore',
     u'country': {u'code': u'sg',
      u'demonym': None,
      u'flag_class': u'singapore',
      u'flag_url': u'/img/flags/png/sg.png',
      u'flag_url_cdn': u'//cdn2.f-cdn.com/img/flags/png/sg.png',
      u'highres_flag_url': u'/img/flags/highres_png/singapore.png',
      u'highres_flag_url_cdn': u'//cdn6.f-cdn.com/img/flags/highres_png/singapore.png',
      u'iso3': None,
      u'language_code': None,
      u'language_id': None,
      u'name': u'Singapore',
      u'person': None,
      u'phone_code': None,
      u'region_id': None,
      u'sanction': None,
      u'seo_url': None},
     u'full_address': None,
     u'latitude': None,
     u'longitude': None,
     u'vicinity': None}



user json2df to convert the entire location field (Series) into a DataFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython2

    from json2df import series2df
    
    extract_df = series2df(df['location'])
    print (extract_df.shape, type(extract_df))
    extract_df.head(10)


.. parsed-literal::

    ((100, 22), <class 'pandas.core.frame.DataFrame'>)




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
          <th>administrative_area</th>
          <th>city</th>
          <th>country_code</th>
          <th>country_demonym</th>
          <th>country_flag_class</th>
          <th>country_flag_url</th>
          <th>country_flag_url_cdn</th>
          <th>country_highres_flag_url</th>
          <th>country_highres_flag_url_cdn</th>
          <th>country_iso3</th>
          <th>...</th>
          <th>country_name</th>
          <th>country_person</th>
          <th>country_phone_code</th>
          <th>country_region_id</th>
          <th>country_sanction</th>
          <th>country_seo_url</th>
          <th>full_address</th>
          <th>latitude</th>
          <th>longitude</th>
          <th>vicinity</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>None</td>
          <td>Singapore</td>
          <td>sg</td>
          <td>None</td>
          <td>singapore</td>
          <td>/img/flags/png/sg.png</td>
          <td>//cdn2.f-cdn.com/img/flags/png/sg.png</td>
          <td>/img/flags/highres_png/singapore.png</td>
          <td>//cdn6.f-cdn.com/img/flags/highres_png/singapo...</td>
          <td>None</td>
          <td>...</td>
          <td>Singapore</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>1</th>
          <td>None</td>
          <td>Bristol</td>
          <td>gb</td>
          <td>None</td>
          <td>united-kingdom</td>
          <td>/img/flags/png/gb.png</td>
          <td>//cdn6.f-cdn.com/img/flags/png/gb.png</td>
          <td>/img/flags/highres_png/united-kingdom.png</td>
          <td>//cdn5.f-cdn.com/img/flags/highres_png/united-...</td>
          <td>None</td>
          <td>...</td>
          <td>United Kingdom</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>2</th>
          <td>None</td>
          <td>Ambohidratrimo</td>
          <td>mg</td>
          <td>None</td>
          <td>madagascar</td>
          <td>/img/flags/png/mg.png</td>
          <td>//cdn3.f-cdn.com/img/flags/png/mg.png</td>
          <td>/img/flags/highres_png/madagascar.png</td>
          <td>//cdn3.f-cdn.com/img/flags/highres_png/madagas...</td>
          <td>None</td>
          <td>...</td>
          <td>Madagascar</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>3</th>
          <td>None</td>
          <td>Drobak</td>
          <td>no</td>
          <td>None</td>
          <td>norway</td>
          <td>/img/flags/png/no.png</td>
          <td>//cdn2.f-cdn.com/img/flags/png/no.png</td>
          <td>/img/flags/highres_png/norway.png</td>
          <td>//cdn3.f-cdn.com/img/flags/highres_png/norway.png</td>
          <td>None</td>
          <td>...</td>
          <td>Norway</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>4</th>
          <td>None</td>
          <td>Torronto</td>
          <td>ca</td>
          <td>None</td>
          <td>canada</td>
          <td>/img/flags/png/ca.png</td>
          <td>//cdn6.f-cdn.com/img/flags/png/ca.png</td>
          <td>/img/flags/highres_png/canada.png</td>
          <td>//cdn6.f-cdn.com/img/flags/highres_png/canada.png</td>
          <td>None</td>
          <td>...</td>
          <td>Canada</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>5</th>
          <td>None</td>
          <td>San Francisco</td>
          <td>us</td>
          <td>None</td>
          <td>united-states</td>
          <td>/img/flags/png/us.png</td>
          <td>//cdn3.f-cdn.com/img/flags/png/us.png</td>
          <td>/img/flags/highres_png/united-states.png</td>
          <td>//cdn6.f-cdn.com/img/flags/highres_png/united-...</td>
          <td>None</td>
          <td>...</td>
          <td>United States</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>6</th>
          <td>None</td>
          <td>London</td>
          <td>gb</td>
          <td>None</td>
          <td>united-kingdom</td>
          <td>/img/flags/png/gb.png</td>
          <td>//cdn6.f-cdn.com/img/flags/png/gb.png</td>
          <td>/img/flags/highres_png/united-kingdom.png</td>
          <td>//cdn5.f-cdn.com/img/flags/highres_png/united-...</td>
          <td>None</td>
          <td>...</td>
          <td>United Kingdom</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>7</th>
          <td>None</td>
          <td>Nashik</td>
          <td>in</td>
          <td>None</td>
          <td>india</td>
          <td>/img/flags/png/in.png</td>
          <td>//cdn2.f-cdn.com/img/flags/png/in.png</td>
          <td>/img/flags/highres_png/india.png</td>
          <td>//cdn3.f-cdn.com/img/flags/highres_png/india.png</td>
          <td>None</td>
          <td>...</td>
          <td>India</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>8</th>
          <td>None</td>
          <td>Timisoara</td>
          <td>ro</td>
          <td>None</td>
          <td>romania</td>
          <td>/img/flags/png/ro.png</td>
          <td>//cdn2.f-cdn.com/img/flags/png/ro.png</td>
          <td>/img/flags/highres_png/romania.png</td>
          <td>//cdn6.f-cdn.com/img/flags/highres_png/romania...</td>
          <td>None</td>
          <td>...</td>
          <td>Romania</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
        <tr>
          <th>9</th>
          <td>None</td>
          <td>Saginaw</td>
          <td>us</td>
          <td>None</td>
          <td>united-states</td>
          <td>/img/flags/png/us.png</td>
          <td>//cdn3.f-cdn.com/img/flags/png/us.png</td>
          <td>/img/flags/highres_png/united-states.png</td>
          <td>//cdn6.f-cdn.com/img/flags/highres_png/united-...</td>
          <td>None</td>
          <td>...</td>
          <td>United States</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
          <td>None</td>
        </tr>
      </tbody>
    </table>
    <p>10 rows × 22 columns</p>
    </div>


