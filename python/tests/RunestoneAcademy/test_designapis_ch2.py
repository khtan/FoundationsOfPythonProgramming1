# region imports
import logging
import pytest
import json
import requests

logger = logging.getLogger(__name__)

def test_1_get():
    response = requests.get('https://farmstall.designapis.com/v1/reviews?maxRating=5')
    logger.info('reason: {}'.format(response.reason))
    logger.info('text: {}'.format(response.text[:150]))

    assert response.status_code == 200

    json = response.json()
    if len(json) > 0 :
        logger.info('item[0]: {}'.format(json[0]))
    else:
        logger.info('empty array')

def test_2_post():
    myobj = {'message': 'hi from earth', 'rating': 4}

    response = requests.post('https://farmstall.designapis.com/v1/reviews', json = myobj)
    logger.info('reason: {}'.format(response.reason))
    logger.info('text: {}'.format(response.text[:150]))

    assert response.status_code == 201


