# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Acccomments(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    comment = models.TextField()
    secret = models.CharField(max_length=10)
    commentid = models.AutoField(db_column='commentID', primary_key=True)  # Field name made lowercase.
    timestamp = models.IntegerField()
    likes = models.IntegerField()
    isspam = models.IntegerField(db_column='isSpam')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acccomments'


class Accounts(models.Model):
    username = models.CharField(db_column='userName', unique=True, max_length=255)  # Field name made lowercase.
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    accountid = models.AutoField(db_column='accountID', primary_key=True)  # Field name made lowercase.
    savedata = models.TextField(db_column='saveData')  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='isAdmin')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    friends = models.CharField(max_length=1024)
    blockedby = models.CharField(db_column='blockedBy', max_length=1024)  # Field name made lowercase.
    blocked = models.CharField(max_length=1024)
    ms = models.IntegerField(db_column='mS')  # Field name made lowercase.
    frs = models.IntegerField(db_column='frS')  # Field name made lowercase.
    youtubeurl = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    twitch = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    registerdate = models.IntegerField(db_column='registerDate')  # Field name made lowercase.
    friendscount = models.IntegerField(db_column='friendsCount')  # Field name made lowercase.
    savekey = models.TextField(db_column='saveKey')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts'


class Actions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField()
    value = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    value2 = models.CharField(max_length=255)
    value3 = models.IntegerField()
    value4 = models.IntegerField()
    value5 = models.IntegerField()
    value6 = models.IntegerField()
    account = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'actions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bannedips(models.Model):
    ip = models.CharField(db_column='IP', max_length=255)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bannedips'


class Blocks(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person1 = models.IntegerField()
    person2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blocks'


class Comments(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    comment = models.TextField()
    secret = models.CharField(max_length=10)
    levelid = models.IntegerField(db_column='levelID')  # Field name made lowercase.
    commentid = models.AutoField(db_column='commentID', primary_key=True)  # Field name made lowercase.
    timestamp = models.IntegerField()
    likes = models.IntegerField()
    percent = models.IntegerField()
    isspam = models.IntegerField(db_column='isSpam')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comments'


class Cpshares(models.Model):
    shareid = models.AutoField(db_column='shareID', primary_key=True)  # Field name made lowercase.
    levelid = models.IntegerField(db_column='levelID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cpshares'


class Dailyfeatures(models.Model):
    feaid = models.AutoField(db_column='feaID', primary_key=True)  # Field name made lowercase.
    levelid = models.IntegerField(db_column='levelID')  # Field name made lowercase.
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dailyfeatures'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Friendreqs(models.Model):
    accountid = models.IntegerField(db_column='accountID')  # Field name made lowercase.
    toaccountid = models.IntegerField(db_column='toAccountID')  # Field name made lowercase.
    comment = models.CharField(max_length=1000)
    uploaddate = models.IntegerField(db_column='uploadDate')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friendreqs'


class Friendships(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person1 = models.IntegerField()
    person2 = models.IntegerField()
    isnew1 = models.IntegerField(db_column='isNew1')  # Field name made lowercase.
    isnew2 = models.IntegerField(db_column='isNew2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friendships'


class Gauntlets(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    level1 = models.IntegerField()
    level2 = models.IntegerField()
    level3 = models.IntegerField()
    level4 = models.IntegerField()
    level5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gauntlets'


class Levels(models.Model):
    gameversion = models.IntegerField(db_column='gameVersion')  # Field name made lowercase.
    binaryversion = models.IntegerField(db_column='binaryVersion')  # Field name made lowercase.
    username = models.TextField(db_column='userName')  # Field name made lowercase.
    levelid = models.AutoField(db_column='levelID', primary_key=True)  # Field name made lowercase.
    levelname = models.CharField(db_column='levelName', max_length=255)  # Field name made lowercase.
    leveldesc = models.TextField(db_column='levelDesc')  # Field name made lowercase.
    levelversion = models.IntegerField(db_column='levelVersion')  # Field name made lowercase.
    levellength = models.IntegerField(db_column='levelLength')  # Field name made lowercase.
    audiotrack = models.IntegerField(db_column='audioTrack')  # Field name made lowercase.
    auto = models.IntegerField()
    password = models.IntegerField()
    original = models.IntegerField()
    twoplayer = models.IntegerField(db_column='twoPlayer')  # Field name made lowercase.
    songid = models.IntegerField(db_column='songID')  # Field name made lowercase.
    objcount = models.IntegerField(db_column='objects')
    coins = models.IntegerField()
    requestedstars = models.IntegerField(db_column='requestedStars')  # Field name made lowercase.
    extrastring = models.TextField(db_column='extraString')  # Field name made lowercase.
    levelstring = models.TextField(db_column='levelString')  # Field name made lowercase.
    levelinfo = models.TextField(db_column='levelInfo')  # Field name made lowercase.
    secret = models.TextField()
    stardifficulty = models.IntegerField(db_column='starDifficulty')  # Field name made lowercase.
    downloads = models.IntegerField()
    likes = models.IntegerField()
    stardemon = models.IntegerField(db_column='starDemon')  # Field name made lowercase.
    starauto = models.CharField(db_column='starAuto', max_length=11)  # Field name made lowercase.
    starstars = models.IntegerField(db_column='starStars')  # Field name made lowercase.
    uploaddate = models.CharField(db_column='uploadDate', max_length=1337)  # Field name made lowercase.
    updatedate = models.IntegerField(db_column='updateDate')  # Field name made lowercase.
    starcoins = models.IntegerField(db_column='starCoins')  # Field name made lowercase.
    starfeatured = models.IntegerField(db_column='starFeatured')  # Field name made lowercase.
    starhall = models.IntegerField(db_column='starHall')  # Field name made lowercase.
    starepic = models.IntegerField(db_column='starEpic')  # Field name made lowercase.
    stardemondiff = models.IntegerField(db_column='starDemonDiff')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    extid = models.CharField(db_column='extID', max_length=255)  # Field name made lowercase.
    unlisted = models.IntegerField()
    originalreup = models.IntegerField(db_column='originalReup')  # Field name made lowercase.
    hostname = models.CharField(max_length=255)
    iscpshared = models.IntegerField(db_column='isCPShared')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'levels'


class Levelscores(models.Model):
    scoreid = models.AutoField(db_column='scoreID', primary_key=True)  # Field name made lowercase.
    accountid = models.IntegerField(db_column='accountID')  # Field name made lowercase.
    levelid = models.IntegerField(db_column='levelID')  # Field name made lowercase.
    percent = models.IntegerField()
    uploaddate = models.IntegerField(db_column='uploadDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'levelscores'


class Links(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accountid = models.IntegerField(db_column='accountID')  # Field name made lowercase.
    targetaccountid = models.IntegerField(db_column='targetAccountID')  # Field name made lowercase.
    server = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    targetuserid = models.IntegerField(db_column='targetUserID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'links'


class Mappacks(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    levels = models.CharField(max_length=512)
    stars = models.IntegerField()
    coins = models.IntegerField()
    difficulty = models.IntegerField()
    rgbcolors = models.CharField(max_length=11)
    colors2 = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'mappacks'


class Messages(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    body = models.TextField()
    subject = models.TextField()
    accid = models.IntegerField(db_column='accID')  # Field name made lowercase.
    messageid = models.AutoField(db_column='messageID', primary_key=True)  # Field name made lowercase.
    toaccountid = models.IntegerField(db_column='toAccountID')  # Field name made lowercase.
    timestamp = models.IntegerField()
    secret = models.CharField(max_length=25)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'messages'


class Modactions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField()
    value = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    value2 = models.CharField(max_length=255)
    value3 = models.IntegerField()
    value4 = models.IntegerField()
    value5 = models.IntegerField()
    value6 = models.IntegerField()
    account = models.IntegerField()
    value7 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'modactions'


class Modips(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=69)  # Field name made lowercase.
    ismod = models.IntegerField(db_column='isMod')  # Field name made lowercase.
    accountid = models.IntegerField(db_column='accountID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modips'


class Quests(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField()
    amount = models.IntegerField()
    reward = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'quests'


class Reports(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    levelid = models.IntegerField(db_column='levelID')  # Field name made lowercase.
    hostname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'reports'


class Songs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    authorid = models.IntegerField(db_column='authorID')  # Field name made lowercase.
    authorname = models.CharField(db_column='authorName', max_length=100)  # Field name made lowercase.
    size = models.CharField(max_length=100)
    download = models.CharField(max_length=1337)
    hash = models.CharField(max_length=256)
    isdisabled = models.IntegerField(db_column='isDisabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'songs'


class Users(models.Model):
    isregistered = models.IntegerField(db_column='isRegistered')  # Field name made lowercase.
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    extid = models.CharField(db_column='extID', max_length=100)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=69)  # Field name made lowercase.
    stars = models.IntegerField()
    demons = models.IntegerField()
    icon = models.IntegerField()
    color1 = models.IntegerField()
    color2 = models.IntegerField()
    icontype = models.IntegerField(db_column='iconType')  # Field name made lowercase.
    coins = models.IntegerField()
    usercoins = models.IntegerField(db_column='userCoins')  # Field name made lowercase.
    special = models.IntegerField()
    gameversion = models.IntegerField(db_column='gameVersion')  # Field name made lowercase.
    secret = models.CharField(max_length=69)
    accicon = models.IntegerField(db_column='accIcon')  # Field name made lowercase.
    accship = models.IntegerField(db_column='accShip')  # Field name made lowercase.
    accball = models.IntegerField(db_column='accBall')  # Field name made lowercase.
    accbird = models.IntegerField(db_column='accBird')  # Field name made lowercase.
    accdart = models.IntegerField(db_column='accDart')  # Field name made lowercase.
    accrobot = models.IntegerField(db_column='accRobot', blank=True, null=True)  # Field name made lowercase.
    accglow = models.IntegerField(db_column='accGlow')  # Field name made lowercase.
    creatorpoints = models.DecimalField(db_column='creatorPoints', max_digits=10, decimal_places=0)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=69)  # Field name made lowercase.
    lastplayed = models.IntegerField(db_column='lastPlayed')  # Field name made lowercase.
    diamonds = models.IntegerField()
    orbs = models.IntegerField()
    completedlvls = models.IntegerField(db_column='completedLvls')  # Field name made lowercase.
    accspider = models.IntegerField(db_column='accSpider')  # Field name made lowercase.
    accexplosion = models.IntegerField(db_column='accExplosion')  # Field name made lowercase.
    chest1time = models.IntegerField()
    chest2time = models.IntegerField()
    chest1count = models.IntegerField()
    chest2count = models.IntegerField()
    isbanned = models.IntegerField(db_column='isBanned')  # Field name made lowercase.
    iscreatorbanned = models.IntegerField(db_column='isCreatorBanned')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
