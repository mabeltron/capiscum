from ap import admin, db
from models import Account, Check, Groupcheck, Groupreply, Postauth, Reply, Usergroup
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(Account, db.session))
admin.add_view(ModelView(Check, db.session))
admin.add_view(ModelView(Groupcheck, db.session))
admin.add_view(ModelView(Groupreply, db.session))
admin.add_view(ModelView(Postauth, db.session))
admin.add_view(ModelView(Reply, db.session))
admin.add_view(ModelView(Usergroup, db.session))
