import configparser
import filters
import json
import os
from pathlib import Path
import filter_applier_exception as fae
from filter_applier_exception import FilterApplierException


class FiltersApplier:
    def __init__(self, config_name):
        config = configparser.ConfigParser()
        config.read(config_name)
        self.input_data_location = config['data_location']['input_data_location']
        if not os.path.isdir(self.input_data_location):
            raise FilterApplierException(fae.NO_LOCATION, self.input_data_location)
        self.output_data_location = config['data_location']['output_data_location']
        if not os.path.isdir(self.output_data_location):
            os.makedirs(self.output_data_location)  # мб и не надо, в задании не обговорено
        self.filters = self._make_func_list(config['filters']['sequence'])

    @staticmethod
    def _make_func_list(filters_line: str) -> list:
        filters_list = filters_line.split(',')
        func_list = []
        for filter_name in filters_list:
            if filter_name in filters.func_dict:
                func_list.append(filters.func_dict[filter_name])
            else:
                raise FilterApplierException(fae.BAD_FILTER_NAME, filter_name)
        return func_list

    def apply_filters_to_all(self):
        for file in os.listdir(self.input_data_location):
            self._apply_filters(file)

    def _apply_all_filters(self, k, v, filename) -> tuple:
        for filter_func in self.filters:
            result = filter_func(k, v)
            if not result:
                return None
            k, v = result
        return k, v

    def _apply_filters(self, filename):
        with open(Path(self.input_data_location) / filename, 'r') as data:
            try:
                input_data = json.load(data)
            except Exception as e:
                raise FilterApplierException(fae.INVALID_JSON, filename, e)
        output_data = {}
        try:
            for k, v in input_data.items():
                result = self._apply_all_filters(k, v, filename)
                if not result:
                    continue
                k, v = result
                output_data[k] = v
        except Exception as e:
            raise FilterApplierException(fae.BAD_FILTER, e, filename)
        with open(Path(self.output_data_location) / filename, 'w') as data:
            json.dump(output_data, data)
