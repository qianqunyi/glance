# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import http.client as http

from glance.tests import functional


class TestSchemas(functional.SynchronousAPIBase):

    def setUp(self):
        super(TestSchemas, self).setUp()
        self.start_server()

    def test_resource(self):
        # Ensure the image link works and custom properties are loaded
        path = '/v2/schemas/image'
        response = self.api_get(path)
        self.assertEqual(http.OK, response.status_code)
        image_schema = response.json
        expected = set([
            'id',
            'name',
            'visibility',
            'checksum',
            'os_hash_algo',
            'os_hash_value',
            'created_at',
            'updated_at',
            'tags',
            'size',
            'virtual_size',
            'owner',
            'container_format',
            'disk_format',
            'self',
            'file',
            'status',
            'schema',
            'direct_url',
            'locations',
            'min_ram',
            'min_disk',
            'protected',
            'os_hidden',
            'stores',
        ])
        self.assertEqual(expected, set(image_schema['properties'].keys()))

        # Ensure the images link works and agrees with the image schema
        path = '/v2/schemas/images'
        response = self.api_get(path)
        self.assertEqual(http.OK, response.status_code)
        images_schema = response.json
        item_schema = images_schema['properties']['images']['items']
        self.assertEqual(item_schema, image_schema)
