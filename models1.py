# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Exp001(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    scenenature = models.SmallIntegerField(db_column='SceneNature')  # Field name made lowercase.
    scenename = models.CharField(db_column='SceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp001'


class Exp002(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    scenenature = models.SmallIntegerField(db_column='SceneNature')  # Field name made lowercase.
    scenename = models.CharField(db_column='SceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp002'


class Exp003(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    scenenature = models.SmallIntegerField(db_column='SceneNature')  # Field name made lowercase.
    scenename = models.CharField(db_column='SceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp003'


class Exp004(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    scenenature = models.SmallIntegerField(db_column='SceneNature')  # Field name made lowercase.
    scenename = models.CharField(db_column='SceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp004'


class Exp005(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    leftscenenature = models.SmallIntegerField(db_column='LeftSceneNature')  # Field name made lowercase.
    leftscenename = models.CharField(db_column='LeftSceneName', max_length=60)  # Field name made lowercase.
    rightscenenature = models.SmallIntegerField(db_column='RightSceneNature')  # Field name made lowercase.
    rightscenename = models.CharField(db_column='RightSceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.
    foretime = models.CharField(db_column='ForeTime', max_length=60)  # Field name made lowercase.
    foremillisecond = models.BigIntegerField(db_column='ForeMilliSecond')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp005'


class Exp006(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    leftscenenature = models.SmallIntegerField(db_column='LeftSceneNature')  # Field name made lowercase.
    leftscenename = models.CharField(db_column='LeftSceneName', max_length=60)  # Field name made lowercase.
    rightscenenature = models.SmallIntegerField(db_column='RightSceneNature')  # Field name made lowercase.
    rightscenename = models.CharField(db_column='RightSceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.
    foretime = models.CharField(db_column='ForeTime', max_length=60)  # Field name made lowercase.
    foremillisecond = models.BigIntegerField(db_column='ForeMilliSecond')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp006'


class Exp007(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    scenenature = models.SmallIntegerField(db_column='SceneNature')  # Field name made lowercase.
    scenename = models.CharField(db_column='SceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp007'


class Exp0072(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    scenenature = models.SmallIntegerField(db_column='SceneNature')  # Field name made lowercase.
    scenename = models.CharField(db_column='SceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp007_2'


class Exp008(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey('Experimentrecordtable', db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    groupindex = models.BigIntegerField(db_column='GroupIndex')  # Field name made lowercase.
    scenenature = models.SmallIntegerField(db_column='SceneNature')  # Field name made lowercase.
    scenename = models.CharField(db_column='SceneName', max_length=60)  # Field name made lowercase.
    facenature = models.SmallIntegerField(db_column='FaceNature')  # Field name made lowercase.
    facename = models.CharField(db_column='FaceName', max_length=60)  # Field name made lowercase.
    facepos = models.SmallIntegerField(db_column='FacePos')  # Field name made lowercase.
    judgement = models.BigIntegerField(db_column='Judgement')  # Field name made lowercase.
    trialtime = models.FloatField(db_column='TrialTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exp008'


class Experimentrecordtable(models.Model):
    experimentrecordid = models.BigIntegerField(db_column='ExperimentRecordID', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey('Userinfotable', db_column='UserInfoID')  # Field name made lowercase.
    experimentname = models.CharField(db_column='ExperimentName', max_length=30)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=60)  # Field name made lowercase.
    times = models.IntegerField(db_column='Times')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'experimentrecordtable'


class Eyeexp001(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey(Experimentrecordtable, db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    lefteyecoordx = models.BigIntegerField(db_column='LeftEyeCoordX')  # Field name made lowercase.
    lefteyecoordy = models.BigIntegerField(db_column='LeftEyeCoordY')  # Field name made lowercase.
    righteyecoordx = models.BigIntegerField(db_column='RightEyeCoordX')  # Field name made lowercase.
    righteyecoordy = models.BigIntegerField(db_column='RightEyeCoordY')  # Field name made lowercase.
    leftrelocationcoordx = models.BigIntegerField(db_column='LeftRelocationCoordX')  # Field name made lowercase.
    leftrelocationcoordy = models.BigIntegerField(db_column='LeftRelocationCoordY')  # Field name made lowercase.
    rightrelocationcoordx = models.BigIntegerField(db_column='RightRelocationCoordX')  # Field name made lowercase.
    rightrelocationcoordy = models.BigIntegerField(db_column='RightRelocationCoordY')  # Field name made lowercase.
    valid = models.BigIntegerField(db_column='Valid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eyeexp001'


class Eyeexp005(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey(Experimentrecordtable, db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    lefteyecoordx = models.BigIntegerField(db_column='LeftEyeCoordX')  # Field name made lowercase.
    lefteyecoordy = models.BigIntegerField(db_column='LeftEyeCoordY')  # Field name made lowercase.
    righteyecoordx = models.BigIntegerField(db_column='RightEyeCoordX')  # Field name made lowercase.
    righteyecoordy = models.BigIntegerField(db_column='RightEyeCoordY')  # Field name made lowercase.
    leftrelocationcoordx = models.BigIntegerField(db_column='LeftRelocationCoordX')  # Field name made lowercase.
    leftrelocationcoordy = models.BigIntegerField(db_column='LeftRelocationCoordY')  # Field name made lowercase.
    rightrelocationcoordx = models.BigIntegerField(db_column='RightRelocationCoordX')  # Field name made lowercase.
    rightrelocationcoordy = models.BigIntegerField(db_column='RightRelocationCoordY')  # Field name made lowercase.
    valid = models.BigIntegerField(db_column='Valid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eyeexp005'


class Eyeexp006(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey(Experimentrecordtable, db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    lefteyecoordx = models.BigIntegerField(db_column='LeftEyeCoordX')  # Field name made lowercase.
    lefteyecoordy = models.BigIntegerField(db_column='LeftEyeCoordY')  # Field name made lowercase.
    righteyecoordx = models.BigIntegerField(db_column='RightEyeCoordX')  # Field name made lowercase.
    righteyecoordy = models.BigIntegerField(db_column='RightEyeCoordY')  # Field name made lowercase.
    leftrelocationcoordx = models.BigIntegerField(db_column='LeftRelocationCoordX')  # Field name made lowercase.
    leftrelocationcoordy = models.BigIntegerField(db_column='LeftRelocationCoordY')  # Field name made lowercase.
    rightrelocationcoordx = models.BigIntegerField(db_column='RightRelocationCoordX')  # Field name made lowercase.
    rightrelocationcoordy = models.BigIntegerField(db_column='RightRelocationCoordY')  # Field name made lowercase.
    valid = models.BigIntegerField(db_column='Valid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eyeexp006'


class Eyetobiiexp001(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey(Experimentrecordtable, db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    eyecoordx = models.BigIntegerField(db_column='EyeCoordX')  # Field name made lowercase.
    eyecoordy = models.BigIntegerField(db_column='EyeCoordY')  # Field name made lowercase.
    valid = models.BigIntegerField(db_column='Valid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eyetobiiexp001'


class Eyetobiiexp005(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey(Experimentrecordtable, db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    eyecoordx = models.BigIntegerField(db_column='EyeCoordX')  # Field name made lowercase.
    eyecoordy = models.BigIntegerField(db_column='EyeCoordY')  # Field name made lowercase.
    valid = models.BigIntegerField(db_column='Valid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eyetobiiexp005'


class Eyetobiiexp006(models.Model):
    experimentdataid = models.BigIntegerField(db_column='ExperimentDataID', primary_key=True)  # Field name made lowercase.
    experimentrecordid = models.ForeignKey(Experimentrecordtable, db_column='ExperimentRecordID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=60)  # Field name made lowercase.
    millisecond = models.BigIntegerField(db_column='MilliSecond')  # Field name made lowercase.
    eyecoordx = models.BigIntegerField(db_column='EyeCoordX')  # Field name made lowercase.
    eyecoordy = models.BigIntegerField(db_column='EyeCoordY')  # Field name made lowercase.
    valid = models.BigIntegerField(db_column='Valid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eyetobiiexp006'


class Imagearousalvote(models.Model):
    voteid = models.BigIntegerField(db_column='VoteID', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey('Userinfotable', db_column='UserInfoID')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imagearousalvote'


class Imagedescription(models.Model):
    descriptionid = models.BigIntegerField(db_column='DescriptionID', primary_key=True)  # Field name made lowercase.
    voteid = models.ForeignKey('Imagemmpivote', db_column='VoteID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imagedescription'


class Imagegeneralvote(models.Model):
    voteid = models.BigIntegerField(db_column='VoteID', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey('Userinfotable', db_column='UserInfoID')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imagegeneralvote'


class Imagemmpivote(models.Model):
    voteid = models.BigIntegerField(db_column='VoteID', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey('Userinfotable', db_column='UserInfoID')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imagemmpivote'


class Imagevalancevote(models.Model):
    voteid = models.BigIntegerField(db_column='VoteID', primary_key=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey('Userinfotable', db_column='UserInfoID')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imagevalancevote'


class ScaleAnswers(models.Model):
    answer_name = models.CharField(max_length=100)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scale_answers'


class ScaleItems(models.Model):
    item_name = models.CharField(max_length=100)
    parameter = models.CharField(max_length=10)
    scale_name = models.ForeignKey('ScaleScalename')
    sex = models.IntegerField()
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scale_items'


class ScaleItemsAnswer(models.Model):
    items = models.ForeignKey(ScaleItems)
    answers = models.ForeignKey(ScaleAnswers)

    class Meta:
        managed = False
        db_table = 'scale_items_answer'
        unique_together = (('items', 'answers'),)


class ScaleScalename(models.Model):
    name = models.CharField(max_length=50)
    describe = models.TextField()
    create_time = models.DateTimeField()
    rule = models.TextField()
    guidance = models.TextField()

    class Meta:
        managed = False
        db_table = 'scale_scalename'


class ScaleSubject(models.Model):
    identity = models.CharField(max_length=18)
    scale_id = models.CharField(max_length=11)
    user_id = models.CharField(max_length=11)
    score = models.CharField(max_length=100, blank=True, null=True)
    describe = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scale_subject'


class ScaleSubjectItemAnswer(models.Model):
    subject_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    answer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scale_subject_item_answer'


class Userinfotable(models.Model):
    userinfoid = models.BigIntegerField(db_column='UserInfoID', primary_key=True)  # Field name made lowercase.
    loginname = models.CharField(db_column='LoginName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=60, blank=True, null=True)  # Field name made lowercase.
    authority = models.IntegerField(db_column='Authority', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=25)  # Field name made lowercase.
    sex = models.IntegerField(db_column='Sex')  # Field name made lowercase.
    birthday = models.CharField(db_column='Birthday', max_length=20, blank=True, null=True)  # Field name made lowercase.
    education = models.CharField(db_column='Education', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)  # Field name made lowercase.
    studentid = models.CharField(db_column='StudentID', max_length=18)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinfotable'
