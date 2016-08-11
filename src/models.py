from ap import db

class Account(db.Model):
    __tablename__ = "radacct"
    id = db.Column('radacctid', db.Integer, primary_key=True)
    session_id = db.Column('acctsessionid', db.String(64))
    unique_id = db.Column('acctuniqueid', db.String(32), unique=True)
    username = db.Column(db.String(253))
    groupname = db.Column(db.String(253))
    realm = db.Column(db.String(64))
    nasipaddress = db.Column(db.String(16))
    nasportid = db.Column(db.String(15))
    nasporttype = db.Column(db.String(32))
    acctstarttime = db.Column(db.DateTime)
    acctstoptime = db.Column(db.DateTime)
    acctsessiontime = db.Column(db.Integer)
    acctauthentic = db.Column(db.String(32))
    connectinfo_start = db.Column(db.String(50))
    connectinfo_stop = db.Column(db.String(50))
    acctinputoctets = db.Column(db.Integer)
    acctoutputoctets = db.Column(db.Integer)
    calledstationid = db.Column(db.String(50))
    callingstationid = db.Column(db.String(50))
    acctterminatecause = db.Column(db.String(32))
    servicetype = db.Column(db.String(32))
    xascendsessionsvrkey = db.Column(db.String(10))
    framedprotocol = db.Column(db.String(32))
    framedipaddress = db.Column(db.String(16))
    acctstartdelay = db.Column(db.Integer)
    acctstopdelay = db.Column(db.Integer)

class Check(db.Model):
    __tablename__ = "radcheck"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    attribute = db.Column(db.String(64))
    op = db.Column(db.String(2))
    value = db.Column(db.String(253))

class Groupcheck(db.Model):
    __tablename__ = "radgroupcheck"
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(64))
    attribute = db.Column(db.String(64))
    op = db.Column(db.String(2))
    value = db.Column(db.String(253))

class Groupreply(db.Model):
    __tablename__ = "radgroupreply"
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(64))
    attribute = db.Column(db.String(64))
    op = db.Column(db.String(2))
    value = db.Column(db.String(253))

class Postauth(db.Model):
    __tablename__ = "radpostauth"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(253))
    passwd = db.Column('pass', db.String(128))
    reply = db.Column(db.String(32))
    calledstationid = db.Column(db.String(50))
    callingstationid = db.Column(db.String(50))
    authdate = db.Column(db.DateTime)

class Reply(db.Model):
    __tablename__ = "radreply"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    attribute = db.Column(db.String(64))
    op = db.Column(db.String(2))
    value = db.Column(db.String(253))

class Usergroup(db.Model):
    __tablename__ = "radusergroup"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(253))
    groupname = db.Column(db.String(64))
    priority = db.Column(db.Integer)
