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
