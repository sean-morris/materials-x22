test = {   'name': 'q3_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> set(faithful_predictions.labels) == set(['duration', 'wait', 'predicted wait']) # Make sure your column labels are correct.\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> abs(1 - np.mean(faithful_predictions.column(2))/100) <= 0.35\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
