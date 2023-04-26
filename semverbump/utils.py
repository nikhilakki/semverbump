# Copyright (c) 2023 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


class TomlWriter:
    @staticmethod
    def _dumps_value(value):
        if isinstance(value, bool):
            return "true" if value else "false"
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, list):
            return f"[{', '.join(TomlWriter._dumps_value(v) for v in value)}]"
        else:
            raise TypeError(f"{type(value).__name__} {value!r} is not supported")

    @staticmethod
    def dumps(toml_dict, table=""):
        toml = []
        for key, value in toml_dict.items():
            if isinstance(value, dict):
                table_key = f"{table}.{key}" if table else key
                toml.append(f"\n[{table_key}]\n{TomlWriter.dumps(value, table_key)}")
            else:
                toml.append(f"{key} = {TomlWriter._dumps_value(value)}")
        return "\n".join(toml)
