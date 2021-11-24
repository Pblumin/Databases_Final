# # import app
# # import db
# # import MySQLdb.cursors
# from app import db

# class SCHOOL(db.Model):
#     __tablename__ = 'school'

#     sid = db.Column(db.Integer, primary_key=True)
#     sname = db.Column(db.String(20))

#     def __repr__(self):
#         return "<SCHOOL(sid=%s, sname='%s')>" % (self.sid, self.sname) 


# class PROFESSOR(db.Model):
#     __tablename__ = 'professor'

#     pid = db.Column(db.Integer, primary_key=True)
#     sid = db.Column(db.Integer, db.ForeignKey('school.sid'))
#     pname = db.Column(db.String(40))

#     teaches_at = db.relationship('PROFESSOR',
#                                 backref=db.backref('school', cascade='delete'))
                                
#     def __repr__(self):
#         return "<PROFESSOR(pid=%s, sid=%s, pname='%s')>" % (self.pid, self.sid, self.pname) 

# class CLASS(db.Model):
#     __tablename__ = 'class'
    
#     cid = db.Column(db.Integer, primary_key=True)
#     pid = db.Column(db.Integer, db.ForeignKey('professor.pid'))
#     cname = db.Column(db.String(50))

#     taught_by = db.relationship('CLASS',
#                                 backref=db.backref('professor', cascade='delete'))
                                
#     def __repr__(self):
#         return "<PROFESSOR(cid=%s, pid=%s, cname='%s')>" % (self.cid, self.pid, self.cname) 


# class USERS(db.Model):
#     __tablename__ = 'user'

#     uid = db.Column(db.Integer, primary_key=True)
#     uname = db.Column(db.String(20))
#     upass = db.Column(db.String(20))
                            
#     def __repr__(self):
#         return "<USERS(uid=%s, uname='%s', upass='%s')>" % (self.uid, self.uname, self.upass) 

# class REVIEW(db.Model):
#     __tablename__ = 'review'
#     #__table_args__ = (db.PrimaryKeyConstraint('sid', 'bid', 'eid', 'day'), {})
    
#     rid = db.Column(db.Integer, primary_key=True)
#     pid = db.Column(db.Integer, db.ForeignKey('professor.pid'))
#     uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
#     diffculty = db.Column(db.Integer)
#     overall = db.Column(db.Integer)
#     recommend = db.Column(db.Boolean)
#     description = db.Column(db.String(255))

#     has = db.relationship('REVIEW',
#                                 backref=db.backref('professor', cascade='delete'))

#     added_by = db.relationship('REVIEW',
#                                 backref=db.backref('user', cascade='delete'))
#     def __repr__(self):
#         return "<REVIEW(rid=%s, pid=%s, uid=%s, diffculty=%s, overall=%s, recommend=%s, description='%s')>" % (self.rid, self.pid, self.uid, self.diffculty, self.overall, self.recommend, self.description) 

# class LIKES(db.Model):
#     __tablename__ = 'likes'
#     #__table_args__ = (db.PrimaryKeyConstraint('sid', 'bid', 'eid', 'day'), {})
    
#     lid = db.Column(db.Integer, primary_key=True)
#     rid = db.Column(db.Integer, db.ForeignKey('review.pid'))
#     uid = db.Column(db.Integer, db.ForeignKey('user.pid'))

#     has = db.relationship('LIKES',
#                                 backref=db.backref('review', cascade='delete'))

#     gives = db.relationship('LIKES',
#                                 backref=db.backref('user', cascade='delete'))
#     def __repr__(self):
#         return "<LIKES(lid=%s, rid=%s, uid=%s)>" % (self.lid, self.rid, self.uid) 
