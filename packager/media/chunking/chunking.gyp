# Copyright 2017 Google Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

{
  'variables': {
    'shaka_code': 1,
  },
  'targets': [
    {
      'target_name': 'chunking',
      'type': '<(component)',
      'sources': [
        'chunking_handler.cc',
        'chunking_handler.h',
      ],
      'dependencies': [
        '../base/media_base.gyp:media_base',
      ],
    },
    {
      'target_name': 'chunking_unittest',
      'type': '<(gtest_target_type)',
      'sources': [
        'chunking_handler_unittest.cc',
      ],
      'dependencies': [
        '../../testing/gtest.gyp:gtest',
        '../../testing/gmock.gyp:gmock',
        '../base/media_base.gyp:media_handler_test_base',
        '../test/media_test.gyp:media_test_support',
        'chunking',
      ]
    },
  ],
}

