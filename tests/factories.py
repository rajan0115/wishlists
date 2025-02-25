# Copyright 2016, 2019 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test Factory to make fake objects for testing
"""
import datetime
from datetime import date

import factory
from factory.fuzzy import FuzzyChoice, FuzzyDate
from service.models import Wishlists, Items


class WishlistsFactory(factory.Factory):
    """Creates fake pets that you don't have to feed"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Maps factory to data model"""

        model = Wishlists

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    customer_id = FuzzyChoice(choices=[1, 2,3])
    created_on = datetime.datetime.now()


class ItemsFactory(factory.Factory):
    """Creates fake pets that you don't have to feed"""


    class Meta:  # pylint: disable=too-few-public-methods
        """Maps factory to data model"""

        model = Items

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    wishlist_id = 1
    product_id = FuzzyChoice(choices=[1, 2,3])
    rank = FuzzyChoice(choices=[1, 2,3])
    quantity = FuzzyChoice(choices=[1, 2,3])
    price = FuzzyChoice(choices=[100, 200,300])






