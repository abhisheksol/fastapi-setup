# app/admin.py

from sqladmin import Admin, ModelView
from app.database import engine, Base


def setup_admin(app):
    admin = Admin(app, engine)

    # Loop through all registered models
    for mapper in Base.registry.mappers:
        model = mapper.class_

        # Create dynamic ModelView
        class DynamicAdmin(ModelView, model=model):
            column_list = [c.name for c in model.__table__.columns]

        admin.add_view(DynamicAdmin)
