#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(friend_reccomendation("Bobby")[1])
          <class 'str'>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(friend_reccomendation("Jared"))
          <class 'list'>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(friend_reccomendation("Jared"))
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

