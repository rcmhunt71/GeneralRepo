# def _build_id_list(self, key: str = None, data_set: typing.OrderedDict = None, tag=None, depth=0) -> typing.List:
#     data_set = data_set if data_set is not None else self.data
#     parent_keys = [key] if key is not None else [x for x in self.data.keys()]
#     set_data = []
#
#     # tab_char = "\t"
#     # tab = f'{depth}  {tab_char * depth}'
#     # if self.index == target_index:
#     #     print(f"{tab}DATA SET:\n{tab}{pprint.pformat(data_set)}")
#     #     print(f"{tab}PARENT KEYS: {parent_keys}")
#
#     for p_key in parent_keys:
#         if p_key.startswith('@'):
#             continue
#
#         asset_data = data_set.get(p_key, data_set)
#         tag = p_key if tag is None else f"{tag}:{p_key}"
#
#         # if self.index == target_index:
#         #     print(f"{tab}TAG: {tag}\n{tab}KEY: {p_key}\n{tab}DATA: {pprint.pformat(asset_data)}\n")
#
#         set_data.extend([f"{tag}:{key}:{value}" for key, value in asset_data.items() if
#                          not isinstance(value, OrderedDict) and not key.startswith('@')])
#
#         ## WORKS
#         for key, value in asset_data.items():
#             if isinstance(value, OrderedDict):
#                 # print(f"{tab}ITERATION {depth + 1}:\n"
#                 #       f"{tab}S----------------\n"
#                 #       f"{tab}TAG: '{tag}'\n{tab}SUBKEY: '{key}'\n{tab}DATA_SET  {value}\n")
#                 set_data.extend(self._build_id_list(key=key, data_set=value, tag=tag, depth=depth + 1))
#                 # print(f"{tab}E------------------\n")
#
#         # print(f"{tab}{key}:: UPDATED DATA LIST: {set_data}\n")
#
#     return set_data


class TestEq:
    def __init__(self, id_set):
        self.id_set = id_set

    def __eq__(self, other):
        """
        Equality is where the symmetric difference (set_x ^ set_y) of the sets is 0.
        Symmetric different = new set with elements in either self or other, but not both.

        :param other: Instantiated/populated BaseDealElement Obj
        :return: Boolean
        """
        return self.id_set == other.id_set

    def __lt__(self, other):
        """
        Less Than: not equal AND is a subset, but other has more elements
        :param other: Instantiated/populated BaseDealElement Obj
        :return: Boolean
        """

        is_eq, is_subset, is_superset = self._get_comparison(other=other)
        return not is_eq and is_subset

    def __le__(self, other):
        """
        Less Than or Equal To:
           * Equals: equal sets
               OR
           * Less Than: not equal AND is a subset but other has more elements

        :param other: Instantiated/populated BaseDealElement Obj
        :return: Boolean
        """
        return self == other or self < other

    def __gt__(self, other):
        """
        Greater Than: not equal AND is a subset, but self has more elements
        :param other: Instantiated/populated BaseDealElement Obj
        :return: Boolean
        """
        is_eq, is_subset, is_superset = self._get_comparison(other=other)
        return not is_eq and is_superset

    def __ge__(self, other):
        """
        Greater Than or Equal To:
           * Equals: equal sets
               OR
           * Greater Than: not equal AND is a subset AND self has more elements

        :param other: Instantiated/populated BaseDealElement Obj
        :return: Boolean
        """
        return self == other or self > other

    def __ne__(self, other):
        """
        Are the sets completely unequal (no common elements, disjoint)
        :param other: Instantiated/populated BaseDealElement Obj
        :return: Boolean
        """
        return self.id_set.isdisjoint(other.id_set)

    def _get_comparison(self, other):
        """
        Determine various metrics about the sets. This will determine equality, size different, and are they subsets.
        :param other: Instantiated/populated BaseDealElement Obj
        :return: (tuple): is_equal, is_subset, difference_in_length
        """
        is_equal = self == other
        is_subset = self.id_set.issubset(other.id_set)
        is_superset = self.id_set.issuperset(other.id_set)
        return is_equal, is_subset, is_superset


if __name__ == "__main__":

    data = [
        ['foo', 'poo', 'doo'],
        ['foo', 'poo', 'doo', 'noo'],
        ['foo', 'poo'],
        ['cat', 'dog', 'horse'],
    ]

    first_set = data[0]

    for second_set in data:
        set1 = TestEq(id_set=set(first_set))
        set2 = TestEq(id_set=set(second_set))

        print("-" * 80)
        print(f"SET 1: {first_set}\nSET 2: {second_set}\n")
        print(f"Is obj1 == obj 2: {set1 == set2}")
        print(f"Is obj1 >  obj 2: {set1 > set2}")
        print(f"Is obj1 >= obj 2: {set1 >= set2}")
        print(f"Is obj1 < obj 2: {set1 < set2}")
        print(f"Is obj1 <= obj 2: {set1 <= set2}")
        print(f"Is obj1 != obj 2: {set1 != set2}\n")


# TEST: set1 = data_1, set2 == data_1
# TEST: set1 = data_1, set2 == data_2
# TEST: set1 = data_1, set2 == data_3
