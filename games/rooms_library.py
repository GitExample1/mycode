#!/usr/bin/python3

## Library for rooms and items
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room':{
                  'east'  : 'Porch',
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion'
                },
            'Garden' : {
                  'north' : 'Dining Room'
                },
            'Porch' : {
                  'west'  : 'Dining Room',
                  'item'  : 'lucky_coin'
                }

         }
