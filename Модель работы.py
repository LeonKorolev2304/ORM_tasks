class Jobs(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.Datetime, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.Datetime, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean,
                              index=True, unique=True, nullable=True)
    user = orm.relationship('User')
