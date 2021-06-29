from sqlalchemy import inspect

db = None


class SqlAlchemyHelper(object):
    def __repr__(self):
        dict_data = self.to_dict()
        data_to_show = ["{}='{}'".format(k, v) for k, v in dict_data.items()]

        attrs_data = ",".join(data_to_show)
        return "{}({})".format(self.__class__.__name__, attrs_data)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
